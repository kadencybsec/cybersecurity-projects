# CYBERSECURITY / 70 PROJECT FIELD LAB
> **Kaden Younis · 2026–2028 · Learning in public · Evidence over badges**

![Live progress dashboard](assets/progress-dashboard.svg)

## Mission
Build foundational security skills through **70 small, documented, authorised learning sprints**, four steps per project. Work toward a UK cybersecurity apprenticeship after sixth form.

**At launch:** 70 projects defined · 280 steps scheduled · no claims of completion. Progress is calculated only from the [source-of-truth register](data/progress.json).

## Working system
1. Open the project scheduled in the [master roadmap](docs/roadmap.md).
2. Read its `README.md`, complete the current step in your own isolated lab or training environment.
3. Commit only original, sanitised code, diagrams, synthetic sample data and learning notes.
4. Update the matching step's `status` and `evidence` in [data/progress.json](data/progress.json).
5. GitHub Actions validates the register and redraws the dashboard. A project counts as complete **only when all four steps are completed**.

Status values: `not_started` · `in_progress` · `completed` · `delayed`.

### Starting point: B06 — Home cybersecurity lab
[Open B06's four-step checklist](projects/beginner/B06/README.md) · 9–14 November 2026

## Programme map
| Tier | IDs | Number | Folder |
|:--|:--|--:|:--|
| Foundations / beginner | B01–B25 | 25 | [Beginner](projects/beginner/) |
| Intermediate / applied | I26–I50 | 25 | [Intermediate](projects/intermediate/) |
| Advanced / research | A51–A70 | 20 | [Advanced](projects/advanced/) |

## What this portfolio will demonstrate
- **Systems:** Linux, virtual machines, networks, permissions, firewalls
- **Security analysis:** log review, detection, forensics, threat modelling
- **Building tools:** Python, secure web applications, safe local prototypes
- **Communication:** clear reports, reproducible steps, limitations, remediation
- **Professional practice:** authorised scope, redacted evidence and honest attribution

### Learning outside projects
[Weekly learning log](https://github.com/kadencybsec/cyber-learning-log) · [GitHub profile](https://github.com/kadencybsec)

## Trust and evidence
This repository intentionally starts with no completed work. Some planned projects cover malware, password attacks or service disruption; their educational scope is **isolated, synthetic, defensive or research-based**. No live unauthorised testing, malware samples, credentials, or vulnerable public targets.

Use [the evidence standard](docs/evidence-standard.md) and [security policy](SECURITY.md). The Word action plan is the schedule's source for originally assigned tasks.
