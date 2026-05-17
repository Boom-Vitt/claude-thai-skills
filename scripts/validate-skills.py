#!/usr/bin/env python3
"""validate-skills.py -- lint every SKILL.md in this repo.

Each skill is a directory under ``skills/`` that contains a ``SKILL.md`` file.
The file must open with a YAML-style frontmatter block delimited by ``---``
lines and must declare at least the two fields Claude Code reads at load
time: ``name`` and ``description``.

This validator deliberately does not pull in PyYAML so the script runs on any
machine with a stock Python 3 install. The frontmatter we care about is a
flat list of ``key: value`` pairs, so a hand-written parser is enough.

Checks performed for each skill directory:

* A ``SKILL.md`` file exists at the expected path.
* The file begins with a ``---`` line and contains a closing ``---``.
* The frontmatter contains a ``name`` field whose value matches the directory
  name. A mismatch is a real bug: Claude Code looks up skills by directory
  name and a mismatched ``name`` confuses tools that index the marketplace.
* The frontmatter contains a non-empty ``description`` field. Skills with an
  empty description are effectively un-discoverable.
* The body below the frontmatter contains at least one Markdown heading. An
  empty body usually means the skill was scaffolded but never written.
* Every skill listed in ``.claude-plugin/plugin.json`` exists on disk and
  every skill directory on disk is listed in ``plugin.json``. Drift between
  the two surfaces is the single most common cause of "skill not loading"
  reports.

Exit codes:
  0  every skill validated cleanly
  1  one or more skills had at least one error (errors are printed inline)

Usage:
  python3 scripts/validate-skills.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
PLUGIN_JSON = REPO_ROOT / ".claude-plugin" / "plugin.json"


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return ``(frontmatter_dict, body)`` parsed from a Markdown file.

    Raises ValueError if the document does not start with a ``---`` fence or
    if the fence is never closed. The parser intentionally only handles flat
    ``key: value`` lines; nested YAML structures are not used by skill files.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("file does not start with a '---' frontmatter fence")

    closing_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        raise ValueError("frontmatter fence opened with '---' but never closed")

    fields: dict[str, str] = {}
    for raw in lines[1:closing_index]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise ValueError(f"frontmatter line is not 'key: value': {raw!r}")
        key, value = raw.split(":", 1)
        fields[key.strip()] = value.strip()

    body = "\n".join(lines[closing_index + 1 :])
    return fields, body


def body_has_heading(body: str) -> bool:
    for line in body.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#"):
            return True
    return False


def validate_one(skill_dir: Path) -> list[str]:
    """Return a list of human-readable error strings for one skill directory."""
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        return [f"missing SKILL.md at {skill_file.relative_to(REPO_ROOT)}"]

    try:
        text = skill_file.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"SKILL.md is not valid UTF-8: {exc}"]

    try:
        fields, body = parse_frontmatter(text)
    except ValueError as exc:
        return [f"frontmatter parse error: {exc}"]

    name = fields.get("name", "")
    if not name:
        errors.append("frontmatter is missing a 'name' field")
    elif name != skill_dir.name:
        errors.append(
            f"frontmatter name '{name}' does not match directory name "
            f"'{skill_dir.name}'"
        )

    description = fields.get("description", "")
    if not description:
        errors.append("frontmatter is missing a non-empty 'description' field")

    if not body_has_heading(body):
        errors.append("body has no Markdown heading after the frontmatter")

    return errors


def listed_in_manifest() -> list[str]:
    """Return the skill directory names declared in ``.claude-plugin/plugin.json``."""
    if not PLUGIN_JSON.exists():
        return []
    try:
        data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{PLUGIN_JSON} is not valid JSON: {exc}") from exc
    paths = data.get("skills", [])
    names: list[str] = []
    for path in paths:
        # The manifest stores paths like "skills/thai-invoice"; we only want
        # the leaf name so we can compare it against the directories on disk.
        names.append(Path(path).name)
    return names


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"FAIL: skills directory not found at {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_dirs = sorted([d for d in SKILLS_DIR.iterdir() if d.is_dir()])
    if not skill_dirs:
        print(f"FAIL: no skill directories found under {SKILLS_DIR}", file=sys.stderr)
        return 1

    total_errors = 0
    for skill_dir in skill_dirs:
        errors = validate_one(skill_dir)
        if errors:
            total_errors += len(errors)
            print(f"[FAIL] {skill_dir.name}")
            for err in errors:
                print(f"       - {err}")
        else:
            print(f"[PASS] {skill_dir.name}")

    # Drift check between plugin.json and the skills directory. We treat this
    # as a single conceptual check at the end so the per-skill output above
    # stays focused on the skill's own files.
    try:
        manifest_names = listed_in_manifest()
    except ValueError as exc:
        print(f"[FAIL] plugin.json: {exc}")
        total_errors += 1
        manifest_names = []

    on_disk = {d.name for d in skill_dirs}
    declared = set(manifest_names)

    missing_from_manifest = sorted(on_disk - declared)
    missing_from_disk = sorted(declared - on_disk)

    if missing_from_manifest or missing_from_disk:
        print("[FAIL] plugin.json drift")
        for name in missing_from_manifest:
            print(f"       - on disk but not declared in plugin.json: {name}")
            total_errors += 1
        for name in missing_from_disk:
            print(f"       - declared in plugin.json but not on disk: {name}")
            total_errors += 1
    else:
        print("[PASS] plugin.json matches skills/ directory")

    print()
    if total_errors:
        print(f"FAILED: {total_errors} error(s) across {len(skill_dirs)} skill(s)")
        return 1
    print(f"All {len(skill_dirs)} skill(s) validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
