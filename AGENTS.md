
## Anti-detection browser stack (this project)

Two routes, both installed server-wide (details in `~/.config/opencode/AGENTS.md`
§ "Anti-detection browser stack"). Route 1: **camofox-browser** server
(`camofox` CLI, `--user <shop>` persistent profiles, port 9377) — use for
eBay/Proshop/Tonitron-style walls. Route 2: **trawl** Docker container
(`localhost:8191/scrape`) — Cloudflare-tier fallback; proven on
bargainhardware.co.uk. Route doc for the RAM hunt:
`docs/research/camofox-route.md`. Skills: `$camofox-browser`, `$camofox-cli`.
