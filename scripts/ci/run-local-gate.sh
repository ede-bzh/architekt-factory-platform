#!/usr/bin/env bash
# Mirror GitHub Actions CI test job locally (run from repo root).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

echo "==> ruff"
ruff check platform/ tests/

echo "==> bandit"
PYTHONPATH= python3 -m bandit -r platform/ -lll -q -c bandit.yaml

echo "==> secret-scan"
bash scripts/ci/secret-scan.sh

echo "==> pip-audit"
if ! PYTHONPATH= python3 -m pip_audit --version >/dev/null 2>&1; then
  PYTHONPATH= python3 -m pip install -q pip-audit
fi
PYTHONPATH= python3 -m pip_audit -r "$ROOT/platform/requirements.txt" --desc on

echo "==> pytest (CI gate)"
export PYTHONPATH=.
export PLATFORM_LLM_PROVIDER=demo
export PLATFORM_ENV=test
python3 -m pytest \
  tests/test_demo.py \
  tests/test_events.py \
  tests/test_deterministic_tools.py \
  tests/test_adaptive_intelligence.py \
  tests/test_adversarial_l0.py \
  tests/test_plugins.py \
  tests/test_llm_cache.py \
  tests/test_platform_api.py \
  tests/test_health_api.py \
  tests/test_rate_limit.py \
  tests/test_uruk_rtk.py \
  tests/test_workers.py \
  tests/test_b_features.py \
  tests/test_api_key_alias.py \
  tests/test_llm_budget.py \
  tests/test_quality_pdf.py \
  tests/test_adversarial_l2.py \
  tests/test_adversarial_l2_llm.py \
  tests/test_finops_margin.py \
  tests/test_prometheus_architekt.py \
  tests/test_ai_audit_logs.py \
  tests/test_case_study.py \
  tests/test_architekt_delivery_audit.py \
  tests/test_architekt_branding.py \
  tests/test_i18n_en_fr.py \
  tests/test_no_legacy_external_refs.py \
  tests/test_readme_en_fr.py \
  tests/test_monitoring_live_perf.py \
  tests/test_wave_e_runtime.py \
  tests/test_doc_no_architekt_user_facing.py \
  -q

echo "==> OK"
