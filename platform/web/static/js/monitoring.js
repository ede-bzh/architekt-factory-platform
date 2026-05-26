/**
 * Live monitoring dashboard — shared by monitoring.html and _partial_monitoring.html.
 * Poll interval matches MONITORING_CACHE_TTL (20s) on /api/monitoring/live.
 */
(function () {
  "use strict";

  const POLL_INTERVAL_MS = 20000;
  let currentHours = 24;
  let pollTimer = null;

  function fmt(n) {
    if (n == null) return "—";
    if (n >= 1e6) return (n / 1e6).toFixed(1) + "M";
    if (n >= 1e3) return (n / 1e3).toFixed(1) + "K";
    return String(n);
  }

  function fmtUsd(n) {
    return "$" + (n || 0).toFixed(2);
  }

  function fmtTime(sec) {
    if (!sec) return "—";
    if (sec < 60) return sec + "s";
    if (sec < 3600) return Math.floor(sec / 60) + "m";
    const h = Math.floor(sec / 3600);
    const m = Math.floor((sec % 3600) / 60);
    return h + "h" + (m ? m + "m" : "");
  }

  function badges(obj, el) {
    if (!el) return;
    const colors = {
      completed: "green",
      done: "green",
      active: "blue",
      running: "blue",
      in_progress: "purple",
      failed: "red",
      pending: "yellow",
      backlog: "yellow",
      planning: "yellow",
      blocked: "red",
      review: "purple",
    };
    const entries = Object.entries(obj || {});
    if (entries.length === 0) {
      el.innerHTML = '<span class="mon-empty">—</span>';
      return;
    }
    el.innerHTML = entries
      .map(
        ([k, v]) =>
          `<span class="mon-badge ${colors[k] || "purple"}">${k}: ${v}</span>`
      )
      .join("");
  }

  function barColor(pct) {
    return pct > 80 ? "red" : pct > 60 ? "yellow" : "green";
  }

  function $(id) {
    return document.getElementById(id);
  }

  function setText(id, text) {
    const el = $(id);
    if (el) el.textContent = text;
  }

  async function refresh() {
    if (!$("monRoot")) return;
    try {
      const r = await fetch("/api/monitoring/live?hours=" + currentHours);
      if (!r.ok) return;
      const d = await r.json();
      const s = d.system || {};

      setText("monCpu", (s.cpu_percent || 0) + "%");
      setText("monCpuSys", "System: " + (s.sys_cpu_percent || 0) + "%");
      const cpuBar = $("monCpuBar");
      if (cpuBar) {
        cpuBar.style.width = Math.min(s.cpu_percent || 0, 100) + "%";
        cpuBar.className = "mon-bar-fill " + barColor(s.cpu_percent || 0);
      }

      setText("monMem", (s.mem_rss_mb || 0).toFixed(1) + " MB");
      setText(
        "monMemSys",
        (s.sys_mem_used_gb || 0).toFixed(1) +
          " / " +
          (s.sys_mem_total_gb || 0).toFixed(1) +
          " GB (" +
          (s.sys_mem_percent || 0) +
          "%)"
      );
      const memBar = $("monMemBar");
      if (memBar) {
        memBar.style.width = (s.sys_mem_percent || 0) + "%";
        memBar.className = "mon-bar-fill " + barColor(s.sys_mem_percent || 0);
      }

      setText("monDisk", (s.disk_percent || 0) + "%");
      setText(
        "monDiskSub",
        (s.disk_used_gb || 0).toFixed(1) +
          " / " +
          (s.disk_total_gb || 0).toFixed(1) +
          " GB"
      );
      const diskBar = $("monDiskBar");
      if (diskBar) {
        diskBar.style.width = (s.disk_percent || 0) + "%";
        diskBar.className = "mon-bar-fill " + barColor(s.disk_percent || 0);
      }

      setText("monUptime", "Uptime: " + fmtTime(s.uptime_seconds));
      setText("monPid", s.pid || "—");
      setText("monThreads", s.threads || "—");
      setText("monFiles", s.open_files || "—");

      const ag = d.agents || {};
      setText("monAgentsRegistered", ag.registered || 0);
      setText("monAgentsActive", ag.active || 0);
      setText("monAgentsParticipated", ag.participated || 0);
      setText("monAgentsSessions", ag.sessions_with_agents || 0);

      const msg = d.messages || {};
      setText("monMsg24h", fmt(msg.last_24h || 0));
      setText("monMsgTotal", fmt(msg.total || 0));
      setText("monProjects", d.projects || 0);

      const l = d.llm || {};
      const periodLabels = { 24: "24h", 168: "7d", 720: "30d", 8760: "1y" };
      setText(
        "monLlmPeriod",
        "(" + (periodLabels[currentHours] || currentHours + "h") + ")"
      );
      setText("monLlmCalls", fmt(l.total_calls || 0));
      setText("monLlmIn", fmt(l.total_tokens_in || 0));
      setText("monLlmOut", fmt(l.total_tokens_out || 0));
      setText("monLlmCost", "$" + (l.total_cost_usd || 0).toFixed(2));
      setText(
        "monLlmLatency",
        l.avg_duration_ms ? Math.round(l.avg_duration_ms) + "ms" : "—"
      );
      setText("monLlmErrors", l.error_count || 0);

      const chart = $("monLlmChart");
      if (chart) {
        if (l.hourly && l.hourly.length > 0) {
          const maxCalls = Math.max(...l.hourly.map((h) => h.calls), 1);
          chart.innerHTML = l.hourly
            .map((h) => {
              const pct = Math.max((h.calls / maxCalls) * 100, 2);
              return `<div class="mon-chart-bar" style="height:${pct}%" title="${h.hour}h: ${h.calls} calls, ${fmt(h.tokens)} tok, $${h.cost.toFixed(3)}"></div>`;
            })
            .join("");
        } else {
          chart.innerHTML =
            '<div class="mon-empty" style="margin:auto">No hourly data</div>';
        }
      }

      const prov = $("monProviders");
      if (prov) {
        if (l.by_provider && l.by_provider.length > 0) {
          prov.innerHTML = l.by_provider
            .map(
              (p) =>
                `<tr><td>${p.provider}</td><td style="font-size:0.7rem">${p.model}</td><td>${p.calls}</td><td>$${(p.cost_usd || 0).toFixed(3)}</td><td>${Math.round(p.avg_ms || 0)}</td></tr>`
            )
            .join("");
        } else {
          prov.innerHTML =
            '<tr><td colspan="5" class="mon-empty">No LLM calls yet</td></tr>';
        }
      }

      const agentsTb = $("monTopAgents");
      if (agentsTb) {
        if (l.by_agent && l.by_agent.length > 0) {
          agentsTb.innerHTML = l.by_agent
            .slice(0, 10)
            .map((a) => {
              const grade = a.capability_grade || "executor";
              const badge =
                grade === "organizer"
                  ? '<span style="font-size:0.65rem;padding:1px 5px;border-radius:3px;background:var(--accent-purple,#7c3aed);color:#fff">org</span>'
                  : '<span style="font-size:0.65rem;padding:1px 5px;border-radius:3px;background:var(--accent-blue,#2563eb);color:#fff">exec</span>';
              return `<tr><td>${a.agent_id}</td><td>${badge}</td><td>${a.calls}</td><td>${fmt(a.tokens_out || 0)}</td><td>$${(a.cost_usd || 0).toFixed(3)}</td></tr>`;
            })
            .join("");
        } else {
          agentsTb.innerHTML =
            '<tr><td colspan="5" class="mon-empty">No agent data yet</td></tr>';
        }
      }

      badges(d.missions, $("monMissions"));
      badges(d.sprints, $("monSprints"));
      badges(d.features, $("monFeatures"));

      const memEl = $("monMemory");
      if (memEl && d.memory && typeof d.memory === "object") {
        const entries = Object.entries(d.memory);
        if (entries.length > 0) {
          memEl.innerHTML = entries
            .map(([k, v]) => {
              const label = k.replace(/_/g, " ");
              return `<div class="mon-col"><div class="label">${label}</div><div class="val">${typeof v === "number" ? fmt(v) : v || "—"}</div></div>`;
            })
            .join("");
        } else {
          memEl.innerHTML =
            '<span class="mon-empty">No memory data</span>';
        }
      }

      const db = d.database || {};
      setText(
        "monDbSize",
        db.size_mb != null ? db.size_mb.toFixed(1) + " MB" : "—"
      );
      setText("monDbTables", db.tables || "—");
      setText("monDbRows", fmt(db.total_rows || 0));
      if ($("monDbSchemaVer")) {
        setText(
          "monDbSchemaVer",
          db.schema_version != null ? "v" + db.schema_version : "—"
        );
      }
      if ($("monDbJournal")) {
        setText("monDbJournal", db.journal_mode || "—");
      }
      const tbEl = $("monDbTopTables");
      if (tbEl) {
        if (db.top_tables && db.top_tables.length > 0) {
          tbEl.innerHTML = db.top_tables
            .map(
              ([name, cnt]) =>
                `<tr><td>${name}</td><td style="text-align:right">${fmt(cnt)}</td></tr>`
            )
            .join("");
        } else {
          tbEl.innerHTML =
            '<tr><td colspan="2" class="mon-empty">No tables</td></tr>';
        }
      }

      const v = d.vectors || {};
      setText("monVecTotal", fmt(v.total_vectors || 0));
      setText("monVecEmbedded", fmt(v.with_embedding || 0));
      setText("monVecScopes", v.scopes || 0);
      setText("monVecDim", v.dimension || "—");
      setText("monVecProvider", v.provider || "No provider configured");
      const vecPct =
        v.total_vectors > 0
          ? Math.round(((v.with_embedding || 0) / v.total_vectors) * 100)
          : 0;
      const vecBar = $("monVecBar");
      if (vecBar) vecBar.style.width = vecPct + "%";
      setText("monVecPct", vecPct + "% embedded");

      if (d.mcp) {
        const mcpEl = $("monMcpServers");
        if (mcpEl) {
          const entries = Object.entries(d.mcp).filter(([k]) => k !== "error");
          if (entries.length > 0) {
            mcpEl.innerHTML = entries
              .map(([name, info]) => {
                const up = info.status === "up" || info.status === "ok";
                const statusClass = up ? "mon-dot-up" : "mon-dot-down";
                const port = info.port ? `:${info.port}` : "";
                const detail = [];
                if (info.tools) detail.push(info.tools + " tools");
                if (info.sessions !== undefined)
                  detail.push(info.sessions + " sessions");
                if (info.entries !== undefined)
                  detail.push(fmt(info.entries) + " entries");
                if (info.size_mb) detail.push(info.size_mb + " MB");
                return `<div class="mon-mcp-item"><span class="mon-dot ${statusClass}"></span><span class="mon-mcp-name">${name}</span><span class="mon-mcp-detail">${port}${detail.length ? " · " + detail.join(" · ") : ""}</span></div>`;
              })
              .join("");
          } else {
            mcpEl.innerHTML =
              '<div class="mon-empty">No MCP servers detected</div>';
          }
        }
      }

      const req = d.requests || {};
      setText("monReqTotal", fmt(req.total_requests || 0));
      setText("monReq4xx", fmt(req.errors_4xx || 0));
      setText("monReq5xx", fmt(req.errors_5xx || 0));
      setText(
        "monReqAvg",
        req.avg_ms ? req.avg_ms.toFixed(1) + "ms" : "—"
      );
      const reqEndEl = $("monReqEndpoints");
      if (reqEndEl) {
        if (req.top_endpoints && req.top_endpoints.length > 0) {
          reqEndEl.innerHTML = req.top_endpoints
            .slice(0, 10)
            .map(
              (ep) =>
                `<tr><td style="font-size:0.7rem">${ep.endpoint}</td><td style="text-align:right">${fmt(ep.hits)}</td><td style="text-align:right">${ep.avg_ms}ms</td><td style="text-align:right;color:${ep.p95_ms > 500 ? "var(--red, #ef4444)" : "inherit"}">${ep.p95_ms}ms</td></tr>`
            )
            .join("");
        } else {
          reqEndEl.innerHTML =
            '<tr><td colspan="4" class="mon-empty">No requests yet</td></tr>';
        }
      }
      const statColors = {
        200: "green",
        201: "green",
        204: "green",
        301: "blue",
        302: "blue",
        304: "blue",
        400: "yellow",
        401: "yellow",
        403: "yellow",
        404: "yellow",
        500: "red",
        502: "red",
        503: "red",
      };
      const reqStatusEl = $("monReqStatus");
      if (reqStatusEl) {
        if (req.by_status && Object.keys(req.by_status).length > 0) {
          reqStatusEl.innerHTML = Object.entries(req.by_status)
            .map(
              ([code, cnt]) =>
                `<span class="mon-badge ${statColors[code] || "purple"}">${code}: ${cnt}</span>`
            )
            .join("");
        } else {
          reqStatusEl.innerHTML = '<span class="mon-empty">—</span>';
        }
      }

      const mcpC = d.mcp_calls || {};
      setText("monMcpCallsTotal", fmt(mcpC.total_calls || 0));
      setText("monMcpCallsErrors", fmt(mcpC.total_errors || 0));
      setText(
        "monMcpCallsAvg",
        mcpC.avg_ms ? mcpC.avg_ms.toFixed(1) + "ms" : "—"
      );
      const mcpTb = $("monMcpCallsTable");
      if (mcpTb) {
        const mcpHealth =
          d.mcp && d.mcp.mcp_sf
            ? d.mcp.mcp_sf
            : d.mcp && d.mcp.mcp_platform
              ? d.mcp.mcp_platform
              : {};
        const byTool = mcpHealth.by_tool || mcpC.by_tool || {};
        const toolEntries = Object.entries(byTool);
        if (toolEntries.length > 0) {
          mcpTb.innerHTML = toolEntries
            .map(([tool, info]) => {
              if (typeof info === "object") {
                return `<tr><td style="font-size:0.7rem">${tool}</td><td>${info.calls || 0}</td><td>${info.errors || 0}</td><td>${info.avg_ms ? info.avg_ms.toFixed(0) : "—"}</td></tr>`;
              }
              return `<tr><td style="font-size:0.7rem">${tool}</td><td>${info}</td><td>—</td><td>—</td></tr>`;
            })
            .join("");
        } else {
          mcpTb.innerHTML =
            '<tr><td colspan="4" class="mon-empty">No MCP calls yet</td></tr>';
        }
      }

      const costs = d.llm_costs || {};
      setText("monCostTotal", "$" + (costs.total_usd || 0).toFixed(4));
      const costTb = $("monCostByProvider");
      if (costTb) {
        if (costs.by_provider && Object.keys(costs.by_provider).length > 0) {
          costTb.innerHTML = Object.entries(costs.by_provider)
            .map(
              ([provName, info]) =>
                `<tr><td>${provName}</td><td>${info.calls || 0}</td><td>${fmt((info.tokens_in || 0) + (info.tokens_out || 0))}</td><td>$${(info.cost_usd || 0).toFixed(4)}</td></tr>`
            )
            .join("");
        } else {
          costTb.innerHTML =
            '<tr><td colspan="4" class="mon-empty">No LLM costs yet</td></tr>';
        }
      }

      const rtk = d.rtk || {};
      const rtkRow = $("monRtkRow");
      if (rtkRow && rtk.calls > 0) {
        rtkRow.style.display = "";
        setText("monRtkCalls", fmt(rtk.calls || 0));
        const saved = rtk.bytes_saved || 0;
        setText(
          "monRtkBytesSaved",
          saved >= 1024 ? (saved / 1024).toFixed(1) + "KB" : saved + "B"
        );
        setText("monRtkRatio", (rtk.ratio_pct || 0).toFixed(1) + "%");
        setText("monRtkTokens", fmt(rtk.tokens_saved_est || 0));
      }

      const anon = d.anonymization || {};
      setText("monAnonTotal", fmt(anon.total || 0));
      const anonEl = $("monAnonByType");
      if (anonEl) {
        if (anon.by_type && Object.keys(anon.by_type).length > 0) {
          anonEl.innerHTML = Object.entries(anon.by_type)
            .map(
              ([t, c]) =>
                `<span class="mon-badge purple">${t}: ${c}</span>`
            )
            .join("");
        } else {
          anonEl.innerHTML =
            '<span class="mon-empty">No anonymization data</span>';
        }
      }
      const rlm = d.mcp && d.mcp.rlm_cache;
      const rlmEl = $("monRlmScopes");
      if (rlmEl) {
        if (rlm && rlm.by_scope && Object.keys(rlm.by_scope).length > 0) {
          rlmEl.innerHTML = Object.entries(rlm.by_scope)
            .map(
              ([scope, c]) =>
                `<span class="mon-badge blue">${scope}: ${c}</span>`
            )
            .join("");
        } else {
          rlmEl.innerHTML = `<span class="mon-empty">${rlm ? fmt(rlm.entries || 0) + " cached" : "No RLM cache"}</span>`;
        }
      }

      const inc = d.incidents || {};
      setText("monIncOpen", inc.open || 0);
      setText("monIncTotal", inc.total || 0);
      const incEl = $("monIncBadges");
      if (incEl) {
        if (inc.by_severity_status && inc.by_severity_status.length > 0) {
          const sevColors = {
            P0: "red",
            P1: "red",
            P2: "yellow",
            P3: "blue",
            P4: "purple",
          };
          incEl.innerHTML = inc.by_severity_status
            .map(
              (row) =>
                `<span class="mon-badge ${sevColors[row.severity] || "purple"}">${row.severity} ${row.status}: ${row.cnt}</span>`
            )
            .join("");
        } else {
          incEl.innerHTML =
            '<span class="mon-empty">No incidents <svg class="icon icon-sm" style="vertical-align:middle"><use href="#icon-check-circle"/></svg></span>';
        }
      }

      const az = d.azure || {};
      const vm = az.vm || {};
      setText("monAzVmName", vm.name || "—");
      setText("monAzVmIp", vm.ip || "—");
      setText("monAzVmRegion", vm.region || "—");
      setText("monAzVmSize", vm.size || "—");

      const srvEl = $("monAzServers");
      if (srvEl && az.servers && az.servers.length > 0) {
        srvEl.innerHTML = az.servers
          .map((sv) => {
            const up = sv.status === "up";
            const cls = up
              ? "mon-dot-up"
              : sv.status === "down"
                ? "mon-dot-down"
                : "";
            return `<div class="mon-mcp-item"><span class="mon-dot ${cls}"></span><span class="mon-mcp-name">${sv.name}</span><span class="mon-mcp-detail">:${sv.port}</span></div>`;
          })
          .join("");
      }

      const bk = az.backup || {};
      setText("monAzBackupAcct", bk.storage_account || "—");
      setText("monAzBackupGRS", bk.replication || "—");
      setText("monAzBackupDbs", bk.sqlite_dbs || "—");
      const azContEl = $("monAzContainers");
      if (azContEl && bk.containers && bk.containers.length > 0) {
        azContEl.innerHTML = bk.containers
          .map((c) => `<span class="mon-badge blue">${c}</span>`)
          .join("");
      }
      const azRetEl = $("monAzRetention");
      if (azRetEl && bk.retention) {
        azRetEl.innerHTML = Object.entries(bk.retention)
          .map(
            ([k, val]) =>
              `<span class="mon-badge purple">${k}: ${val}</span>`
          )
          .join("");
      }

      const azc = az.costs || {};
      setText("monAzCostAzure", fmtUsd(azc.azure_llm_usd));
      setText("monAzCostOther", fmtUsd(azc.other_llm_usd));
      setText("monAzCostTotal", fmtUsd(azc.total_llm_usd));
      setText("monAzCostVm", fmtUsd(azc.vm_monthly_usd));
      setText("monAzCostPg", fmtUsd(azc.pg_monthly_usd));
      setText("monAzCostStorage", fmtUsd(azc.storage_monthly_usd));
      setText("monAzCostInfra", fmtUsd(azc.total_infra_monthly_usd));

      const ds = d.docker_system || {};
      setText("monDockerVersion", ds.server_version || "—");
      setText("monDockerRunning", ds.containers_running ?? "—");
      const dockerRunningEl = $("monDockerRunning");
      if (dockerRunningEl) {
        dockerRunningEl.className =
          "val" + (ds.containers_running > 0 ? "" : " mon-val-red");
      }
      setText("monDockerStopped", ds.containers_stopped ?? "—");
      const dockerStoppedEl = $("monDockerStopped");
      if (dockerStoppedEl) {
        dockerStoppedEl.className =
          "val" + (ds.containers_stopped > 0 ? " mon-val-yellow" : "");
      }
      setText("monDockerImages", ds.images ?? "—");
      setText("monDockerVolumes", ds.volumes_count ?? "—");
      setText(
        "monDockerDisk",
        ds.total_disk_gb ? ds.total_disk_gb + " GB" : "—"
      );
      setText(
        "monDockerImgDisk",
        ds.images_size_gb ? ds.images_size_gb + " GB" : "—"
      );
      setText(
        "monDockerCtDisk",
        ds.containers_disk_mb != null ? ds.containers_disk_mb + " MB" : "—"
      );
      setText(
        "monDockerVolDisk",
        ds.volumes_size_gb ? ds.volumes_size_gb + " GB" : "—"
      );
      setText(
        "monDockerCacheDisk",
        ds.build_cache_gb ? ds.build_cache_gb + " GB" : "—"
      );

      const dockerEl = $("monDockerTable");
      if (dockerEl) {
        if (d.docker && d.docker.length > 0) {
          dockerEl.innerHTML = d.docker
            .map((c) => {
              const up = c.state === "running";
              const dot = up
                ? '<span style="color:#22c55e">●</span>'
                : c.state === "exited"
                  ? '<span style="color:#ef4444">●</span>'
                  : '<span style="color:#eab308">●</span>';
              const memPct =
                c.mem_limit_mb > 0
                  ? Math.round((c.mem_mb / c.mem_limit_mb) * 100)
                  : 0;
              const memBar =
                c.mem_limit_mb > 0
                  ? `<div style="background:var(--bg-tertiary,#1a1730);border-radius:3px;height:4px;width:60px;margin-top:2px"><div style="background:${memPct > 80 ? "var(--red,#ef4444)" : memPct > 50 ? "var(--yellow,#eab308)" : "var(--green,#22c55e)"};height:4px;border-radius:3px;width:${Math.min(memPct, 100)}%"></div></div>`
                  : "";
              const cpuColor =
                c.cpu_pct > 80
                  ? "var(--red,#ef4444)"
                  : c.cpu_pct > 40
                    ? "var(--yellow,#eab308)"
                    : "var(--green,#22c55e)";
              return `<tr>
                    <td style="font-size:0.75rem;font-weight:500">${dot} ${c.name}</td>
                    <td style="font-size:0.7rem;opacity:0.8">${c.status}${c.restarts ? ' <span style="color:var(--yellow,#eab308)">(' + c.restarts + " restarts)</span>" : ""}</td>
                    <td style="font-size:0.75rem;font-weight:600;color:${cpuColor}">${up ? c.cpu_pct + "%" : "—"}</td>
                    <td style="font-size:0.7rem">${up ? c.mem_mb + " MB" : "—"}${memBar}</td>
                    <td style="font-size:0.65rem;opacity:0.7">${up ? "↓" + c.net_rx_mb + " / ↑" + c.net_tx_mb + " MB" : "—"}</td>
                    <td style="font-size:0.7rem">${up ? c.pids : "—"}</td>
                    <td style="font-size:0.65rem;opacity:0.6">${c.image}</td>
                </tr>`;
            })
            .join("");
        } else {
          dockerEl.innerHTML =
            '<tr><td colspan="7" class="mon-empty">No Docker info</td></tr>';
        }
      }

      const gitReposEl = $("monGitRepos");
      if (gitReposEl) {
        const repos = Array.isArray(d.git)
          ? d.git
          : d.git && d.git.branch
            ? [d.git]
            : [];
        if (repos.length > 0) {
          gitReposEl.innerHTML = repos
            .map(
              (repo) => `
                <div style="margin-bottom:1rem;padding-bottom:0.8rem;border-bottom:1px solid var(--border)">
                    <div style="display:flex;gap:1rem;margin-bottom:0.4rem;align-items:center">
                        <span style="font-weight:600;font-size:0.82rem;color:var(--text-primary)">${repo.label || repo.path || "?"}</span>
                        <span style="font-size:0.72rem;color:var(--accent);background:var(--accent)22;padding:1px 6px;border-radius:4px">
                            <svg style="width:10px;height:10px;vertical-align:-1px"><use href="#icon-git-branch"/></svg> ${repo.branch || "—"}
                        </span>
                        <span style="font-size:0.68rem;color:var(--text-tertiary)">${repo.last_commit_time ? repo.last_commit_time.substring(0, 16) : "—"}</span>
                    </div>
                    <table class="mon-table" style="margin:0">
                        <tbody>${(repo.recent_commits || [])
                          .map(
                            (c) =>
                              `<tr><td style="font-family:monospace;font-size:0.68rem;color:var(--accent);width:60px">${c.hash}</td><td style="font-size:0.7rem">${c.message}</td></tr>`
                          )
                          .join("")}</tbody>
                    </table>
                </div>
            `
            )
            .join("");
        } else {
          gitReposEl.innerHTML =
            '<div class="mon-empty">No git repos found</div>';
        }
      } else {
        const git = d.git || {};
        setText("monGitBranch", git.branch || "—");
        setText(
          "monGitLastCommit",
          git.last_commit_time ? git.last_commit_time.substring(0, 16) : "—"
        );
        const gitEl = $("monGitCommits");
        if (gitEl) {
          if (git.recent_commits && git.recent_commits.length > 0) {
            gitEl.innerHTML = git.recent_commits
              .map(
                (c) =>
                  `<tr><td style="font-family:monospace;font-size:0.7rem;color:var(--accent)">${c.hash}</td><td style="font-size:0.7rem">${c.message}</td></tr>`
              )
              .join("");
          } else {
            gitEl.innerHTML =
              '<tr><td colspan="2" class="mon-empty">No git data</td></tr>';
          }
        }
      }

      const phaseEl = $("monPhaseStats");
      if (phaseEl) {
        if (d.phase_stats && d.phase_stats.length > 0) {
          const statusColors = {
            completed: "color:var(--green,#22c55e)",
            running: "color:var(--blue,#3b82f6)",
            failed: "color:var(--red,#ef4444)",
            pending: "opacity:0.6",
          };
          phaseEl.innerHTML = d.phase_stats
            .map(
              (p) =>
                `<tr><td style="font-size:0.75rem">${p.phase_name || "—"}</td><td style="${statusColors[p.status] || ""};font-size:0.7rem">${p.status}</td><td>${p.cnt}</td><td>${p.avg_sec ? fmtTime(Math.round(p.avg_sec)) : "—"}</td></tr>`
            )
            .join("");
        } else {
          phaseEl.innerHTML =
            '<tr><td colspan="4" class="mon-empty">No phase data</td></tr>';
        }
      }
    } catch (e) {
      console.warn("Monitoring refresh error:", e);
    }
  }

  function setRange(hours) {
    currentHours = hours;
    document.querySelectorAll(".mon-range-btn").forEach((b) => {
      b.classList.toggle("active", parseInt(b.dataset.hours, 10) === hours);
    });
    refresh();
  }

  function init() {
    if (!$("monRoot")) return;
    if (pollTimer) {
      clearInterval(pollTimer);
      pollTimer = null;
    }
    const defaultBtn = document.querySelector('.mon-range-btn[data-hours="24"]');
    if (defaultBtn) defaultBtn.classList.add("active");
    refresh();
    pollTimer = setInterval(refresh, POLL_INTERVAL_MS);
  }

  window.setRange = setRange;
  window.MonitoringDashboard = {
    POLL_INTERVAL_MS,
    init,
    refresh,
    setRange,
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  document.body.addEventListener("htmx:afterSwap", (event) => {
    const target = event.detail && event.detail.target;
    if (!target) return;
    if (
      target.id === "monRoot" ||
      (target.querySelector && target.querySelector("#monRoot"))
    ) {
      init();
    }
  });
})();
