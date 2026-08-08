from fastapi.responses import HTMLResponse
from urllib.parse import quote

def get_sub_page_html(api_url: str, title: str, subtitle: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>{quote(title)} · CBeeNet</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700;14..32,800;14..32,900&family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
  /* ===== RESET & ROOT ===== */
  * {{ margin:0; padding:0; box-sizing:border-box; -webkit-tap-highlight-color:transparent; }}
  :root {{
    --bg: #08060b;
    --surface: rgba(16, 14, 26, 0.75);
    --surface2: rgba(28, 24, 44, 0.6);
    --surface3: #1e1a2e;
    --border: rgba(255, 255, 255, 0.06);
    --border-glow: rgba(180, 80, 255, 0.3);
    --text: #f2edff;
    --text2: #b8b0d0;
    --text3: #6a6380;
    --primary: #a855f7;
    --primary-light: #c084fc;
    --primary-dark: #7c3aed;
    --secondary: #ec4899;
    --accent: #f472b6;
    --green: #34d399;
    --green-bg: rgba(52, 211, 153, 0.12);
    --red: #fb7185;
    --red-bg: rgba(251, 113, 133, 0.12);
    --radius: 28px;
    --shadow: 0 20px 60px rgba(0,0,0,0.7);
    --glow: 0 0 50px rgba(168,85,247,0.15);
  }}
  html, body {{ height:100%; }}
  body {{
    font-family: 'Vazirmatn', 'Inter', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    direction: rtl;
    overflow-x: hidden;
    background-image:
      radial-gradient(circle at 20% 30%, rgba(168,85,247,0.10) 0%, transparent 60%),
      radial-gradient(circle at 80% 70%, rgba(236,72,153,0.07) 0%, transparent 60%),
      radial-gradient(circle at 50% 50%, rgba(0,0,0,0) 0%, var(--bg) 100%);
  }}

  /* ===== ANIMATED BG ===== */
  .orb {{
    position: fixed;
    border-radius: 50%;
    filter: blur(90px);
    opacity: 0.3;
    pointer-events: none;
    z-index: 0;
    animation: orbFloat 20s ease-in-out infinite alternate;
  }}
  .orb1 {{ width: 400px; height: 400px; background: var(--primary); top: -5%; left: -10%; animation-delay: 0s; }}
  .orb2 {{ width: 350px; height: 350px; background: var(--secondary); bottom: -5%; right: -10%; animation-delay: -7s; }}
  .orb3 {{ width: 300px; height: 300px; background: var(--primary-dark); top: 40%; left: 50%; animation-delay: -14s; opacity: 0.15; }}
  @keyframes orbFloat {{
    0% {{ transform: translate(0, 0) scale(1); }}
    100% {{ transform: translate(60px, -60px) scale(1.2); }}
  }}

  /* ===== WRAPPER ===== */
  .wrap {{
    position: relative;
    z-index: 10;
    max-width: 560px;
    margin: 0 auto;
    padding: 28px 16px 48px;
  }}

  /* ===== HEADER ===== */
  .header {{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 8px 0 24px;
  }}
  .logo-wrap {{
    width: 96px;
    height: 96px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 44px;
    color: #fff;
    box-shadow: 0 0 0 8px rgba(168,85,247,0.15), 0 20px 60px rgba(168,85,247,0.3);
    transition: all 0.5s ease;
    position: relative;
  }}
  .logo-wrap::after {{
    content: '';
    position: absolute;
    inset: -4px;
    border-radius: 50%;
    padding: 2px;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary), var(--primary-light));
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    opacity: 0.6;
  }}
  .logo-wrap:hover {{ transform: scale(1.06) rotate(-4deg); box-shadow: 0 0 0 12px rgba(168,85,247,0.2), 0 25px 70px rgba(168,85,247,0.4); }}
  .brand {{
    font-size: 32px;
    font-weight: 900;
    margin-top: 18px;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary), var(--primary-light));
    background-size: 200% 200%;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: gradShift 6s ease infinite;
    letter-spacing: -0.02em;
  }}
  @keyframes gradShift {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
  }}
  .tagline {{
    font-size: 11px;
    color: var(--text3);
    letter-spacing: 0.4em;
    text-transform: uppercase;
    font-weight: 600;
    margin-top: 4px;
  }}
  .tele-link {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-top: 18px;
    padding: 10px 26px;
    border-radius: 40px;
    background: rgba(168,85,247,0.10);
    border: 1px solid rgba(168,85,247,0.15);
    color: var(--primary-light);
    font-size: 13px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }}
  .tele-link:hover {{
    background: rgba(168,85,247,0.18);
    border-color: var(--primary);
    box-shadow: 0 0 40px rgba(168,85,247,0.15);
    transform: translateY(-3px) scale(1.02);
  }}

  /* ===== GLASS CARD ===== */
  .glass {{
    background: var(--surface);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
  }}

  /* ===== INFO CARD ===== */
  .info-card {{
    background: var(--surface);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 26px 28px;
    margin: 14px 0 18px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s;
  }}
  .info-card:hover {{ border-color: var(--border-glow); }}
  .info-card .glow-spot {{
    position: absolute;
    top: -80px;
    right: -80px;
    width: 260px;
    height: 260px;
    background: radial-gradient(circle, rgba(168,85,247,0.08), transparent 70%);
    pointer-events: none;
  }}
  .info-eyebrow {{
    font-size: 10px;
    font-weight: 700;
    color: var(--primary-light);
    text-transform: uppercase;
    letter-spacing: 0.2em;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
  }}
  .info-name {{
    font-size: 26px;
    font-weight: 800;
    background: linear-gradient(135deg, #fff, var(--primary-light));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin-bottom: 6px;
  }}
  .info-desc {{
    font-size: 13px;
    color: var(--text2);
    line-height: 1.8;
  }}

  /* ===== STATS ===== */
  .stats {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-bottom: 20px;
  }}
  .stat-item {{
    background: var(--surface2);
    border-radius: 20px;
    padding: 18px 8px;
    text-align: center;
    border: 1px solid var(--border);
    transition: all 0.3s;
    backdrop-filter: blur(8px);
  }}
  .stat-item:hover {{
    border-color: var(--border-glow);
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.3);
  }}
  .stat-label {{
    font-size: 9px;
    font-weight: 700;
    color: var(--text3);
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }}
  .stat-value {{
    font-size: 24px;
    font-weight: 800;
    margin-top: 4px;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }}
  .stat-sub {{
    font-size: 10px;
    color: var(--text3);
    margin-top: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 4px;
  }}
  .dot-live {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--green);
    display: inline-block;
    animation: pulse-dot 1.8s infinite;
  }}
  @keyframes pulse-dot {{
    0%,100% {{ opacity:1; transform:scale(1); }}
    50% {{ opacity:0.2; transform:scale(0.6); }}
  }}

  /* ===== COPY ALL BAR ===== */
  .copy-all {{
    background: var(--surface);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 16px 22px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 14px;
    flex-wrap: wrap;
    background: linear-gradient(135deg, rgba(168,85,247,0.06), rgba(236,72,153,0.04));
    border-color: rgba(168,85,247,0.10);
  }}
  .copy-all-text {{
    flex: 1;
    min-width: 130px;
  }}
  .copy-all-title {{
    font-size: 15px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .copy-all-sub {{
    font-size: 10px;
    color: var(--text3);
  }}
  .btn-copy-all {{
    font-family: inherit;
    font-size: 13px;
    font-weight: 800;
    padding: 10px 24px;
    border: none;
    border-radius: 40px;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: #fff;
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 4px 25px rgba(168,85,247,0.3);
  }}
  .btn-copy-all:hover {{
    transform: scale(1.04);
    box-shadow: 0 8px 40px rgba(168,85,247,0.5);
  }}

  /* ===== CONFIG LIST ===== */
  .section-header {{
    font-size: 13px;
    font-weight: 800;
    color: var(--text3);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin: 28px 0 16px;
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .section-header i {{ color: var(--primary-light); font-size: 18px; }}

  .config-item {{
    background: var(--surface);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    margin-bottom: 16px;
    overflow: hidden;
    transition: all 0.3s;
  }}
  .config-item:hover {{
    border-color: var(--border-glow);
    box-shadow: var(--glow), var(--shadow);
  }}
  .config-header {{
    padding: 18px 22px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    cursor: pointer;
    user-select: none;
    transition: background 0.2s;
  }}
  .config-header:hover {{
    background: rgba(255,255,255,0.02);
  }}
  .config-label {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 16px;
    font-weight: 700;
    flex: 1;
    min-width: 0;
  }}
  .config-badge-proto {{
    font-size: 9px;
    padding: 2px 12px;
    border-radius: 30px;
    font-weight: 700;
    background: rgba(168,85,247,0.10);
    color: var(--primary-light);
    white-space: nowrap;
  }}
  .config-status {{
    font-size: 10px;
    font-weight: 700;
    padding: 4px 14px;
    border-radius: 30px;
    display: flex;
    align-items: center;
    gap: 5px;
    white-space: nowrap;
  }}
  .config-status.on {{ background: var(--green-bg); color: var(--green); border: 1px solid rgba(52,211,153,0.2); }}
  .config-status.off {{ background: var(--red-bg); color: var(--red); border: 1px solid rgba(251,113,133,0.2); }}
  .config-toggle {{
    font-size: 22px;
    color: var(--text3);
    transition: transform 0.4s;
  }}
  .config-toggle.open {{ transform: rotate(180deg); }}

  .config-body {{
    padding: 0 22px 22px;
    display: none;
  }}
  .config-body.open {{ display: block; }}

  .usage-bar-wrap {{
    margin: 12px 0 10px;
  }}
  .usage-meta {{
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    color: var(--text3);
    margin-bottom: 6px;
  }}
  .usage-meta b {{ color: var(--text2); }}
  .bar-track {{
    height: 8px;
    border-radius: 10px;
    background: rgba(255,255,255,0.05);
    overflow: hidden;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.3);
  }}
  .bar-fill {{
    height: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    transition: width 0.8s cubic-bezier(0.2,0.9,0.3,1);
    width: 0%;
    box-shadow: 0 0 12px rgba(168,85,247,0.3);
  }}
  .remain-tag {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 10px;
    font-weight: 700;
    padding: 2px 14px;
    border-radius: 30px;
    margin-top: 8px;
  }}
  .remain-tag.ok {{ background: var(--green-bg); color: var(--green); }}
  .remain-tag.warn {{ background: rgba(168,85,247,0.10); color: var(--primary-light); }}
  .remain-tag.danger {{ background: var(--red-bg); color: var(--red); }}

  /* ===== SERVER LIST ===== */
  .server-list {{
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid var(--border);
  }}
  .server-list-title {{
    font-size: 10px;
    font-weight: 700;
    color: var(--text3);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    display: flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 12px;
  }}
  .server-row {{
    background: var(--surface3);
    border-radius: 16px;
    padding: 12px 16px;
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 8px;
    border: 1px solid var(--border);
    transition: all 0.2s;
  }}
  .server-row:hover {{ border-color: var(--border-glow); background: rgba(168,85,247,0.04); }}
  .server-index {{
    font-size: 10px;
    font-weight: 700;
    color: var(--text3);
    min-width: 28px;
  }}
  .server-address {{
    flex: 1;
    font-family: 'Inter', monospace;
    font-size: 10.5px;
    color: var(--text2);
    direction: ltr;
    text-align: left;
    word-break: break-all;
    line-height: 1.6;
    min-width: 0;
  }}
  .btn-copy {{
    font-family: inherit;
    font-size: 10px;
    font-weight: 700;
    padding: 5px 16px;
    border: none;
    border-radius: 30px;
    background: linear-gradient(135deg, var(--primary), var(--primary-dark));
    color: #fff;
    display: flex;
    align-items: center;
    gap: 4px;
    cursor: pointer;
    transition: all 0.2s;
    flex-shrink: 0;
  }}
  .btn-copy:hover {{ transform: scale(1.06); box-shadow: 0 4px 20px rgba(168,85,247,0.3); }}

  /* ===== FOOTER ===== */
  .footer {{
    text-align: center;
    margin-top: 40px;
    padding: 18px 0 4px;
    font-size: 10px;
    color: var(--text3);
    letter-spacing: 0.05em;
    border-top: 1px solid var(--border);
  }}
  .footer a {{
    color: var(--primary-light);
    font-weight: 700;
    text-decoration: none;
    transition: 0.2s;
  }}
  .footer a:hover {{ text-decoration: underline; color: var(--secondary); }}

  /* ===== TOAST ===== */
  .toast {{
    position: fixed;
    bottom: 36px;
    left: 50%;
    transform: translateX(-50%) translateY(80px);
    background: var(--surface2);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 14px 28px;
    font-size: 14px;
    font-weight: 600;
    color: var(--text);
    opacity: 0;
    transition: all 0.5s cubic-bezier(0.2,0.9,0.3,1);
    z-index: 999;
    pointer-events: none;
    display: flex;
    align-items: center;
    gap: 10px;
    box-shadow: 0 16px 50px rgba(0,0,0,0.7);
  }}
  .toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
  .toast.success {{ border-color: rgba(52,211,153,0.3); background: rgba(52,211,153,0.10); color: var(--green); }}

  /* ===== LOADING / EMPTY ===== */
  .state-placeholder {{
    text-align: center;
    padding: 80px 20px;
  }}
  .state-placeholder i {{
    font-size: 56px;
    color: var(--text3);
    display: block;
    margin-bottom: 18px;
    opacity: 0.4;
  }}
  .state-placeholder p {{ font-size: 14px; color: var(--text3); }}
  .spinner i {{
    animation: spin 1.2s linear infinite;
    color: var(--primary-light);
  }}
  @keyframes spin {{ to {{ transform: rotate(360deg); }} }}

  /* ===== RESPONSIVE ===== */
  @media (max-width: 480px) {{
    .stats {{ grid-template-columns: 1fr 1fr; }}
    .stats .stat-item:last-child {{ grid-column: 1 / -1; }}
    .copy-all {{ flex-direction: column; align-items: stretch; text-align: center; }}
    .btn-copy-all {{ justify-content: center; }}
    .config-header {{ flex-wrap: wrap; }}
    .config-label {{ min-width: 100%; }}
  }}
  @media (max-width: 380px) {{
    .stats {{ grid-template-columns: 1fr; }}
    .server-row {{ flex-wrap: wrap; }}
  }}
</style>
</head>
<body>

<!-- Orbs -->
<div class="orb orb1"></div>
<div class="orb orb2"></div>
<div class="orb orb3"></div>

<!-- Toast -->
<div class="toast" id="toast"></div>

<!-- Main -->
<div class="wrap">
  <div class="header">
    <div class="logo-wrap"><i class="ti ti-brand-c-sharp"></i></div>
    <div class="brand">CBeeNet</div>
    <div class="tagline">اشتراک · VPN</div>
    <a class="tele-link" href="https://t.me/CBeeNet" target="_blank">
      <i class="ti ti-brand-telegram"></i> @CBeeNet
    </a>
  </div>

  <div id="root">
    <div class="state-placeholder spinner">
      <i class="ti ti-loader-2"></i>
      <p>در حال دریافت اطلاعات…</p>
    </div>
  </div>

  <div class="footer">
    کانال رسمی <a href="https://t.me/CBeeNet" target="_blank">@CBeeNet</a> · v12
  </div>
</div>

<script>
// ===== CONFIG =====
const API_URL = "{api_url}";
let allLinks = [];

// ===== HELPERS =====
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
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }})[c]);
}}
function protoLabel(protocols) {{
  if (!protocols || !protocols.length) return '<span class="config-badge-proto">VLESS+WS</span>';
  const labels = {{
    'vless-ws': 'VLESS+WS',
    'xhttp-packet-up': 'XHTTP',
    'xhttp-stream-up': 'XHTTP',
    'xhttp-stream-one': 'XHTTP ULTRA'
  }};
  return protocols.map(p => `<span class="config-badge-proto">${{labels[p] || 'VLESS+WS'}}</span>`).join('');
}}

