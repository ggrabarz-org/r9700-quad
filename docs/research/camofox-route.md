# CamoFox route — the standing browser path for the RAM hunt

**Tool:** [camofox-browser](https://github.com/redf0x1/camofox-browser) v2.5.0 — REST/CLI server wrapping the
Camoufox engine (Firefox, C++-level fingerprint spoofing). Installed globally; engine at
`/root/.cache/camofox-browser-engine` (v158.0.1-beta.41).

## Why this route (measured, not assumed)

| Attempt | Result |
|---|---|
| curl + r.jina.ai | works only for non-walled shops; 403 on Proshop.de/Tonitrus/picclick; DDG 202/403 |
| Playwright Chromium + UA masking | IP-walled by eBay.com (4/4 error pages); Galaxus HTTP2-blocked; Kaufland/Mindfactory click-walls |
| **Camoufox (python lib)** | cracked eBay.com + Galaxus search, but **every session is a new identity** → eBay rate-limited the IP within ~12 navigations, then IP-banned the domain |
| **camofox-browser server (persistent profiles)** | **no throttling** — same IP, same shop, unlimited passes; consent/cookies persist |

## Standing procedure

```bash
export PATH=/root/.nvm/versions/node/v24.22.0/bin:$PATH
export CAMOUFOX_INSTALL_DIR=/root/.cache/camofox-browser-engine

camofox server status                       # if down: camofox server start --background
curl -s localhost:9377/health               # {"ok":true,"engine":"camoufox",...}

# ONE PERSISTENT PROFILE PER SHOP — always pass --user <shop>
camofox open "<url>" --user ebay --format json
sleep 4
camofox snapshot --user ebay > /tmp/opencode/ramcheck/snap.txt   # accessibility tree, refs [eN]
grep -iE 'EUR|MwSt|verfügbar|Versand' /tmp/opencode/ramcheck/snap.txt
```

- `snapshot` is the cheap read (accessibility tree, small). `get-text` returns >1 MB on eBay → **always redirect to a file**, never stdout.
- Consent dialog: click the accept ref once per profile; it persists in that profile.
- Budget: **≤6 navigations per shop per pass**; one dossier per item.
- Multi-profile isolation verified: `--user ebay` and `--user proshop` run as separate persistent contexts.
- Skills installed for agents: `.agents/skills/camofox-browser`, `.agents/skills/camofox-cli` (`npx skills add redf0x1/camofox-browser`).

## What still needs plain curl (cheaper, not walled)

ibfusion · senetic.pl · senetic.de · Kingston datasheets (`kingston.com/datasheets/<PN>.pdf` + `pdftotext`) ·
Kingston/memorycow Algolia JSON (app `C7SR80KDDJ`, index `kingstonindex` / `memcowindex`).

## Dead ends (do not retry)

Kaufland.de · Mindfactory (interactive click-wall) · Galaxus product pages (CAPTCHA; search tiles work) ·
Amazon.de (error-page cycle; occasionally serves, filter unreliable) · abstock.com (SSL cert CN broken) ·
serverpartdeals.com · bulk-memory.eu · itpro.lt · mem-tek.fr · etb-online/etbhost · ramexpert · po-memory ·
mr-memory.co.uk · svp.co.uk (DNS dead) · dataprint.sk (print shop) · eBay via r.jina.ai/picclick (use the server).

## SPD rule (unchanged, non-negotiable)

A module qualifies only if its **JEDEC SPD default is 6400 @ 1.1 V**.
Kingston: quote the datasheet sentence. Samsung/Micron/hynix: **"no SPD sentence published"** — never guess.
