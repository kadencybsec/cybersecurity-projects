#!/usr/bin/env python3
"""Sync checked project-issue tasks into the 70-project progress register.

An issue checkbox is evidence that the corresponding task was reported done;
no completion is inferred from schedules, issue creation or issue closure.
"""
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "data" / "progress.json"
STEP_RE = re.compile(
    r"^\s*-\s*\[([ xX])\]\s*\*\*([BIA]\d{2}-S[1-4]):?\*\*",
    flags=re.MULTILINE,
)
TITLE_RE = re.compile(r"^([BIA]\d{2})\b")


def extract_steps(issue):
    title = issue.get("title") or ""
    match = TITLE_RE.match(title)
    if match is None:
        return None, {}
    project_id = match.group(1)
    checks = {}
    for checked, step in STEP_RE.findall(issue.get("body") or ""):
        if step.startswith(project_id + "-") and step not in checks:
            checks[step] = bool(checked.strip())
    return project_id, checks


def synchronize(registry, issue):
    project_id, checks = extract_steps(issue)
    if not project_id or len(checks) != 4:
        return False
    project = next(
        (item for item in registry.get("projects", []) if item.get("id") == project_id),
        None,
    )
    if project is None:
        return False
    current = {s["id"] for s in project["steps"]}
    if set(checks) != current:
        return False
    changed = False
    for step in project["steps"]:
        original = step["status"]
        if checks[step["id"]]:
            updated = "completed"
        elif original == "completed":
            updated = "not_started"
        else:
            # Preserve explicit "in_progress" or "delayed" statuses for
            # unchecked tasks. They can be set when reporting progress.
            updated = original
        if updated != original:
            step["status"] = updated
            changed = True
    if changed:
        registry["last_reviewed"] = datetime.now(timezone.utc).date().isoformat()
    return changed


def main():
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        print("No issue event supplied; nothing to sync")
        return
    event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    issue = event.get("issue") or {}
    data = json.loads(REGISTER.read_text(encoding="utf-8"))
    if synchronize(data, issue):
        REGISTER.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"Updated documented steps from issue: {issue.get('title')}")
    else:
        print("No completed-step changes in a recognised project issue")


if __name__ == "__main__":
    main()