// ===== DATA FETCH =====
async function loadData() {{
  try {{
    const r = await fetch(API_URL);
    if (!r.ok) throw new Error();
    return await r.json();
  }} catch (e) {{
    return null;
  }}
}}

// ===== RENDER =====
function render(d) {{
  const root = document.getElementById('root');
  if (!d || !d.links || !d.links.length) {{
    root.innerHTML = `<div class="state-placeholder">
      <i class="ti ti-link-off"></i>
      <p>کانفیگی یافت نشد</p>
    </div>`;
    return;
  }}
  allLinks = d.links;
  d.links.forEach(l => l._lines = l.vless_link ? l.vless_link.split("\\n").filter(x => x) : []);

  const active = d.links.filter(l => l.active).length;
  const totalUsed = d.links.reduce((s, l) => s + (l.used_bytes || 0), 0);
  let html = '';

  // Info card
  html += `<div class="info-card">
    <div class="glow-spot"></div>
    <div class="info-eyebrow"><i class="ti ti-folder"></i> ${{d.links.length === 1 ? 'کانفیگ' : 'گروه دسترسی'}}</div>
    <div class="info-name">${{esc(d.name || 'CBeeNet')}}</div>
    ${{d.desc ? `<div class="info-desc">${{esc(d.desc)}}</div>` : ''}}
  </div>`;

  // Stats
  html += `<div class="stats">
    <div class="stat-item">
      <div class="stat-label">وضعیت</div>
      <div class="stat-value">${{d.links.length === 1 ? (d.links[0].active ? 'فعال' : 'غیرفعال') : active + '/' + d.links.length}}</div>
      <div class="stat-sub"></div>
    </div>
    <div class="stat-item">
      <div class="stat-label">مصرف کل</div>
      <div class="stat-value">${{fmtB(totalUsed)}}</div>
      <div class="stat-sub">مجموع</div>
    </div>
    <div class="stat-item">
      <div class="stat-label">اتصالات</div>
      <div class="stat-value">${{d.active_connections || 0}}</div>
      <div class="stat-sub"><span class="dot-live"></span> آنلاین</div>
    </div>
  </div>`;

  // Copy all bar
  if (d.links.length > 0) {{
    const allVlessLinks = d.links.map(l => l.vless_link || '').filter(x => x);
    const count = allVlessLinks.length;
    html += `<div class="copy-all">
      <div class="copy-all-text">
        <div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه کانفیگ‌ها</div>
        <div class="copy-all-sub">${{count}} لینک · با یک کلیک</div>
      </div>
      <button class="btn-copy-all" onclick="copyAll()"><i class="ti ti-clipboard-copy"></i> کپی همه (${{count}})</button>
    </div>`;
  }}

  // Config list header
  html += `<div class="section-header"><i class="ti ti-link"></i> کانفیگ‌ها (${{d.links.length}})</div>`;

  // Config items
  for (let i = 0; i < d.links.length; i++) {{
    const l = d.links[i];
    const pct = l.limit_bytes > 0 ? Math.min(100, (l.used_bytes / l.limit_bytes) * 100) : 0;
    const remain = l.limit_bytes > 0 ? Math.max(0, l.limit_bytes - l.used_bytes) : -1;
    const rf = remain < 0 ? '∞' : fmtB(remain);
    const rc = remain < 0 ? 'ok' : (remain < 1048576 ? 'danger' : (remain < 1073741824 ? 'warn' : 'ok'));
    const statusClass = l.active ? 'on' : 'off';
    const statusIcon = l.active ? 'circle-check' : 'circle-x';
    const statusText = l.active ? 'فعال' : 'غیرفعال';
    const protoBadges = l.protocols ? protoLabel(l.protocols) : '<span class="config-badge-proto">VLESS+WS</span>';

    html += `<div class="config-item">
      <div class="config-header" onclick="toggleBody(this)">
        <div class="config-label">
          <span>${{esc(l.label)}}</span>
          ${{protoBadges}}
        </div>
        <span class="config-status ${{statusClass}}"><i class="ti ti-${{statusIcon}}"></i> ${{statusText}}</span>
        <span class="config-toggle"><i class="ti ti-chevron-down"></i></span>
      </div>
      <div class="config-body">
        <div class="usage-bar-wrap">
          <div class="usage-meta">
            <span>مصرف: <b>${{l.used_fmt}}</b></span>
            <span>سهمیه: <b>${{l.limit_fmt}}</b></span>
          </div>
          <div class="bar-track"><div class="bar-fill" style="width:${{pct}}%;"></div></div>
          <span class="remain-tag ${{rc}}"><i class="ti ${{remain < 0 ? 'ti-infinity' : 'ti-database'}}"></i> ${{remain < 0 ? 'نامحدود' : 'باقی: ' + rf}}</span>
        </div>
        ${{l._lines.length ? `<div class="server-list">
          <div class="server-list-title"><i class="ti ti-server-2"></i> سرورهای دسترسی</div>
          ${{l._lines.map((line, j) => `
            <div class="server-row">
              <span class="server-index">#${{j+1}}</span>
              <span class="server-address">${{esc(line)}}</span>
              <button class="btn-copy" onclick="copyText('${{esc(line)}}')"><i class="ti ti-copy"></i> کپی</button>
            </div>
          `).join('')}}
        </div>` : ''}}
      </div>
    </div>`;
  }}

  root.innerHTML = html;
}}

