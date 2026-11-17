# Storage and lanes

<p class="muted">Two Gen5 drives in a board whose M.2 slots are Gen3 x2. That mismatch is accepted, not fixed, because the disk is not on the engine's hot path.</p>

## What the board offers

| Port | Width / generation | Notes |
|---|---|---|
| `M2_0`, `M2_1` | **PCIe Gen3 x2** | 2280/22110. ~2 GB/s each — a fifth of a Gen5 drive |
| `U2_P0_G1A`, `U2_P0_G1B` | Gen5 x8 | unused in this build |
| `U2_P0_P0A`, `U2_P0_P0B` | Gen5 x8 **or SATA** | unused in this build |
| SATA | **none** | `SATA_SGP1/2` are backplane SGPIO headers, not ports |

## The two drives

| Drive | Interface | Runs at |
|---|---|---|
| Samsung 9100 PRO 2 TB (`MZ-VAP2T0B`) | Gen5 x4 | ~2 GB/s in the onboard slot |
| XPG Mars 980 2 TB | Gen5 x4 | ~2 GB/s in the onboard slot |

Costing a Gen5 drive and running it at Gen3 x2 is a deliberate trade. The
alternatives are cheaper or equal, and each adds parts this build does not have:

- A **Gen3 x2-class drive** would cost less for the same speed. The pick here is
  availability, not throughput.
- An **MCIO adapter** would give the drives Gen5 x4, at the price of one MCIO
  port, a power lead, and a part outside the envelope of this build.

If the drives ever need to be faster, that is a separate decision with its own
part. Nothing else in the build changes.

## What the disk is actually asked to do

- **Model load, once per start.** A 79 GB IQ3_S at ~2 GB/s is about 40 s. At
  Gen5 x4 it would be about 6 s. Once, not per token.
- **Nothing during decode.** Experts come from VRAM or from host RAM via
  `--resident-cpu-experts`; the PLE table comes from RAM when `--ple-io ram` is
  set, which is the recommended configuration.
- **Checkpoint writes**, if conversation cache is used.

A per-token disk dependency would make this the wrong choice. There is none.

## Thermal reality

- Onboard M.2 sits under the GPU risers. Four risers hold the cards away from
  the board, which is better than four cards seated over the sockets.
- A Gen5 drive running at Gen3 x2 generates far less heat than the same drive at
  full Gen5, so the thermal case is easier, not harder.
- Target <70 °C from `smartctl -A`.

## RAID 0 reality

Two drives in RAID 0 double the failure surface for throughput a model load
barely notices. Keep them separate: one for the OS, one for models.

## Lane budget

| Consumer | Lanes |
|---|---:|
| 4× PCIe 5.0 x16 GPUs (risers) | 64 |
| 2× onboard M.2 (Gen3 x2) | 4 |
| **CPU total** | **128** |

This uses 68 of 128 Gen5 lanes. Lane count is not a constraint on SP5.

