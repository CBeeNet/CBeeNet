from fastapi.responses import HTMLResponse
from urllib.parse import quote

def get_sub_page_html(api_url: str, title: str, subtitle: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>{quote(title)} · CBeeNet</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{
  --bg: #0b0b10;
  --bg2: #12121a;
  --bg3: #1a1a2e;
  --card: rgba(22, 22, 35, 0.7);
  --card2: rgba(30, 30, 50, 0.6);
  --card3: rgba(40, 40, 65, 0.5);
  --border: rgba(0, 200, 255, 0.15);
  --border2: rgba(0, 200, 255, 0.40);
  --accent: #00e5ff;
  --accent2: #00b4d8;
  --accent3: #90e0ef;
  --text: #f0f8ff;
  --text2: #b0d4f0;
  --text3: #6a8c9e;
  --green: #4ade80;
  --green-bg: rgba(74, 222, 128, 0.12);
  --red: #f87171;
  --red-bg: rgba(248, 113, 113, 0.12);
  --shadow: 0 12px 48px rgba(0, 0, 0, 0.7);
  --radius: 20px;
  --glow: 0 0 30px rgba(0, 229, 255, 0.15);
}}
html,body{{height:100%}}
body{{
  font-family: 'Vazirmatn', sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  direction: rtl;
  overflow-x: hidden;
  background: radial-gradient(ellipse at 20% 30%, #0d1b2a 0%, transparent 60%),
              radial-gradient(ellipse at 80% 70%, #1a0b2e 0%, transparent 50%),
              var(--bg);
}}
/* animated background orbs */
.orb{{
  position:fixed;
  border-radius:50%;
  filter:blur(120px);
  z-index:0;
  pointer-events:none;
  animation: floatOrb 12s ease-in-out infinite alternate;
}}
.o1{{
  width:400px;height:400px;
  background:radial-gradient(circle, rgba(0,229,255,0.10), transparent 70%);
  top:-150px;right:-100px;
  animation-delay:0s;
}}
.o2{{
  width:350px;height:350px;
  background:radial-gradient(circle, rgba(124,58,237,0.08), transparent 70%);
  bottom:-120px;left:-120px;
  animation-delay:4s;
}}
.o3{{
  width:300px;height:300px;
  background:radial-gradient(circle, rgba(0,200,255,0.06), transparent 70%);
  top:50%;left:50%;transform:translate(-50%,-50%);
  animation-delay:8s;
}}
@keyframes floatOrb{{
  0%{{transform:translate(0,0) scale(1)}}
  33%{{transform:translate(30px,-40px) scale(1.1)}}
  66%{{transform:translate(-20px,20px) scale(0.9)}}
  100%{{transform:translate(10px,-20px) scale(1.05)}}
}}
.wrap{{
  position:relative;z-index:10;
  max-width:600px;margin:0 auto;padding:20px 16px 48px;
}}
.header{{
  text-align:center;padding:30px 0 16px;position:relative;
}}
.header::after{{
  content:'';
  position:absolute;bottom:0;left:50%;transform:translateX(-50%);
  width:60px;height:3px;
  background:linear-gradient(90deg, transparent, var(--accent), var(--accent2), transparent);
  border-radius:4px;
  filter:drop-shadow(0 0 8px rgba(0,229,255,0.3));
}}
.ch-avatar{{
  width:80px;height:80px;border-radius:50%;
  margin:0 auto 16px;
  background:linear-gradient(135deg, var(--accent), var(--accent2), #7c3aed);
  display:flex;align-items:center;justify-content:center;
  font-size:38px;color:#000;
  box-shadow: 0 0 0 4px rgba(0,229,255,0.2), 0 12px 40px rgba(0,229,255,0.25);
  position:relative;
  transition:transform 0.3s ease, box-shadow 0.3s;
}}
.ch-avatar:hover{{
  transform:scale(1.06);
  box-shadow: 0 0 0 6px rgba(0,229,255,0.3), 0 16px 56px rgba(0,229,255,0.35);
}}
.ch-avatar i{{filter:drop-shadow(0 2px 4px rgba(0,0,0,0.3));}}
.ch-name{{
  font-size:22px;font-weight:900;
  background:linear-gradient(135deg, var(--text), var(--accent3));
  -webkit-background-clip:text;background-clip:text;color:transparent;
  letter-spacing:-0.02em;
}}
.ch-sub{{
  font-size:11px;color:var(--text3);margin-top:6px;
  letter-spacing:0.2em;text-transform:uppercase;font-weight:600;
  opacity:0.8;
}}
.ch-link{{
  display:inline-flex;align-items:center;gap:8px;
  font-size:12px;color:var(--accent);text-decoration:none;font-weight:700;
  margin-top:12px;padding:6px 20px;
  border-radius:40px;
  background:rgba(0,229,255,0.08);
  border:1px solid rgba(0,229,255,0.15);
  transition:all 0.25s;
  backdrop-filter:blur(4px);
}}
.ch-link:hover{{
  background:rgba(0,229,255,0.18);
  border-color:var(--accent);
  box-shadow:0 0 20px rgba(0,229,255,0.15);
  transform:translateY(-2px);
}}
.info-card{{
  background:var(--card);
  backdrop-filter:blur(12px);
  border:1px solid var(--border);
  border-radius:var(--radius);
  padding:22px 26px;
  margin-top:20px;margin-bottom:16px;
  position:relative;
  overflow:hidden;
  transition:border-color 0.3s, box-shadow 0.3s;
  box-shadow:var(--shadow);
}}
.info-card:hover{{
  border-color:var(--border2);
  box-shadow:var(--shadow), var(--glow);
}}
.info-card::before{{
  content:'';
  position:absolute;top:-80px;right:-80px;
  width:200px;height:200px;
  background:radial-gradient(circle, rgba(0,229,255,0.06), transparent 70%);
  pointer-events:none;
}}
.info-eyebrow{{
  font-size:10px;font-weight:700;color:var(--accent);
  text-transform:uppercase;letter-spacing:0.12em;
  margin-bottom:10px;
  display:flex;align-items:center;gap:8px;
}}
.info-name{{
  font-size:22px;font-weight:900;
  background:linear-gradient(135deg, #fff, var(--accent3));
  -webkit-background-clip:text;background-clip:text;color:transparent;
  margin-bottom:6px;
}}
.info-desc{{
  font-size:13px;color:var(--text2);line-height:1.8;opacity:0.9;
}}
.stats-row{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px;
}}
.stat-box{{
  background:var(--card);
  backdrop-filter:blur(8px);
  border:1px solid var(--border);
  border-radius:16px;
  padding:18px 12px;
  text-align:center;
  transition:all 0.25s;
  box-shadow:0 4px 16px rgba(0,0,0,0.2);
}}
.stat-box:hover{{
  border-color:var(--border2);
  transform:translateY(-3px);
  box-shadow:0 8px 28px rgba(0,229,255,0.08);
}}
.stat-box .sl{{
  font-size:9px;color:var(--text3);font-weight:700;
  text-transform:uppercase;letter-spacing:0.08em;
  margin-bottom:8px;
}}
.stat-box .sv{{
  font-size:22px;font-weight:900;
  background:linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip:text;background-clip:text;color:transparent;
  line-height:1.2;
}}
.stat-box .ss{{
  font-size:10px;color:var(--text3);margin-top:6px;
  display:flex;align-items:center;justify-content:center;gap:5px;
}}
.dot{{
  width:6px;height:6px;border-radius:50%;
  display:inline-block;
  animation:pulse-dot 1.5s infinite;
}}
@keyframes pulse-dot{{
  0%,100%{{opacity:1;transform:scale(1)}}
  50%{{opacity:0.3;transform:scale(0.7)}}
}}
.dot.g{{background:var(--green);box-shadow:0 0 8px var(--green)}}
.section-title{{
  font-size:12px;font-weight:800;color:var(--text3);
  text-transform:uppercase;letter-spacing:0.1em;
  margin-bottom:14px;
  display:flex;align-items:center;gap:8px;
}}
.section-title i{{font-size:16px;color:var(--accent);}}
.cfg-list{{
  display:flex;flex-direction:column;gap:12px;
}}
.cfg-card{{
  background:var(--card2);
  backdrop-filter:blur(8px);
  border:1px solid var(--border);
  border-radius:var(--radius);
  padding:18px 20px;
  transition:all 0.3s;
  position:relative;
  overflow:hidden;
  box-shadow:0 4px 16px rgba(0,0,0,0.2);
}}
.cfg-card:hover{{
  border-color:var(--border2);
  transform:translateY(-2px);
  box-shadow:var(--glow), 0 8px 32px rgba(0,0,0,0.3);
}}
.cfg-card::after{{
  content:'';
  position:absolute;top:0;right:0;
  width:4px;height:100%;
  background:linear-gradient(180deg, var(--green), var(--accent));
  border-radius:0 4px 4px 0;
  transition:background 0.3s;
}}
.cfg-card.inactive::after{{
  background:linear-gradient(180deg, var(--red), #fca5a5);
}}
.cfg-head{{
  display:flex;align-items:flex-start;justify-content:space-between;gap:10px;
  margin-bottom:12px;flex-wrap:wrap;
}}
.cfg-label-wrap{{
  flex:1;min-width:0;
}}
.cfg-label{{
  font-size:15px;font-weight:800;color:var(--text);
  display:flex;align-items:center;gap:6px;
}}
.cfg-proto{{
  font-size:9px;padding:2px 10px;border-radius:6px;
  font-weight:700;display:inline-block;margin-top:4px;
}}
.pc-ws{{
  background:rgba(0,229,255,0.10);color:var(--accent);
}}
.pc-xhttp{{
  background:rgba(124,58,237,0.12);color:#c084fc;
}}
.cfg-status-pill{{
  font-size:10px;padding:4px 12px;border-radius:30px;
  font-weight:700;display:flex;align-items:center;gap:5px;
  white-space:nowrap;flex-shrink:0;
  backdrop-filter:blur(4px);
}}
.cfg-status-pill.on{{
  background:var(--green-bg);color:var(--green);
  border:1px solid rgba(74,222,128,0.2);
}}
.cfg-status-pill.off{{
  background:var(--red-bg);color:var(--red);
  border:1px solid rgba(248,113,113,0.2);
}}
.usage-area{{
  margin-bottom:12px;
}}
.usage-text{{
  font-size:11px;color:var(--text3);
  display:flex;justify-content:space-between;margin-bottom:6px;
}}
.usage-text span b{{color:var(--text2);font-weight:700;}}
.bar{{
  height:6px;border-radius:6px;
  background:rgba(0,229,255,0.06);
  overflow:hidden;
  box-shadow:inset 0 1px 3px rgba(0,0,0,0.2);
}}
.bar-fill{{
  height:100%;border-radius:6px;
  transition:width 0.7s cubic-bezier(0.2, 0.9, 0.3, 1);
  position:relative;
  overflow:hidden;
  background:linear-gradient(90deg, var(--accent2), var(--accent), #7c3aed);
}}
.bar-fill::after{{
  content:'';
  position:absolute;inset:0;
  background:linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
  width:40%;
  animation:shimmer 2s infinite linear;
}}
@keyframes shimmer{{
  0%{{transform:translateX(-120%)}}
  100%{{transform:translateX(280%)}}
}}
.remaining-tag{{
  display:inline-flex;align-items:center;gap:5px;
  font-size:10px;font-weight:700;
  padding:3px 12px;border-radius:8px;margin-top:8px;
}}
.remaining-tag.ok{{background:var(--green-bg);color:var(--green);}}
.remaining-tag.warn{{background:rgba(0,229,255,0.10);color:var(--accent);}}
.remaining-tag.danger{{background:var(--red-bg);color:var(--red);}}
.server-section{{
  margin-top:14px;padding-top:14px;
  border-top:1px solid var(--border);
}}
.server-title{{
  font-size:10px;font-weight:700;color:var(--text3);
  text-transform:uppercase;letter-spacing:0.08em;
  margin-bottom:10px;
  display:flex;align-items:center;gap:6px;
}}
.server-title i{{color:var(--accent);font-size:14px;}}
.server-row{{
  background:var(--card3);
  backdrop-filter:blur(4px);
  border:1px solid var(--border);
  border-radius:12px;
  padding:10px 14px;
  display:flex;align-items:center;gap:8px;
  margin-bottom:8px;
  transition:all 0.2s;
}}
.server-row:hover{{
  border-color:var(--border2);
  background:rgba(40,40,65,0.7);
}}
.server-row .ip-text{{
  flex:1;font-family:ui-monospace,monospace;
  font-size:10px;color:var(--accent3);
  word-break:break-all;line-height:1.6;min-width:0;
  direction:ltr;text-align:left;
}}
.server-row .ip-label{{
  font-size:9px;color:var(--text3);white-space:nowrap;margin-left:4px;
  font-weight:600;
}}
.copy-btn{{
  font-family:inherit;font-size:10px;font-weight:700;
  padding:6px 14px;border-radius:8px;cursor:pointer;
  border:none;display:flex;align-items:center;gap:4px;
  transition:all 0.2s;white-space:nowrap;flex-shrink:0;
}}
.copy-btn.g{{
  background:linear-gradient(135deg, var(--accent), var(--accent2));
  color:#000;box-shadow:0 4px 16px rgba(0,229,255,0.25);
}}
.copy-btn.g:hover{{
  transform:translateY(-2px);
  box-shadow:0 6px 24px rgba(0,229,255,0.40);
  filter:brightness(1.1);
}}
.copy-all-bar{{
  display:flex;align-items:center;gap:16px;
  background:linear-gradient(135deg, rgba(0,229,255,0.08), rgba(124,58,237,0.06));
  border:1px solid rgba(0,229,255,0.12);
  border-radius:var(--radius);
  padding:16px 20px;
  margin-bottom:16px;
  backdrop-filter:blur(8px);
  flex-wrap:wrap;
}}
.copy-all-text{{
  flex:1;min-width:140px;
}}
.copy-all-title{{
  font-size:13px;font-weight:800;color:var(--text);
  display:flex;align-items:center;gap:6px;
}}
.copy-all-sub{{
  font-size:10px;color:var(--text3);margin-top:2px;
}}
.copy-all-btn{{
  font-family:inherit;font-size:12px;font-weight:800;
  padding:10px 22px;border-radius:12px;cursor:pointer;
  background:linear-gradient(135deg, var(--accent), var(--accent2), #7c3aed);
  color:#000;border:none;
  display:flex;align-items:center;gap:6px;
  transition:all 0.25s;
  box-shadow:0 4px 20px rgba(0,229,255,0.25);
}}
.copy-all-btn:hover{{
  transform:translateY(-3px);
  box-shadow:0 8px 32px rgba(0,229,255,0.40);
}}
.footer{{
  text-align:center;padding:32px 0 8px;
  font-size:10px;color:var(--text3);
  letter-spacing:0.05em;
}}
.footer a{{
  color:var(--accent);font-weight:700;text-decoration:none;
  transition:0.2s;
}}
.footer a:hover{{
  color:var(--accent3);text-decoration:underline;
}}
.toast{{
  position:fixed;bottom:28px;left:50%;
  transform:translateX(-50%) translateY(60px);
  background:var(--card2);
  backdrop-filter:blur(16px);
  border:1px solid var(--border);
  color:var(--text);
  border-radius:14px;
  padding:12px 24px;
  font-size:13px;font-weight:600;
  opacity:0;
  transition:all 0.4s cubic-bezier(0.2, 0.9, 0.3, 1);
  z-index:999;
  pointer-events:none;
  display:flex;align-items:center;gap:8px;
  box-shadow:0 12px 40px rgba(0,0,0,0.6);
}}
.toast.show{{
  opacity:1;transform:translateX(-50%) translateY(0);
}}
.toast.ok{{
  border-color:rgba(74,222,128,0.3);
  background:rgba(74,222,128,0.12);
  color:var(--green);
}}
.empty-state{{
  text-align:center;padding:80px 20px;
}}
.empty-state i{{
  font-size:48px;color:var(--text3);display:block;margin:0 auto 16px;
  opacity:0.5;
}}
.loading{{
  text-align:center;padding:80px 20px;
}}
.loading i{{
  font-size:48px;color:var(--accent);display:block;margin:0 auto 16px;
  animation:spin 1.2s linear infinite;
}}
.loading p{{font-size:13px;color:var(--text3);}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@media(max-width:500px){{
  .stats-row{{grid-template-columns:1fr 1fr;}}
  .stats-row .stat-box:nth-child(3){{grid-column:1/-1;}}
  .copy-all-bar{{flex-direction:column;align-items:stretch;text-align:center;}}
  .copy-all-btn{{justify-content:center;}}
  .cfg-head{{flex-direction:column;align-items:flex-start;}}
  .wrap{{padding:14px 10px 36px;}}
  .info-card{{padding:18px 16px;}}
}}
@media(max-width:380px){{
  .stats-row{{grid-template-columns:1fr;}}
  .server-row{{flex-wrap:wrap;}}
}}
</style>
</head>
<body>
<!-- Background orbs -->
<div class="orb o1"></div>
<div class="orb o2"></div>
<div class="orb o3"></div>

<div class="toast" id="toast"></div>

<div class="wrap">
  <div class="header">
    <div class="ch-avatar"><i class="ti ti-brand-netflix"></i></div>
    <div class="ch-name">CBeeNet</div>
    <div class="ch-sub">SUBSCRIPTION</div>
    <a class="ch-link" href="https://t.me/CBeeNet" target="_blank">
      <i class="ti ti-brand-telegram"></i> @CBeeNet
    </a>
  </div>

  <div id="root">
    <div class="loading"><i class="ti ti-loader-2"></i><p>در حال دریافت اطلاعات…</p></div>
  </div>

  <div class="footer">
    کانال رسمی: <a href="https://t.me/CBeeNet" target="_blank">@CBeeNet</a> · v9.4
  </div>
</div>

<script>
const API_URL = "{api_url}";
let allLinks = [];

function fmtB(b) {{
  if (!b || b === 0) return "0 B";
  if (b < 1024) return b + " B";
  if (b < 1048576) return (b / 1024).toFixed(1) + " KB";
  if (b < 1073741824) return (b / 1048576).toFixed(2) + " MB";
  if (b < 1099511627776) return (b / 1073741824).toFixed(2) + " GB";
  return (b / 1099511627776).toFixed(2) + " TB";
}}

function esc(s) {{
  return String(s || "").replace(/[&<>"']/g, c => ({{
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;"
  }})[c]);
}}

function protoBadge(p) {{
  return p && p.includes("xhttp")
    ? '<span class="cfg-proto pc-xhttp">XHTTP</span>'
    : '<span class="cfg-proto pc-ws">VLESS · WS</span>';
}}

async function loadData() {{
  try {{
    const r = await fetch(API_URL);
    if (!r.ok) throw new Error();
    return await r.json();
  }} catch (e) {{
    return null;
  }}
}}

function render(d) {{
  if (!d || !d.links || !d.links.length) {{
    document.getElementById("root").innerHTML =
      '<div class="empty-state"><i class="ti ti-link-off"></i><p style="font-size:13px;color:var(--text3)">کانفیگی یافت نشد</p></div>';
    return;
  }}
  allLinks = d.links;
  let h = "";
  const active = d.links.filter(l => l.active).length;
  const totalUsed = d.links.reduce((s, l) => s + (l.used_bytes || 0), 0);

  h += "<div class='info-card'>" +
       "<div class='info-eyebrow'><i class='ti ti-folder'></i> " +
       (d.links.length === 1 ? "کانفیگ" : "گروه دسترسی") +
       "</div>" +
       "<div class='info-name'>" + esc(d.name || "CBeeNet") + "</div>" +
       (d.desc ? "<div class='info-desc'>" + esc(d.desc) + "</div>" : "") +
       "</div>";

  h += "<div class='stats-row'>" +
       "<div class='stat-box'><div class='sl'>وضعیت</div>" +
       "<div class='sv' style='font-size:" + (d.links.length === 1 ? "18" : "22") + "px'>" +
       (d.links.length === 1
         ? (d.links[0].active ? "فعال" : "غیرفعال")
         : active + " / " + d.links.length) +
       "</div><div class='ss'></div></div>" +
       "<div class='stat-box'><div class='sl'>مصرف کل</div>" +
       "<div class='sv' style='font-size:18px'>" + fmtB(totalUsed) + "</div>" +
       "<div class='ss'>از مجموع</div></div>" +
       "<div class='stat-box'><div class='sl'>اتصالات زنده</div>" +
       "<div class='sv'>" + (d.active_connections || 0) + "</div>" +
       "<div class='ss'><span class='dot g'></span> آنلاین</div></div>" +
       "</div>";

  if (d.links.length > 1) {{
    h += "<div class='copy-all-bar'>" +
         "<div class='copy-all-text'>" +
         "<div class='copy-all-title'><i class='ti ti-copy'></i> کپی همه</div>" +
         "<div class='copy-all-sub'>یکبار کلیک</div>" +
         "</div>" +
         "<button class='copy-all-btn' onclick='copyAll()'><i class='ti ti-clipboard-copy'></i> کپی (" + active + ")</button>" +
         "</div>";
  }}

  h += "<div class='section-title'><i class='ti ti-link'></i> کانفیگ‌ها</div><div class='cfg-list'>";

  for (let i = 0; i < d.links.length; i++) {{
    const l = d.links[i];
    const pct = l.limit_bytes > 0 ? Math.min(100, (l.used_bytes / l.limit_bytes) * 100) : 0;
    const remain = l.limit_bytes > 0 ? Math.max(0, l.limit_bytes - l.used_bytes) : -1;
    const rf = remain < 0 ? "∞" : fmtB(remain);
    const rc = remain < 0 ? "ok" : (remain < 1048576 ? "danger" : (remain < 1073741824 ? "warn" : "ok"));

    h += "<div class='cfg-card" + (l.active ? "" : " inactive") + "'>" +
         "<div class='cfg-head'>" +
         "<div class='cfg-label-wrap'>" +
         "<div class='cfg-label'>" + esc(l.label) + "</div>" +
         "<div>" + protoBadge(l.protocol) + "</div>" +
         "</div>" +
         "<span class='cfg-status-pill " + (l.active ? "on" : "off") + "'>" +
         (l.active ? "<i class='ti ti-circle-check'></i> فعال" : "<i class='ti ti-circle-x'></i> غیرفعال") +
         "</span>" +
         "</div>" +
         "<div class='usage-area'>" +
         "<div class='usage-text'><span>مصرف: <b>" + l.used_fmt + "</b></span><span>سهمیه: <b>" + l.limit_fmt + "</b></span></div>" +
         "<div class='bar'><div class='bar-fill' style='width:" + pct + "%;'></div></div>" +
         "<span class='remaining-tag " + rc + "'><i class='ti " + (remain < 0 ? "ti-infinity" : "ti-database") + "'></i> " +
         (remain < 0 ? "نامحدود" : "باقی: " + rf) + "</span>" +
         "</div>";

    const lines = l.vless_link ? l.vless_link.split("\\n").filter(x => x) : [];
    if (lines.length > 0) {{
      h += "<div class='server-section'><div class='server-title'><i class='ti ti-server-2'></i> سرورهای دسترسی</div>";
      for (let j = 0; j < lines.length; j++) {{
        h += "<div class='server-row'>" +
             "<span class='ip-label'>#" + (j + 1) + "</span>" +
             "<span class='ip-text'>" + esc(lines[j]) + "</span>" +
             "<button class='copy-btn g' onclick='copyText(allLinks[" + i + "].vless_lines[" + j + "])'><i class='ti ti-copy'></i> کپی</button>" +
             "</div>";
      }}
      h += "</div>";
    }}
    h += "</div>";
  }}

  h += "</div>";
  document.getElementById("root").innerHTML = h;
}}

function copyText(t) {{
  navigator.clipboard.writeText(t).then(() => {{
    const toast = document.getElementById("toast");
    toast.textContent = "✅ کپی شد";
    toast.className = "toast show ok";
    setTimeout(() => toast.classList.remove("show"), 1800);
  }});
}}

function copyAll() {{
  const t = allLinks.map(l => l.vless_link || "").filter(x => x).join("\\n");
  if (!t) return;
  navigator.clipboard.writeText(t).then(() => {{
    const toast = document.getElementById("toast");
    toast.textContent = "✅ همه کپی شد";
    toast.className = "toast show ok";
    setTimeout(() => toast.classList.remove("show"), 1800);
  }});
}}

(async function init() {{
  const d = await loadData();
  if (d) {{
    d.links.forEach(l => l.vless_lines = l.vless_link ? l.vless_link.split("\\n").filter(x => x) : []);
    render(d);
  }} else {{
    document.getElementById("root").innerHTML =
      '<div class="empty-state"><i class="ti ti-alert-circle" style="color:var(--red)"></i><p style="font-size:13px;color:var(--text3)">خطا در بارگذاری</p></div>';
  }}
}})();
</script>
</body>
</html>"""


def get_public_page_html(uuid_key: str) -> str:
    return get_sub_page_html(
        api_url=f"/api/public/sub/{uuid_key}",
        title="CBeeNet Group",
    )


def get_single_sub_page_html(uuid: str) -> str:
    return get_sub_page_html(
        api_url=f"/api/public/sub-single/{uuid}",
        title="CBeeNet Config",
    )
