# CMP 170HX on AliExpress — verified pass (2026-11-15)

Question: are the "CMP 170HX, buy 3 get 2 free, unlock to 80GB A100" AliExpress
listings real, and should we buy 4 cards to unlock ourselves?

Route: **camofox-browser** (`--user alicards`, persistent profile). Plain fetch
returns only the page footer; camofox renders the real PDP including the
AI-generated product summary, spec table and seller card. `trawl` not needed.

## 1. Verdict

- **The research is real**: Kate's VFI writeup (blog.kate.land, 2026-11-10) +
  `kate-land/ga100vfi` (132★) + `amoghmunikote/cmpunlocker` (871★). 8GB card →
  gold 64GB software unlock; 80GB + full SMs need voltage glitching (1–48 h per
  card, per-die fuse burns, payload not published).
- **The WhatsApp / "buy N get M free" cluster is a scam template.** All verified
  listings in it are keyword-stuffed repurposed product pages.
- **One credible seller found**: `Wholesale Tech Store`, 100.0% positive.

## 2. Scam listings — evidence

| Item | Advertised | Actually is |
|---|---|---|
| `1005013131659959` (user's link) | CHF 416.99 GPU | **Vinyl record stand.** AliExpress AI summary: "Vinyl-Regalhalter … 10×10×1 cm, 0,040 kg", brand `tongyue`, 10 000 available, free ship. Same seller as link 2. |
| `1005013586996809` (user's link 2) | "AQ buy 2 get 1" | Same seller `Shop1105817498`, same brand `tongyue`, 0 sold, 0.0% feedback, 47 followers |
| `1005013470506899` | "2+1 … 64GB unlock + capacitor mod" | `Shenzhen Miner Ltd Store`, **0.0%** feedback; spec field = `Abirateronacetat` (a drug) — stuffed page |
| `1005013486035104` | "fully tested 40/80GB" CHF 368 | `Lush Gleam Store`, **0.0%** feedback, 26 followers; spec = `Material: Kunststoff`, `Menge: 20`, shipping **CHF 159.80** — plastic parts |
| `1005013449053925` | "unlocked 64GB 4-GPU workstation" | `Shenzhen Miner Ltd Store` again, 0.0% |

Common tells: 0.0% positive feedback, `tongyue`/no brand, spec fields from an
unrelated product, absurd stock (10 000 / 899), WhatsApp number in the artwork
(two different US/CA VoIP numbers across the same template), bundles only in the
poster — the PDP buy box sells **one card**.

## 3. Credible listing(s) — `Wholesale Tech Store`

| Item | Description | Price | Stock | Sold |
|---|---|---|---|---|
| `1005013600475443` | 8GB CMP 170HX, **64GB VRAM, fully tested, PCIe 2.0 x16 mod**, with fan | CHF 736.99 | **340** | 14 |
| `1005013600473572` | 10GB, 40GB/80GB, PCIe 2.0 x16 mod | CHF 548.19 | 1 | 7 |
| `1005013579548143` | 8GB GDDR6, customisable BIOS | CHF 469.39 | 510 | 14 |

Store: `de.aliexpress.com/store/1105875107`, 100.0% Positive, 39 Follower,
origin Hong Kong, shipping CHF 25.06, delivery Nov 24–Dec 2. Below-market but not
absurd → consistent with real refurb stock, not bait.

**Not yet verified (needs cart/account):** whether CHF 736.99 is per-card or a
bundle-tier unit; final VAT/IOSS treatment for PL (23% ≈ +$800 on 4 cards);
whether "fully tested" includes the patched driver.

## 4. Buy/no-buy

Buy **4 × `1005013600475443`** (≈ CHF 2 948 = $3 516 before VAT) **through the
cart**, card payment, one card first to validate the seller.

Constraints to plan around:
- **NVLink only pairs.** U11 bridge mod + an unpublished ROM-check bypass. 4 cards
  = 2 pairs; cross-pair all-reduce falls back to PCIe Gen2 x16 ≈ 2 GB/s.
- **No FP8/FP4** — Ampere, INT8 ceiling.
- Seller does the hardware half (cap mod, memory geometry). `cmpunlocker` covers
  the software half free. The 64→80GB VFI step remains a self-run weekend project
  on one card, not a paid product.

On arrival: `nvidia-smi -q` (expect 65536 MiB / 70 SM / PCIe Gen2 x16) →
framebuffer write-read sweep across all 64 GB → real model run → open dispute
inside buyer protection if DOA, before touching hardware.

## 5. Anti-detection route note

camofox handles AliExpress PDPs cleanly with one `--user alicards` profile and
survived a ~15-navigation sweep with no wall or CAPTCHA. No `trawl` fallback
needed. Artificial rule for future shop passes: ≤6 navigations per store per
pass still applies (eBay lesson), though AliExpress did not throttle here.
