#!/bin/bash
# Architekt Platform Backup — Wrapper
# Cron daily 3AM: 0 3 * * * /opt/architekt/platform/ops/run_backup.sh >> /var/log/architekt-backup.log 2>&1
# Cron weekly:    0 2 * * 0 /opt/architekt/platform/ops/run_backup.sh --tier weekly >> /var/log/architekt-backup.log 2>&1
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd /tmp
PYTHONUNBUFFERED=1 exec python3 "$SCRIPT_DIR/run_backup.py" "$@"
