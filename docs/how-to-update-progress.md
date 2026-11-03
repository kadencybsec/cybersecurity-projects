# Updating project progress

Open [data/progress.json](../data/progress.json). Find a project by its stable ID (for example `B06`), then its step (for example `B06-S1`).

Set **only the real step status** to one of `not_started`, `in_progress`, `completed`, or `delayed`. Add evidence URLs only after the corresponding evidence exists. Do not add credit for calendar time or README creation.

Example when a real step is finished:

```json
{ "id": "B06-S1", "status": "completed", "evidence": ["projects/beginner/B06/evidence/lab-plan.md"] }
```

Save the file, commit it, and the GitHub Action will rebuild `assets/progress-dashboard.svg`. Overall project completion is computed when **all four** of its steps are completed. A partial project appears in progress; delays are reported separately. If a lab takes longer than the planned week, record the blocker and adjust the calendar, not the evidence.
