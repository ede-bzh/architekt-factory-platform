#!/usr/bin/env bash
# CI wrapper: scan platform/, cli/, tests/ for committed secrets.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

if ! python3 -m detect_secrets scan --help >/dev/null 2>&1; then
  pip install detect-secrets
fi

python3 -m detect_secrets scan \
  --all-files \
  --exclude-files '\.git/.*' \
  platform/ cli/ tests/
