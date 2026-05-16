#!/usr/bin/env bash
#
# test-all.sh — run every self-test that ships with this repo.
#
# This is the single command that contributors and CI both invoke. If you
# add a new skill with executable tests, register the test file at the
# bottom of this script so it runs alongside the others. The goal is that
# `./scripts/test-all.sh` always either prints "All test files passed." and
# exits zero, or names exactly which test file failed and exits non-zero.
#
# Usage:
#   ./scripts/test-all.sh             # run everything
#   ./scripts/test-all.sh --py        # run only Python tests
#   ./scripts/test-all.sh --ts        # run only TypeScript tests
#   ./scripts/test-all.sh --validate  # run only the SKILL.md validator
#
# Exit codes:
#   0  every registered test passed
#   1  at least one test failed (the failing files are listed at the end)
#   2  a required tool (python3, npx) is missing
#
# Environment:
#   PYTHON  override the Python interpreter (defaults to python3)
#   NPX     override the npx command (defaults to npx)
#
set -uo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

PYTHON="${PYTHON:-python3}"
NPX="${NPX:-npx}"

want_py=1
want_ts=1
want_validate=1

if [ "$#" -gt 0 ]; then
  want_py=0
  want_ts=0
  want_validate=0
  for arg in "$@"; do
    case "$arg" in
      --py)        want_py=1 ;;
      --ts)        want_ts=1 ;;
      --validate)  want_validate=1 ;;
      -h|--help)
        sed -n '3,22p' "$0"
        exit 0
        ;;
      *)
        echo "unknown argument: $arg" >&2
        echo "see --help for usage" >&2
        exit 2
        ;;
    esac
  done
fi

# Sanity-check that the interpreters we need are actually on PATH so that a
# missing tool fails fast with a clear error rather than mid-test.
if [ "$want_py" -eq 1 ] && ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "missing interpreter: $PYTHON not found on PATH" >&2
  echo "set the PYTHON environment variable to override (e.g. PYTHON=python3.12)" >&2
  exit 2
fi
if [ "$want_ts" -eq 1 ] && ! command -v "$NPX" >/dev/null 2>&1; then
  echo "missing tool: $NPX not found on PATH" >&2
  echo "install Node.js (which ships with npx) to run the TypeScript tests" >&2
  exit 2
fi

passed=()
failed=()

run_case() {
  local label="$1"
  shift
  printf '\n----- %s -----\n' "$label"
  if "$@"; then
    passed+=("$label")
  else
    failed+=("$label")
  fi
}

if [ "$want_validate" -eq 1 ]; then
  run_case "validate SKILL.md frontmatter" "$PYTHON" scripts/validate-skills.py
fi

if [ "$want_py" -eq 1 ]; then
  run_case "thai-id-validate/validate.py" "$PYTHON" skills/thai-id-validate/validate.py
  run_case "thai-date-format/convert.py"  "$PYTHON" skills/thai-date-format/convert.py
  run_case "thai-invoice/calc.py"         "$PYTHON" skills/thai-invoice/calc.py
  run_case "thai-address/parse.py"        "$PYTHON" skills/thai-address/parse.py
fi

if [ "$want_ts" -eq 1 ]; then
  # We invoke tsx via npx --yes so contributors do not have to install
  # anything before running the suite. CI does the same to keep parity.
  run_case "thai-id-validate/validate.ts" "$NPX" --yes tsx skills/thai-id-validate/validate.ts
  run_case "thai-date-format/convert.ts"  "$NPX" --yes tsx skills/thai-date-format/convert.ts
  run_case "thai-address/parse.ts"        "$NPX" --yes tsx skills/thai-address/parse.ts
fi

printf '\n===== summary =====\n'
printf 'passed: %d\n' "${#passed[@]}"
printf 'failed: %d\n' "${#failed[@]}"

if [ "${#failed[@]}" -gt 0 ]; then
  printf '\nfailing test files:\n'
  for f in "${failed[@]}"; do
    printf '  - %s\n' "$f"
  done
  exit 1
fi

printf '\nAll test files passed.\n'
