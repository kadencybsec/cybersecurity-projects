# B06 — Home lab plan

**Step:** B06-S1 · **Status:** Completed (user-confirmed checks) · **Started:** 3 November 2026

## Why I'm building it

I want a small lab where I can learn Linux, networking and basic security testing without changing anything on my main Mac or home network.

## My computer

- Host: Apple Silicon Mac
- Memory: 16 GB
- Exact chip: to check
- macOS version: to check
- Available disk space: to check

## Virtualisation choice

**VMware Fusion Pro**, latest stable release compatible with my Mac. It supports Apple Silicon, ARM64 Linux guests, host-only networking and snapshots. The free version includes these features. I'll download it from the official Broadcom/VMware portal.

**Guest system:** Ubuntu Desktop 26.04 LTS, **ARM64/aarch64** installation image from ubuntu.com. I will not download the Intel/AMD x86_64 ISO for Fusion on this Mac.

### VM inventory (planned, not installed)

| VM | Role | CPU | RAM | Virtual disk | Network |
|:--|:--|--:|--:|--:|:--|
| `lab-ubuntu-arm` | Linux learning workstation | 4 vCPU | 6 GB | 50 GB, growable | Host-only for experiments; temporary NAT for updates |
| `lab-target-arm` | Second harmless test machine, added in B06-S3 | 2 vCPU | 2 GB | 25 GB, growable | Same host-only network |

I will run one VM at a time whenever possible. If the host becomes slow, I will lower the first VM to 4 GB RAM. I will not start a second VM until I have checked host storage and RAM use. Disk images and snapshots can grow, so the allocated disk sizes are **not** a reliable measure of space used.

## Network design

```text
Apple Silicon Mac
  └── VMware Fusion Pro
       └── host-only virtual network (VMnet1)
            ├── lab-ubuntu-arm (B06-S2)
            └── lab-target-arm (B06-S3)

No normal internet route via VMnet1.
The Mac host can still reach both VMs, so host-only is not complete isolation from the host.
```

- Default experiments: **Private to my Mac / Host-only**, not bridged.
- Internet required for installing or updating packages: temporarily switch the **trusted, updated** Ubuntu VM to **NAT / Share with my Mac**, then return to host-only and check the adapter.
- Avoid dual adapters and USB/shared-folder/clipboard convenience features for untrusted lab tasks.
- Treat the host-only network as a place for machines I own and control, not an excuse to scan a real router or neighbouring devices.
- Verify in B06-S3 that the two VMs can reach one another in host-only mode, and that they cannot reach an internet destination while isolated.

## Snapshot plan

1. `01-clean-install`: after Ubuntu is installed and first updated, before experimenting.
2. `02-lab-configured`: after the host-only setup and basic tools are configured.
3. `before-experiment-YYYYMMDD`: immediately before a lab change that I may want to undo.
4. In B06-S4, make a harmless test change and **restore a snapshot**, then write down what happened.

Snapshots help roll back a VM, but they are **not a substitute for an external backup**. I'll stop the VM and copy the full VM bundle to external storage or an appropriate backup destination when needed. The copy must not accidentally expose passwords or private notes.

## Checklist for B06-S1

- [x] Choose an ARM-compatible hypervisor and Linux distribution.
- [x] Plan VM sizes and a private two-VM network.
- [x] Decide when to use host-only versus temporary NAT.
- [x] Write snapshot names and a restore-test plan.
- [x] Check macOS version and available disk space (user reports checks done; actual values not provided).
- [x] Confirm adequate host space for the proposed VM setup (user-confirmed; no exact amount recorded).

Once the two remaining checks are done, I can close B06-S1. Installing Ubuntu belongs to B06-S2.

## References

- VMware Fusion free edition and included networking/snapshot features: https://www.vmware.com/docs/desktop-hypervisor-faqs
- VMware Fusion Apple Silicon ARM guest compatibility: https://knowledge.broadcom.com/external/article/315602
- VMware network modes: https://knowledge.broadcom.com/external/article/303393
- Official Ubuntu Desktop ARM64 image: https://ubuntu.com/download/desktop

## Work log

- **3 November 2026:** Initial design recorded; Mac storage and exact macOS version still to confirm.

## Fusion configuration observed (3 November 2026)

The VMware Fusion **Finish** screen recognised the selected installer as **Ubuntu 64-bit Arm 26.04.1**. The proposed VM configuration displayed **20 GB disk, 6 GB RAM, 2 CPU cores and Share with my Mac (NAT)**. This is a setup-wizard summary, **not evidence of Ubuntu installation**.

**Action before booting:** open Customize Settings, set the growable virtual disk to 50 GB if host storage allows, keep 6 GB RAM and 2 CPU cores, and use NAT temporarily to install/update. The planned security lab network remains host-only after updates.

**Still to verify:** actual available Mac disk space and macOS version. No B06-S1 completion claimed.

## Virtual disk settings verified in Fusion (3 November 2026, 17:16)

The user-provided VMware Fusion **Hard Disk (NVMe)** screenshot displays a **50.00 GB** virtual disk. The Apply button is greyed out, consistent with there being no unsaved change. This verifies the **configured virtual disk capacity**, not the Mac's available host storage or successful guest OS installation. Next checks: verify 6 GB RAM, 2 CPU cores, NAT for installation, then check host storage before proceeding.

## B06-S1 completion report — 3 November 2026

The user reports that the remaining Mac checks and VMware configuration are in place. The hypervisor choice, ARM64 Ubuntu image, two-VM design, NAT-to-host-only network strategy, and snapshot plan are documented above. The exact macOS version and available host disk-space number were **not shared**, so those values have not been independently verified in this portfolio.

**B06-S1 is complete as a documented design and user-confirmed readiness check.** This does not prove a guest OS has booted or that network isolation/recovery tests succeeded; those belong to B06-S2 through S4.

## B06-S2 installation review (3 November 2026, 17:27)

The user shared Ubuntu's **Ready to install** summary from within VMware Fusion. The selected target was `nvme0n1` with **Erase disk and install Ubuntu**, a FAT32 EFI partition (`nvme0n1p1` mounted at `/boot/efi`), and an ext4 root partition (`nvme0n1p2` mounted at `/`). The default application selection and no guest disk encryption were selected. This is consistent with installing Ubuntu 26.04.1 ARM64 to the newly configured VMware virtual disk. The summary itself did not show capacity; the previous VMware settings screenshot showed a 50 GB virtual disk.

**Evidence status:** Installer configuration reviewed, but Ubuntu installation, first login, networking tests and guest system verification are not yet shown. The screenshot is held in the chat and is not embedded in the repository.
