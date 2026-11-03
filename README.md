<div align="center">

![Cybersecurity Projects and Research](assets/portfolio-banner.svg)

**A growing collection of cybersecurity labs, software, tools, research and documented investigations.**

[![Portfolio](https://img.shields.io/badge/PORTFOLIO-CURATED%20WORK-46DDCF?style=for-the-badge&labelColor=102334)](PORTFOLIO.md)
[![Learning Track](https://img.shields.io/badge/LEARNING-STRUCTURED%20PROJECTS-5EBAFA?style=for-the-badge&labelColor=102334)](docs/roadmap.md)
[![Study Log](https://img.shields.io/badge/NOTES-LEARNING%20LOG-ACB2FF?style=for-the-badge&labelColor=102334)](https://github.com/kadencybsec/cyber-learning-log)

</div>

## Overview

This repository is the main public workspace for **Kaden Younis's practical cybersecurity work**. It is designed to grow with new tools, independent projects, security analysis and research, including work created **after** the original 2026–2028 learning roadmap.

Every finished item should explain its purpose, authorised scope, technical approach, test results, evidence and limitations. A folder or checklist alone does not demonstrate a finished project.

## Explore the portfolio

| Section | Purpose | Location |
|:--|:--|:--|
| **Curated work** | Best completed pieces to share with recruiters, with direct evidence | [Portfolio index](PORTFOLIO.md) |
| **Independent projects** | New investigations and builds outside the original roadmap | [Independent projects](independent-projects/) |
| **Tools & automation** | Original scripts, utilities, tests and safe prototypes | [Tools](tools/) |
| **Security research** | Threat modelling, referenced technical findings and defensive research | [Research](research/) |
| **Case studies & reports** | Sanitised findings, remediation plans, lessons learned | [Case studies](case-studies/) |
| **Structured learning track** | The original 70-project programme, with numbered steps | [Roadmap](docs/roadmap.md) |

### Current work

**B06 — Personal cybersecurity lab** is the first scheduled learning sprint, covering safe VM isolation, initial Linux setup, a second test system and recovery snapshots. [Open B06](projects/beginner/B06/README.md).

Finished independent work will be added to the [portfolio index](PORTFOLIO.md), not buried within the training checklist.

## Structured learning programme

The existing training track is a **specific 70-project programme**, not the scope of this entire portfolio.

| Level | IDs | Project folders |
|:--|:--|:--|
| Beginner | B01–B25 | [Browse](projects/beginner/) |
| Intermediate | I26–I50 | [Browse](projects/intermediate/) |
| Advanced | A51–A70 | [Browse](projects/advanced/) |

![Recorded progress of the original 70-project programme](assets/progress-dashboard.svg)

This visual shows **only** progress in the original numbered curriculum. It is computed from [data/progress.json](data/progress.json), which starts with no completed projects. Unrelated future work has its own index and will not distort this percentage.

## How to add new work

1. Choose a location: `independent-projects/`, `tools/`, `research/`, or `case-studies/`.
2. Create a descriptive folder and start with the [independent project template](docs/independent-project-template.md).
3. Record requirements and scope, build or investigate, test, then write your own conclusions.
4. Keep sample data harmless and screenshots redacted. Describe failures and limitations.
5. Once genuinely completed, add the item to [PORTFOLIO.md](PORTFOLIO.md) with links to its evidence. Unfinished work stays in the work-in-progress section.

See [publishing workflow](docs/publishing-workflow.md) and [evidence standard](docs/evidence-standard.md).

## What matters here

- **Reproducibility:** document setup, versions, assumptions and expected results.
- **Clarity:** explain why commands and technical decisions work.
- **Security:** use owned/authorised labs and synthetic data; never commit secrets or personal data.
- **Honesty:** distinguish a plan, a prototype, a tested result and a production-ready tool.
- **Iteration:** preserve what changed and what was learned.

**Related:** [GitHub profile](https://github.com/kadencybsec) · [Cyber learning log](https://github.com/kadencybsec/cyber-learning-log) · [Security policy](SECURITY.md)
