#!/usr/bin/env python3
"""Validate the real project register and render an evidence-based SVG dashboard."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "progress.json"
OUT = ROOT / "assets" / "progress-dashboard.svg"
ALLOWED = {"not_started", "in_progress", "completed", "delayed"}
TIERS = [("B", "BEGINNER", 25), ("I", "INTERMEDIATE", 25), ("A", "ADVANCED", 20)]

def load():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    projects = data.get("projects", [])
    assert len(projects) == 70, "Expected exactly 70 projects"
    ids = [p["id"] for p in projects]
    assert len(set(ids)) == 70, "Duplicate project IDs"
    all_steps = []
    for p in projects:
        steps = p.get("steps", [])
        assert len(steps) == 4, f"{p['id']} must have four steps"
        assert all(s.get("status") in ALLOWED for s in steps), f"Bad status in {p['id']}"
        assert all(s.get("id") == f"{p['id']}-S{i}" for i, s in enumerate(steps, 1)), f"Step ID mismatch in {p['id']}"
        all_steps.extend(steps)
    assert len(all_steps) == 280, "Expected 280 steps"
    assert sorted([x for x in ids if x.startswith("B")]) == [f"B{i:02d}" for i in range(1,26)]
    assert sorted([x for x in ids if x.startswith("I")]) == [f"I{i:02d}" for i in range(26,51)]
    assert sorted([x for x in ids if x.startswith("A")]) == [f"A{i:02d}" for i in range(51,71)]
    return projects, all_steps

def status(p):
    s = [x["status"] for x in p["steps"]]
    if all(x == "completed" for x in s):
        return "completed"
    if "delayed" in s:
        return "delayed"
    if any(x in ("in_progress", "completed") for x in s):
        return "in_progress"
    return "not_started"

def render(projects, all_steps):
    done = sum(status(p) == "completed" for p in projects)
    active = sum(status(p) == "in_progress" for p in projects)
    delayed = sum(status(p) == "delayed" for p in projects)
    step_done = sum(x["status"] == "completed" for x in all_steps)
    percentage = round(done * 100 / 70)
    blocks = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="420" viewBox="0 0 1200 420" role="img" aria-label="Cybersecurity 70-project evidence-based progress">',
        '<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#06111F"/><stop offset="1" stop-color="#0B2031"/></linearGradient><linearGradient id="bar" x2="1"><stop stop-color="#00DFD8"/><stop offset="1" stop-color="#42B8FF"/></linearGradient></defs>',
        '<rect width="1200" height="420" rx="24" fill="url(#bg)"/>',
        '<path d="M30 70H1170M30 295H1170" stroke="#1B3950" stroke-width="2"/>',
        '<g fill="#123146" opacity=".38">'
    ]
    for x in range(30, 1190, 30):
        blocks.append(f'<path d="M{x} 0V420" stroke="#123146" stroke-width=".5"/>')
    blocks.extend([
        '</g><text x="45" y="45" fill="#38E6DF" font-size="16" font-family="monospace" letter-spacing="3">KADEN // CYBERSECURITY FIELD NOTES</text>',
        '<text x="1150" y="45" fill="#8DAAB8" text-anchor="end" font-size="15" font-family="monospace">LIVE FROM VERIFIED STEP DATA</text>',
        '<text x="48" y="120" fill="#B4C6D0" font-size="19" font-family="Arial,sans-serif">PROJECTS COMPLETED</text>',
        f'<text x="45" y="230" fill="#F4FCFF" font-family="monospace" font-weight="bold" font-size="93">{done}<tspan font-size="35" fill="#77A4B6"> / 70</tspan></text>',
        f'<text x="48" y="270" fill="#55D8FF" font-size="17" font-family="monospace">{percentage}% OF PROJECTS COMPLETED</text>',
        '<text x="520" y="120" fill="#B4C6D0" font-size="19">STEP COMPLETION</text>',
        f'<text x="520" y="190" fill="#F4FCFF" font-size="56" font-family="monospace">{step_done}<tspan fill="#77A4B6" font-size="27"> / 280 STEPS</tspan></text>',
        '<rect x="520" y="210" width="620" height="20" rx="10" fill="#1D3B4D"/>',
        f'<rect x="520" y="210" width="{max(0,round(620 * step_done/280))}" height="20" rx="10" fill="url(#bar)"/>',
        f'<text x="520" y="270" fill="#8EAFC0" font-family="monospace" font-size="18">IN PROGRESS {active:02d}   ·   DELAYED {delayed:02d}   ·   PLANNED {70 - done - active - delayed:02d}</text>',
        '<text x="45" y="332" fill="#8EAFC0" font-family="monospace" font-size="15">TRACK PROGRESSION</text>'
    ])
    xs = [45, 435, 825]
    for (prefix,label,total), x in zip(TIERS, xs):
        amount = sum(p["id"].startswith(prefix) and status(p) == "completed" for p in projects)
        blocks += [
            f'<text x="{x}" y="368" font-size="17" font-family="monospace" fill="#E4F7FA">{escape(label)}</text>',
            f'<text x="{x+340}" y="368" text-anchor="end" font-size="17" font-family="monospace" fill="#55D8FF">{amount}/{total}</text>',
            f'<rect x="{x}" y="382" width="340" height="12" rx="6" fill="#224057"/>',
            f'<rect x="{x}" y="382" width="{round(340*amount/total)}" height="12" rx="6" fill="#39DBD1"/>'
        ]
    blocks.append('</svg>')
    return "\n".join(blocks) + "\n"

if __name__ == "__main__":
    projects, steps = load()
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(render(projects, steps), encoding="utf-8")
    print(f"Validated {len(projects)} projects, {len(steps)} steps; dashboard refreshed")
