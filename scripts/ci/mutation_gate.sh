#!/usr/bin/env bash
# Parse mutmut 2.x SQLite cache and fail if mutation score is below threshold.
# Score = killed / (killed + survived); untested/skipped are excluded.
set -euo pipefail

MIN_SCORE="${1:-15}"
LABEL="${2:-mutation}"
CACHE="${MUTMUT_CACHE:-.mutmut-cache}"

if [[ ! -f "${CACHE}" ]]; then
  echo "${LABEL}: no .mutmut-cache (run mutmut first)"
  exit 1
fi

read -r KILLED SURVIVED <<EOF
$(python3 - <<PY
import sqlite3
import sys

cache = "${CACHE}"
try:
    conn = sqlite3.connect(cache)
except sqlite3.Error as exc:
    print(f"0 0", file=sys.stderr)
    print(f"sqlite error: {exc}", file=sys.stderr)
    sys.exit(0)
cur = conn.cursor()
try:
    killed = cur.execute(
        "SELECT COUNT(*) FROM Mutant WHERE status='ok_killed'"
    ).fetchone()[0]
    survived = cur.execute(
        "SELECT COUNT(*) FROM Mutant WHERE status='bad_survived'"
    ).fetchone()[0]
except sqlite3.OperationalError:
    killed, survived = 0, 0
print(f"{killed} {survived}")
PY
)
EOF

TOTAL=$((KILLED + SURVIVED))
if [[ "${TOTAL}" -eq 0 ]]; then
  echo "${LABEL}: no scored mutants (killed=0, survived=0)"
  exit 1
fi

SCORE=$((KILLED * 100 / TOTAL))
echo "${LABEL}: mutation score ${SCORE}% (${KILLED}/${TOTAL} killed; min ${MIN_SCORE}%)"

if [[ "${SCORE}" -lt "${MIN_SCORE}" ]]; then
  echo "${LABEL}: FAIL — below threshold ${MIN_SCORE}%"
  exit 1
fi

echo "${LABEL}: PASS"
