# B06 — VMware Fusion download and first launch

**Date:** 3 November 2026  
**Step:** B06-S1 lab planning; preparing for B06-S2 VM installation  
**Download issue:** Resolved based on observed Fusion launch  
**VM installation:** Not yet started

## What happened
The Broadcom Support Portal initially displayed **“Screening Required”** beside the VMware Fusion **26H1u1** download. Later, VMware Fusion was running locally on the Mac and showing the **“Select the Installation Method”** window. This confirms the application launched successfully; it does not yet prove that Ubuntu was installed.

## Next steps
- [x] Reach the VMware Fusion virtual-machine creation wizard.
- [ ] Download an **Ubuntu 26.04.1 LTS Desktop ARM64** ISO from https://ubuntu.com/download/desktop.
- [ ] In Fusion, choose **Install from disc or image** and select the ARM64 ISO.
- [ ] Configure the planned VM resources and confirm macOS and free disk space before installation.
- [ ] Install Ubuntu during B06-S2.
- [ ] Test network isolation and snapshots in later steps.

## Evidence notes
- **Observed in user screenshot:** Fusion's “Select the Installation Method” wizard, offering disc/image, Windows and remote server options.
- **Meaning:** Fusion can run on this Mac; an operating system has not been installed inside a VM yet.
- **Image status:** Screenshot remains in the study chat; not uploaded to this repository.
- **Result:** Broadcom download blocker no longer prevents opening VMware Fusion.

See [B06 lab design](lab-plan.md).
