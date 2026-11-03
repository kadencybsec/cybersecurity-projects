# B06-S4: VM snapshots, recovery test and lab inventory

**Status:** Planned. Do not mark complete until snapshots have been created and restored successfully.

## Goal

Save recovery points for the two ARM64 Ubuntu VMs, restore a controlled change in at least one VM, and document the final lab.

## VM inventory (observed or reported)

| Property | Ubuntu Desktop | Ubuntu Server |
|:--|:--|:--|
| Purpose | Linux learning VM | Lightweight test VM |
| OS | Ubuntu 26.04.1 LTS ARM64 | Ubuntu Server 26.04.1 LTS ARM64 |
| Memory | 6 GB | 3 GB (configured; recheck if changed) |
| CPU | 2 cores | 2 cores |
| Disk | 50 GB growable virtual NVMe | 25 GB growable virtual NVMe |
| Private IPv4 observed | 172.16.104.128/24 | 172.16.104.130/24 |
| VMware network | Private to my Mac, host-only | Private to my Mac, host-only |

These observed IP addresses may change on a future reboot. Snapshot restore also reverts guest networking changes since the snapshot.

## Phase A — Baseline snapshots

1. Shut down each Linux VM cleanly with `sudo poweroff`.
2. In VMware Fusion, select the first VM and use **Virtual Machine → Snapshots → Take Snapshot**.
3. Name it `B06-clean-hostonly-desktop` and add a description.
4. Repeat for the server with `B06-clean-hostonly-server`.
5. Verify both snapshots appear in their respective snapshot managers.
6. Record a screenshot of each snapshot manager and its names.

**Important:** Snapshot restore discards VM changes made since the snapshot. Keep originals you care about separately. Snapshots are not independent backups.

## Phase B — Test a harmless rollback

Use only the Ubuntu Desktop VM for the first recovery test.

1. Start the Desktop VM.
2. Create a harmless marker file in the home folder:

   ```bash
   printf 'B06 snapshot restore test\n' > ~/b06-snapshot-test.txt
   cat ~/b06-snapshot-test.txt
   ```

3. Take a screenshot showing that the file exists and its contents.
4. Shut down Ubuntu Desktop with `sudo poweroff`.
5. From VMware Fusion, restore **B06-clean-hostonly-desktop**.
6. Boot Ubuntu Desktop and check:

   ```bash
   if test -e ~/b06-snapshot-test.txt; then
     echo 'TEST FAILED: marker still exists'
   else
     echo 'TEST PASSED: marker removed after restore'
   fi
   ```

7. Capture the outcome and explain what restoring a snapshot did.

The marker should be absent if the snapshot was taken before it was created. If it is still present, inspect the selected snapshot and repeat carefully rather than claiming a pass.

## Phase C — Final verification and write-up

- [ ] Both VM snapshots exist with identifiable names.
- [ ] At least one snapshot was restored successfully.
- [ ] The marker-file rollback test passed.
- [ ] Both VMs still have the intended private network configuration after recovery.
- [ ] Final VM inventory and architecture diagram are accurate.
- [ ] Results, limitations and lessons learned are linked from the B06 README.
- [ ] Raw, relevant screenshots are uploaded separately, with captions and no passwords or secrets visible.

## What remains unverified

No B06-S4 snapshot or restore test has yet been performed. This document is a checklist and does not itself constitute successful recovery evidence.

[Previous B06-S3 network tests](network-isolation-notes.md)
