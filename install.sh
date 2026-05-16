#!/usr/bin/env bash
# ติดตั้ง Thai skills ทั้งหมดให้ Claude Code
# Install all Thai skills into your Claude Code user skills directory.
#
# Usage:
#   ./install.sh              # ติดตั้งทุก skill / install everything
#   ./install.sh thai-resume  # ติดตั้งเฉพาะตัวที่ระบุ / install one
set -euo pipefail

DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills"

if [ ! -d "$SRC" ]; then
  echo "ไม่พบโฟลเดอร์ skills/ (skills/ folder not found at $SRC)" >&2
  exit 1
fi

mkdir -p "$DEST"

install_one() {
  local name="$1"
  local from="$SRC/$name"
  local to="$DEST/$name"
  if [ ! -d "$from" ]; then
    echo "ข้าม $name (ไม่พบ / not found)"
    return
  fi
  rm -rf "$to"
  cp -R "$from" "$to"
  echo "✓ ติดตั้ง $name"
}

if [ "$#" -eq 0 ]; then
  for d in "$SRC"/*/; do
    install_one "$(basename "$d")"
  done
else
  for name in "$@"; do
    install_one "$name"
  done
fi

echo ""
echo "เสร็จเรียบร้อย! Skills ติดตั้งไว้ที่ $DEST"
echo "Done. Restart Claude Code (or start a new session) to load the skills."
