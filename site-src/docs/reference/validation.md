# Acceptance protocol

<p class="muted">The projections are not measurements. This is the short version of the acceptance run that replaces them. The full protocol lives in the repository at <code>docs/VALIDATION.md</code>.</p>

## 1. Memory

- MemTest86+: **8 complete passes**, zero errors.
- `edac-util -v`, `ras-mc-ctl --error-count`, `dmesg | grep -i edac`: all 12 DIMMs visible, zero corrected/uncorrected.
- Confirm training at the module's **JEDEC default** — 6400 MT/s for a qualifying part. Anything else means the SPD default is not 6400 and the module fails the rule.
- Twelve DIMMs across twelve channels is the stress case: watch for WHEA and training retries in the first boot, not just in the soak.

**Gate:** 8 passes clean, zero ECC errors, all 12 DIMMs at 6400.

## 2. Storage

- `lsblk`, `nvme list`, `smartctl -a`.
- Confirm `LnkSta: 8 GT/s x2` on both onboard slots. That is the expected value,
  not a fault — the slots are Gen3 x2 by design.
- `fio` sequential 1M and random 4K; record exact numbers.
- Target: ~1.8–2 GB/s sequential per drive. A Gen5 rating here is the drive's,
  not the slot's.
- SMART <70 °C; target <75 °C under load.

## 3. PCIe

- `lspci -d 1002: -vv | grep -E 'LnkCap:|LnkSta:'`: four links, each `LnkSta: Speed 16GT/s` (Gen4 riser) or `32GT/s` (Gen5).
- **Accept Gen4 deliberately.** If a passive riser trains at Gen4 and is stable, leave it — the engine's `--pcie-frac 0.15` means the link carries a fraction of the expert traffic.
- If a card drops to `2.5GT/s` or link-down under load, that riser is the fault. Swap the riser, not the card.
- `dmesg | grep -i -E 'aer|pcie bus error'`: zero AER after the full run.

## 4. Power and thermals

- Wall meter: full load ≤1 700 W at stock, ≤1 350 W at the 210 W cap.
- 12V-2x6 and board aux connectors <60 °C after 20 minutes.
- GPU edge/hotspot, CPU Tctl/Tccd, M.2, VRM: no throttle.
- **The 6-pin `P12V_PCIE` must be populated** — the board will not start without it. If the board refuses to POST, check that first.
- The CPU carries a sustained 280 W from the expert pool: verify it holds clocks for an hour, not a minute.

## 5. Engine

- `strata-device --list-devices`: four R9700s.
- Start with `--pcie-frac` at its gfx12 default (0.15); do not force 0.55 on this hardware.
- 1 stream at 262K; then 8 streams at 262K.
- Record decode, TTFT, prefill, VRAM, wall power, per-card power.
- Gate: 8×262K stable; ≥250 tok/s aggregate decode; ≥2,500 tok/s prefill at 32K; no stream <25 tok/s.
- Watch `--resident-cpu-experts` residency: if the RAM copy does not fit, decode collapses to file reads and the failure looks like a GPU fault.

## 6. Soak

- 24 h at 8 streams + 64K cold prompts.
- No drops, no VRAM growth, no ECC/AER, no thermal throttle.
- Re-check the riser links after the soak — a marginal riser fails late, not at POST.

**Only after this sheet is complete should the machine be called serving.**
