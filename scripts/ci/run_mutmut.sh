#!/usr/bin/env bash
# Run mutmut 2.x on a single target and enforce score via mutation_gate.sh.
# mutmut 3 --max-children is deferred (stats linking broken with platform/ package name).
set -euo pipefail

TARGET="${1:?usage: run_mutmut.sh adversarial|api_key}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "${ROOT}"

export PLATFORM_ENV="${PLATFORM_ENV:-test}"
export PLATFORM_LLM_PROVIDER="${PLATFORM_LLM_PROVIDER:-demo}"

PYTEST_BASE=(
  env PYTHONPATH="${ROOT}"
  PLATFORM_ENV="${PLATFORM_ENV}"
  PLATFORM_LLM_PROVIDER="${PLATFORM_LLM_PROVIDER}"
  python3 -m pytest
)

case "${TARGET}" in
  adversarial)
    MUTATE_PATH="platform/agents/adversarial.py"
    MIN_SCORE="${MUTATION_MIN_ADVERSARIAL:-15}"
    RUNNER=("${PYTEST_BASE[@]}" tests/test_adversarial_l0.py tests/test_adversarial_l2.py -q)
    ;;
  api_key)
    if [[ ! -f platform/auth/api_key.py ]]; then
      echo "Skip: platform/auth/api_key.py not found"
      exit 0
    fi
    MUTATE_PATH="platform/auth/api_key.py"
    MIN_SCORE="${MUTATION_MIN_API_KEY:-10}"
    RUNNER=("${PYTEST_BASE[@]}" \
      tests/test_api_key_alias.py::test_get_platform_api_key_prefers_architekt \
      tests/test_api_key_alias.py::test_get_platform_api_key_falls_back_to_macaron \
      -q)
    ;;
  *)
    echo "Unknown target: ${TARGET}"
    exit 2
    ;;
esac

rm -rf .mutmut-cache mutants 2>/dev/null || true

RUNNER_STR=""
for part in "${RUNNER[@]}"; do
  RUNNER_STR+=" $(printf '%q' "${part}")"
done

# timeout 900s; --max-children=2 applies to mutmut 3+ (see ADR-003)
set +e
env -u PYTHONPATH timeout 900 python3 -m mutmut run \
  --paths-to-mutate="${MUTATE_PATH}" \
  --no-progress \
  --runner="${RUNNER_STR# }"
MUT_EXIT=$?
set -e

env -u PYTHONPATH python3 -m mutmut results 2>&1 | tail -40 || true

bash scripts/ci/mutation_gate.sh "${MIN_SCORE}" "${TARGET}"
