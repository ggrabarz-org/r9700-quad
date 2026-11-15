# Network & IP-routing map (r9700-quad host) — 2026-11-15

## Topology (verified)

```
Internet ── router/gateway 192.168.88.1 (78:9a:18:74:59:39)
    │            NAT → public IP 144.2.104.89  (single uplink)
    │
 192.168.88.0/24  (bridged LAN)
    ├─ 192.168.88.239  proxmoxht40 (Proxmox VE 9.2, root SSH via id_ed25519_proxmox)
    │     ├─ LXC 102 Ubuntu26.04  = 192.168.88.241  ← THIS container (xrdp on 3389)
    │     ├─ VM 100 Win11EN-PURE        (stopped)
    │     ├─ VM 101 Win11EN-CodeSys3.5  (stopped, 16 GB)
    │     ├─ VM 103 Win11EN-NVME        (stopped)
    │     └─ VM 104 Win11EN-oobe        (stopped)
    ├─ 192.168.88.246  Mac (a0:ce:c8:…), ASLEEP/OFF (stale ARP, no ports)
    └─ (no other live hosts in a full /24 22/3389/5900 scan)
```

- **Public IP is shared by the entire LAN: 144.2.104.89.** The eBay IP-ban (144.2.104.x) was on this
  single egress. Routing via the Mac, a Windows VM, or the Proxmox host changes NOTHING — same NAT.
- Proxmox host has `wg` (wireguard) installed but **no VPN interfaces configured**. `nic1` (2nd
  physical NIC) is DOWN (no cable). No IPv6 egress.
- Mac is currently unreachable (asleep/off); when on, not running sshd (22 closed at last sighting).

## What actually gives a different egress IP

1. **WireGuard client on the proxmox host** (or in this container) + a remote endpoint the user owns
   (VPS or commercial VPN with wg config). Then NAT 192.168.88.241 through it → new IP for camofox/trawl.
2. **SSH SOCKS tunnel to a machine that runs a VPN**: `ssh -D 1080 <mac-or-vps>` → point camofox
   (`PROXY_HOST/PORT`) or trawl (`PROXY_URL`) at `socks5://…`. Requires the remote host to have a VPN
   active AND sshd reachable.
3. **Commercial residential proxy** — the standard answer for IP rotation in scraping; plug into both
   camofox (`PROXY_HOST/PORT/USERNAME/PASSWORD`) and trawl (`PROXY_URL`). Costs money, no hardware needed.
4. **Windows VMs / Mac over the LAN** — fingerprint variety yes, IP variety no.

## T3 environment linking

`t3_environment_links` → none linked. To drive the Mac/Win through T3, open T3 Code on that machine
and link it (Settings → Labs → Linked environments). Same-IP caveat still applies.

## eBay status note

2026-11-15: eBay.de serves again through camofox's persistent `--user ebay` profile (item page +
prices rendered; price US $2.808,44 / €2.547,80 confirmed live). The IP ban was temporary (~15 h).
Keep one-identity-per-site discipline: do not hammer.