// ===== TOGGLE =====
function toggleBody(headerEl) {{
  const body = headerEl.nextElementSibling;
  const toggle = headerEl.querySelector('.config-toggle');
  body.classList.toggle('open');
  toggle.classList.toggle('open');
}}

// ===== COPY =====
function copyText(t) {{
  navigator.clipboard.writeText(t).then(() => {{
    showToast('✅ کپی شد', 'success');
  }});
}}
function copyAll() {{
  const all = allLinks.map(l => l.vless_link || '').filter(x => x).join('\\n');
  if (!all) {{
    showToast('❌ لینکی برای کپی نیست', '');
    return;
  }}
  navigator.clipboard.writeText(all).then(() => {{
    showToast('✅ همه ' + allLinks.length + ' کانفیگ کپی شد', 'success');
  }});
}}
function showToast(msg, type = '') {{
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast show ' + (type || '');
  clearTimeout(t._hide);
  t._hide = setTimeout(() => t.classList.remove('show'), 2000);
}}

// ===== INIT =====
(async function init() {{
  const data = await loadData();
  if (data) {{
    render(data);
  }} else {{
    document.getElementById('root').innerHTML = `
      <div class="state-placeholder">
        <i class="ti ti-alert-circle" style="color:var(--red)"></i>
        <p>خطا در بارگذاری</p>
      </div>
    `;
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
