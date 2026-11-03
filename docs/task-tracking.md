# Task tracking

The personal **Cybersecurity Workspace** GitHub Project is the task board. Its project cards are linked GitHub Issues. Each 70-project card contains the four original step checkboxes, dates, scope and links to the relevant evidence folder.

Status values on the board: Not Started (blue), In Progress (yellow), Completed (green), Delayed (red).

The issue checklist is the record of **which steps were finished**. When a task is checked or unchecked in one of these issues, the `Sync issue checklists to progress data` workflow updates the matching step in `data/progress.json` on the default branch. The separate progress-dashboard workflow then refreshes the 70-project chart. An unchecked task can separately be marked in progress or delayed in the register.

The project board's Status, Steps completed and deadline fields are changed when reported, or can be edited manually. **GitHub Projects status fields and Google Calendar colours do not automatically sync with one another.** The GitHub Projects board is private; public repositories contain the code and technical evidence.

New independent projects should be tracked on the same board but stored in `independent-projects/`, `tools/`, `research/` or `case-studies/`. They do not alter the percentage for the original 70-project track.
