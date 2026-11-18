# Storage and lanes

<p class="muted">The array lives on MCIO at full Gen5 x4, not on the two onboard M.2 slots, which are Gen3 x2. That matters more than it looks: it is the storage half of why the board choice works.</p>

## What the board offers

| Port | Width / generation | Used for |
|---|---|---|
| `Slot_1` … `Slot_5` | **PCIe Gen5 x16, five of them** | 4× R9700 (three direct, one on an extender) |
| MCIO 8i #1 | Gen5 x8 | **2× 9100 PRO now** (via 8i→2× M.2 adapter) |
| MCIO 8i #2 | Gen5 x8 | **Free — drives 3 and 4 after expansion** |
| MCIO 8i #3 | Gen5 x8 **or SATA** | Cold SATA SSD (cable in the box) |
| MCIO 8i #4 | Gen5 x8 **or SATA** | Spare |
| `M2_0`, `M2_1` | **PCIe Gen3 x2** | Optional boot disk. ~2 GB/s, a fifth of a Gen5 drive |
| SATA | **none onboard** | The 8× SATA cable from MCIO #3 is the path |

## The array

| Stage | Drives | Ports | Capacity | Sequential |
|---|---|---|---:|---|
| **Now** | 2× 9100 PRO 2 TB | MCIO #1 (x8) | **4 TB** | **~29 GB/s** |
| **Later** | 4× 9100 PRO 2 TB | MCIO #1 + #2 | **8 TB** | **~59 GB/s** |

Two Gen5 x4 drives on one x8 port is the natural fit: 2× 14.8 GB/s ≈ 29 GB/s
against a 32 GB/s ceiling. The expansion is the same drive, the same adapter and
the next MCIO connector — no other part changes.

RAID 0 across them is a choice, not a requirement. Two separate drives (models on
one, checkpoints on the other) cost nothing in throughput a model load notices
and halve the failure surface.

## Why not the onboard M.2

`M2_0`/`M2_1` are **PCIe Gen3 x2** — about 2 GB/s each. A 9100 PRO there runs at
14% of its rating. It works, and it is a perfectly good boot disk, but putting a
Gen5 array on a Gen3 x2 link costs four times the load time for no benefit.

This is also why the previous board's storage story was worse: it spent an MCIO
group on a fourth-GPU adapter. On the MZ23-SU0 the fourth GPU is a slot, so
**all four MCIO connectors stay available for drives**.

## What the disk is actually asked to do

- **Model load, once per start.** A 79 GB IQ3_S at ~29 GB/s is about 3 s. It was
  ~40 s over a Gen3 x2 slot. Once per start, not per token.
- **Nothing during decode.** Experts come from VRAM or from host RAM via
  `--resident-cpu-experts`; the PLE table comes from RAM when `--ple-io ram` is
  set, which is the recommended configuration.
- **Checkpoint writes**, if conversation cache is used.

A per-token disk dependency would make any of this the wrong choice. There is
none — but the load-time difference is real and is why the array goes on MCIO.

## Thermal reality

- The MCIO adapters sit in the airflow path, not under the GPUs. Better than four
  cards breathing on an onboard M.2.
- Full-Gen5 drives run hotter than the same drives throttled to Gen3 x2. Give the
  adapter area a fan and target **<70 °C** from `smartctl -A`.
- The fourth card, on an extender, is the part most likely to sit near a drive.
  Plan the extender route before the drives.

## Cold storage

One **870 EVO** on MCIO #3 via the **8× SATA cable included in the retail box**
(`25CF9-6007A7-A4R`). The board has no native SATA ports, so this is the
documented path and it needs no extra purchase.

1 TB holds the OS and the model archive but **not** an image of a 4 TB array. For
array images, use the 870 EVO 4 TB or an 8 TB HDD — and at 8 TB of array you need
the HDD regardless.

## Lane budget

| Consumer | Lanes |
|---|---:|
| 4× PCIe 5.0 x16 GPUs | 64 |
| 2× MCIO 8i for the array | 16 |
| 1× MCIO 8i for SATA | 8 |
| 2× onboard M.2 (Gen3 x2, if used) | 4 |
| **CPU total** | **128** |

This uses 88 of 128 Gen5 lanes, leaving room for the spare MCIO and a NIC. Lane
count is not a constraint on SP5 — it never was. The constraint was **slot
count**, and five native x16 slots is what makes this board the pick.
