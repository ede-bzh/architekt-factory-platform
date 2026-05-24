"""Mission case study — markdown export for client proof."""

from __future__ import annotations

import json
from datetime import datetime, timezone

from ..db.migrations import get_db
from ..llm.observability import get_tracer
from ..metrics.finops_summary import compute_margin, mission_revenue_usd


def generate_case_study_markdown(mission_id: str) -> str:
    """Build a markdown case study from mission + run + LLM traces."""
    db = get_db()
    try:
        mission = db.execute(
            "SELECT id, name, status, config_json, created_at FROM missions WHERE id = ?",
            (mission_id,),
        ).fetchone()
        if not mission:
            return f"# Case study\n\nMission `{mission_id}` introuvable.\n"

        run = db.execute(
            """
            SELECT id, status, brief, phases_json, created_at, completed_at
            FROM mission_runs
            WHERE id = ? OR session_id = ?
            ORDER BY created_at DESC LIMIT 1
        """,
            (mission_id, mission_id),
        ).fetchone()

        cost_row = db.execute(
            """
            SELECT COUNT(*) AS calls,
                   COALESCE(SUM(cost_usd), 0) AS cost_usd,
                   COALESCE(SUM(tokens_in + tokens_out), 0) AS tokens
            FROM llm_traces WHERE mission_id = ?
        """,
            (mission_id,),
        ).fetchone()

        features = db.execute(
            "SELECT status, COUNT(*) AS cnt FROM features WHERE epic_id = ? GROUP BY status",
            (mission_id,),
        ).fetchall()
    finally:
        db.close()

    name = mission["name"] or mission_id
    cost = float(cost_row["cost_usd"] or 0) if cost_row else 0.0
    calls = int(cost_row["calls"] or 0) if cost_row else 0
    tokens = int(cost_row["tokens"] or 0) if cost_row else 0
    rev = mission_revenue_usd(mission_id)
    margin = compute_margin(cost, rev)

    lines = [
        f"# Case study — {name}",
        "",
        f"_Généré le {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_",
        "",
        "## Résumé",
        "",
        f"- **Mission** : `{mission_id}`",
        f"- **Statut** : {dict(mission).get("status", '—')}",
    ]
    if run:
        lines.extend(
            [
                f"- **Dernière exécution** : {run['status']} (`{run['id']}`)",
                f"- **Brief** : {(run['brief'] or '')[:300]}",
            ]
        )

    lines.extend(
        [
            "",
            "## FinOps",
            "",
            "| Métrique | Valeur |",
            "|----------|--------|",
            f"| Appels LLM | {calls} |",
            f"| Tokens | {tokens:,} |",
            f"| Coût LLM (USD) | ${cost:.4f} |",
            f"| Revenu estimé (USD) | ${margin['revenue_usd']:,.2f} |",
            f"| Marge (%) | {margin['margin_pct']}% |",
            "",
        ]
    )

    if features:
        lines.append("## Backlog produit")
        lines.append("")
        for f in features:
            lines.append(f"- **{f['status']}** : {f['cnt']} features")
        lines.append("")

    if run and run.get("phases_json"):
        try:
            phases = json.loads(run["phases_json"])
            if phases:
                lines.append("## Phases")
                lines.append("")
                for p in phases[:15]:
                    pname = p.get("phase_name") or p.get("name", "?")
                    pstatus = p.get("status", "?")
                    lines.append(f"- {pname}: **{pstatus}**")
                lines.append("")
        except Exception:
            pass

    try:
        stats = get_tracer().stats(hours=720)
        if stats.get("by_provider"):
            lines.append("## Providers LLM (30j)")
            lines.append("")
            for p in stats["by_provider"][:5]:
                lines.append(
                    f"- {p.get('provider')}/{p.get('model')}: "
                    f"{p.get('calls')} appels, ${float(p.get('cost_usd', 0)):.4f}"
                )
            lines.append("")
    except Exception:
        pass

    lines.append("---")
    lines.append("*Architekt Factory — export automatique*")
    lines.append("")
    return "\n".join(lines)
