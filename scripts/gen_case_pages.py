#!/usr/bin/env python3
"""Generate the case-study library: cases/<slug>/index.html + cases/index.html
from _data/cases.yml.

Follows the gen_skill_pages.py pattern; visual shell reused from
skills/kol-outreach/index.html. Each case page gets its own <title>, meta
description, canonical, OpenGraph/Twitter cards, JSON-LD (Article +
BreadcrumbList), related-skill internal links, a /services/ CTA, and
prev/next navigation.

Hard rule: no consulting-client project names anywhere — only AFFiNE
(Iris's own company) may be named. Data lives in _data/cases.yml.

Usage:  python3 scripts/gen_case_pages.py
"""
import os, json, html, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://gingiris.tools"
DATE_PUBLISHED = "2026-07-07"

def load_cases():
    path = os.path.join(ROOT, "_data", "cases.yml")
    try:
        import yaml
        return yaml.safe_load(open(path, encoding="utf-8"))
    except ImportError:
        sys.exit("PyYAML not found. Run: pip install pyyaml")

AUTHOR = {
    "@type": "Person", "name": "Iris Wei", "alternateName": "生姜",
    "url": SITE, "sameAs": ["https://x.com/WeiYipei",
    "https://www.linkedin.com/in/yipei-wei-550825105/", "https://huggingface.co/Gingiris"],
}
PUBLISHER = {
    "@type": "Organization", "name": "Gingiris Growth Tools", "url": SITE,
    "logo": {"@type": "ImageObject", "url": f"{SITE}/logo.jpg"},
}

STYLE = """  * { margin:0; padding:0; box-sizing:border-box; }
  :root {
    --bg:#f8f7f4; --surface:#ffffff; --surface-hover:#f3f2ef;
    --border:#e8e6e1; --border-hover:#c8c5be;
    --text:#1a1a1a; --text-secondary:#6b6860; --text-muted:#9b9890;
    --accent:#16a34a; --accent-hover:#15803d;
    --code-bg:#1f2937; --code-text:#e5e7eb;
  }
  body { font-family:'Inter','Noto Sans SC',-apple-system,BlinkMacSystemFont,sans-serif; background:var(--bg); color:var(--text); line-height:1.6; -webkit-font-smoothing:antialiased; }
  .container { max-width:1200px; margin:0 auto; padding:0 24px; }
  .narrow { max-width:760px; margin:0 auto; }
  a { color:inherit; }
  /* Header */
  .site-nav { background:var(--surface); border-bottom:1px solid var(--border); padding:14px 0; position:sticky; top:0; z-index:10; }
  .site-nav .container { display:flex; justify-content:space-between; align-items:center; }
  .site-nav a.logo { font-weight:800; font-size:18px; color:var(--text); text-decoration:none; }
  .site-nav .nav-links { display:flex; gap:24px; font-size:14px; }
  .site-nav .nav-links a { color:var(--text-secondary); text-decoration:none; }
  .site-nav .nav-links a:hover { color:var(--accent); }
  /* Breadcrumb */
  .crumbs { font-size:13px; color:var(--text-muted); padding:20px 0 0; }
  .crumbs a { color:var(--text-secondary); text-decoration:none; }
  .crumbs a:hover { color:var(--accent); }
  /* Hero */
  .hero { padding:40px 0 8px; text-align:center; }
  .hero h1 { font-size:clamp(28px,5vw,44px); font-weight:800; line-height:1.15; letter-spacing:-0.02em; margin-bottom:16px; }
  .hero .tag-line { font-size:18px; color:var(--text-secondary); margin:0 auto 28px; max-width:660px; }
  .case-meta { display:inline-flex; flex-wrap:wrap; justify-content:center; gap:8px; }
  .case-meta span { display:inline-block; background:var(--surface); border:1px solid var(--border); border-radius:999px; padding:5px 14px; font-size:13px; color:var(--text-secondary); }
  .case-meta span.hl { border-color:var(--accent); color:var(--accent-hover); font-weight:600; }
  .credentials { font-size:14px; color:var(--text-muted); margin-top:14px; }
  .credentials strong { color:var(--accent); }
  /* Sections */
  section { padding:40px 0 0; }
  section h2 { font-size:24px; font-weight:800; letter-spacing:-0.01em; margin-bottom:16px; }
  section p.body { font-size:16px; color:var(--text-secondary); }
  .anon-note { border-left:3px solid #f59e0b; padding-left:12px; margin-top:12px; font-size:14px; color:var(--text-muted); }
  /* Key results card */
  .stats { background:var(--surface); border:1px solid var(--border); border-radius:12px; padding:8px 22px; }
  .stats table { width:100%; border-collapse:collapse; font-size:15px; }
  .stats td { padding:13px 0; border-bottom:1px solid var(--border); }
  .stats tr:last-child td { border-bottom:none; }
  .stats td.v { text-align:right; font-weight:700; }
  /* Key takeaways */
  .takeaways { background:#f0fdf4; border:1px solid #bbf7d0; border-left:4px solid var(--accent); border-radius:10px; padding:20px 24px; margin-top:8px; }
  .takeaways h2 { font-size:15px; text-transform:uppercase; letter-spacing:0.04em; color:var(--accent-hover); margin-bottom:10px; }
  .takeaways ul { margin:0; padding-left:20px; }
  .takeaways li { font-size:15.5px; color:var(--text); padding:5px 0; line-height:1.55; }
  /* Steps */
  ol.steps { list-style:none; counter-reset:none; padding:0; margin:0; }
  ol.steps .step { display:flex; gap:16px; padding:18px 0; border-bottom:1px solid var(--border); }
  ol.steps .step:last-child { border-bottom:none; }
  .step-n { flex:0 0 30px; height:30px; width:30px; border-radius:50%; background:var(--accent); color:#fff; font-weight:700; font-size:14px; display:flex; align-items:center; justify-content:center; }
  .step-t { font-weight:700; font-size:16px; margin-bottom:4px; }
  .step-d { font-size:15px; color:var(--text-secondary); line-height:1.6; }
  /* CTA */
  .cta-block { background:var(--code-bg); color:var(--code-text); border-radius:12px; padding:28px 26px; text-align:center; margin-top:8px; }
  .cta-block p { font-size:16px; margin-bottom:16px; }
  .cta-block a.btn { display:inline-block; background:var(--accent); color:#fff; text-decoration:none; font-weight:700; font-size:15px; padding:11px 26px; border-radius:8px; transition:background .15s; }
  .cta-block a.btn:hover { background:var(--accent-hover); }
  /* Related cards */
  .rel-grid { display:grid; gap:12px; }
  .rel-card { display:flex; justify-content:space-between; align-items:center; gap:12px; background:var(--surface); border:1px solid var(--border); border-radius:10px; padding:16px 18px; text-decoration:none; color:var(--text); font-weight:600; font-size:15px; transition:border-color .15s, transform .15s; }
  .rel-card:hover { border-color:var(--accent); transform:translateY(-1px); }
  .rel-card .arr { color:var(--accent); }
  /* Prev / next */
  .pn-nav { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:40px; }
  .pn-nav a { background:var(--surface); border:1px solid var(--border); border-radius:10px; padding:14px 18px; text-decoration:none; transition:border-color .15s; }
  .pn-nav a:hover { border-color:var(--accent); }
  .pn-nav .pn-label { display:block; font-size:12px; color:var(--text-muted); margin-bottom:4px; }
  .pn-nav .pn-title { font-size:14px; font-weight:600; color:var(--text); }
  .pn-nav a.next { text-align:right; }
  .pn-nav .spacer { visibility:hidden; }
  /* Index: hero stats bar */
  .hero-stats { display:grid; grid-template-columns:repeat(4,1fr); gap:12px; max-width:760px; margin:28px auto 0; }
  .hero-stats .hs { background:var(--surface); border:1px solid var(--border); border-radius:12px; padding:16px 10px; text-align:center; }
  .hero-stats .hs b { display:block; font-size:24px; font-weight:800; color:var(--accent-hover); }
  .hero-stats .hs span { font-size:12.5px; color:var(--text-secondary); }
  /* Index: case cards */
  .case-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:16px; margin-top:8px; }
  .case-card { display:flex; flex-direction:column; gap:8px; background:var(--surface); border:1px solid var(--border); border-radius:12px; padding:20px 22px; text-decoration:none; color:var(--text); transition:border-color .15s, transform .15s; }
  .case-card:hover { border-color:var(--accent); transform:translateY(-2px); }
  .case-card .cc-cat { font-size:12px; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.04em; }
  .case-card .cc-title { font-size:17px; font-weight:700; line-height:1.4; }
  .case-card .cc-sum { font-size:14px; color:var(--text-secondary); line-height:1.55; flex:1; }
  .case-card .cc-stat { font-size:14px; font-weight:700; color:var(--accent-hover); }
  .case-card .cc-stat .arr { float:right; color:var(--accent); }
  /* Footer */
  .site-footer { padding:40px 0; border-top:1px solid var(--border); margin-top:56px; text-align:center; font-size:14px; color:var(--text-muted); }
  .site-footer a { color:var(--text-secondary); text-decoration:none; margin:0 8px; }
  .site-footer a:hover { color:var(--accent); }
  @media (max-width:640px) {
    .container { padding:0 14px; }
    .site-nav .nav-links { gap:14px; font-size:12px; overflow-x:auto; white-space:nowrap; }
    .hero { padding:24px 0 4px; }
    .hero-stats { grid-template-columns:repeat(2,1fr); }
    .case-grid { grid-template-columns:1fr; }
    .pn-nav { grid-template-columns:1fr; }
  }"""

NAV = """  <nav class="site-nav">
    <div class="container">
      <a href="/" class="logo">Gingiris Growth Tools</a>
      <div class="nav-links">
        <a href="/blog/">Blog</a>
        <a href="/tools/">Free Tools</a>\n                <a href="/cases/">Cases</a>\n                <a href="/services/">Services</a>
        <a href="/skills/">Skills</a>
        <a href="/cases/" style="color:var(--accent)">Cases</a>
        <a href="/services/">Services</a>
      </div>
    </div>
  </nav>"""

FOOTER = """  <footer class="site-footer">
    <div class="container">
      <p>
        <a href="https://huggingface.co/datasets/Gingiris" target="_blank" rel="noopener">Hugging Face</a> ·
        <a href="https://dev.to/iris1031" target="_blank" rel="noopener">Dev.to</a> ·
        <a href="https://x.com/WeiYipei" target="_blank" rel="noopener">X / Twitter</a> ·
        <a href="/blog/">Blog</a> ·
        <a href="/services/">咨询服务</a>
      </p>
      <p style="margin-top:12px">© Iris (生姜iris) · 数据均来自真实项目复盘，可访谈核证</p>
    </div>
  </footer>"""

ANON_NOTE = ("依保密约定，本案例客户名已匿名处理；所有数据均来自真实项目复盘，"
             "口径与数字未做修饰，可在咨询访谈中核证。")

CREDENTIALS = ('By <strong>Iris Wei (生姜)</strong> · ex-COO of AFFiNE (60K+ GitHub stars)'
               ' · 30× Product Hunt #1 · 105+ 项目实战')


def head(title, description, keywords, url, og_title, og_desc, ld, lang="zh-CN"):
    return f"""<!DOCTYPE html>
<html lang="{lang}" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="keywords" content="{html.escape(keywords)}">
<meta name="author" content="Iris Wei">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="zh" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(og_title)}">
<meta property="og:description" content="{html.escape(og_desc)}">
<meta property="og:image" content="{SITE}/assets/images/og-banner.jpg">
<meta property="og:site_name" content="Gingiris Growth Tools">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(og_title)}">
<meta name="twitter:description" content="{html.escape(og_desc)}">
<meta name="twitter:image" content="{SITE}/assets/images/og-banner.jpg">
<meta name="twitter:creator" content="@WeiYipei">
<script type="application/ld+json">
{ld}
</script>
<style>
{STYLE}
</style>
</head>"""


def jsonld_case(c):
    url = f"{SITE}/cases/{c['slug']}/"
    article = {
        "@type": "Article",
        "headline": c["h1"],
        "description": c["meta_description"],
        "inLanguage": "zh-CN",
        "url": url,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "image": f"{SITE}/assets/images/og-banner.jpg",
        "datePublished": DATE_PUBLISHED,
        "dateModified": DATE_PUBLISHED,
        "author": AUTHOR,
        "publisher": PUBLISHER,
        "keywords": c["keywords"],
        "articleSection": c["category"],
    }
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "实战案例库", "item": f"{SITE}/cases/"},
        {"@type": "ListItem", "position": 3, "name": c["h1"], "item": url}]}
    graph = {"@context": "https://schema.org", "@graph": [article, crumbs]}
    return json.dumps(graph, ensure_ascii=False, indent=2)


def jsonld_index(cases):
    url = f"{SITE}/cases/"
    page = {
        "@type": "CollectionPage",
        "name": "Gingiris 实战案例库 — 12 个增长复盘",
        "description": "105+ 项目实战中的 12 个代表性复盘：开源增长、发布战役、渠道归因、2B 商业化。除 AFFiNE 外全部匿名，数据全真。",
        "inLanguage": "zh-CN", "url": url,
        "author": AUTHOR, "publisher": PUBLISHER,
        "mainEntity": {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": c["h1"],
             "url": f"{SITE}/cases/{c['slug']}/"}
            for i, c in enumerate(cases)]},
    }
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "实战案例库", "item": url}]}
    graph = {"@context": "https://schema.org", "@graph": [page, crumbs]}
    return json.dumps(graph, ensure_ascii=False, indent=2)


def render_case(c, prev_c, next_c):
    url = f"{SITE}/cases/{c['slug']}/"
    takeaways = "\n".join(f'          <li>{t}</li>' for t in c["takeaways"])
    stats = "\n".join(
        f'        <tr><td>{html.escape(k)}</td><td class="v">{html.escape(v)}</td></tr>'
        for k, v in c["stats"])
    moves = "\n".join(
        f'        <li class="step"><span class="step-n">{i+1}</span><div>'
        f'<p class="step-t">{m["name"]}</p><p class="step-d">{m["text"]}</p></div></li>'
        for i, m in enumerate(c["moves"]))
    related = "\n".join(
        f'          <a class="rel-card" href="{u}"><span>{t}</span><span class="arr">&rarr;</span></a>'
        for t, u in c["related"])
    anon = (f'\n      <p class="anon-note">{ANON_NOTE}</p>' if c.get("anon") else "")
    prev_html = (
        f'      <a class="prev" href="/cases/{prev_c["slug"]}/"><span class="pn-label">&larr; 上一篇</span>'
        f'<span class="pn-title">{html.escape(prev_c["h1"])}</span></a>'
        if prev_c else '      <span class="spacer"></span>')
    next_html = (
        f'      <a class="next" href="/cases/{next_c["slug"]}/"><span class="pn-label">下一篇 &rarr;</span>'
        f'<span class="pn-title">{html.escape(next_c["h1"])}</span></a>'
        if next_c else '      <span class="spacer"></span>')
    return f"""{head(c['title'], c['meta_description'], c['keywords'], url,
                     c['h1'], c['tagline'], jsonld_case(c))}
<body>
{NAV}

  <div class="container">
    <nav class="crumbs"><a href="/">Home</a> / <a href="/cases/">实战案例库</a> / {html.escape(c['name'])}</nav>
  </div>

  <header class="hero">
    <div class="container narrow">
      <h1>{html.escape(c['h1'])}</h1>
      <p class="tag-line">{c['tagline']}</p>
      <div class="case-meta">
        <span>{html.escape(c['category'])}</span>
        <span>{html.escape(c['year'])}</span>
        <span class="hl">{html.escape(c['card_stat'])}</span>
      </div>
      <p class="credentials">{CREDENTIALS}</p>
    </div>
  </header>

  <div class="container narrow">
    <section>
      <div class="takeaways">
        <h2>关键要点</h2>
        <ul>
{takeaways}
        </ul>
      </div>
    </section>

    <section>
      <h2>背景与挑战</h2>
      <p class="body">{c['challenge']}</p>{anon}
    </section>

    <section>
      <h2>关键数据</h2>
      <div class="stats"><table><tbody>
{stats}
      </tbody></table></div>
    </section>

    <section>
      <h2>打法拆解</h2>
      <ol class="steps">
{moves}
      </ol>
    </section>

    <section>
      <h2>结果与沉淀</h2>
      <p class="body">{c['result']}</p>
    </section>

    <section>
      <div class="cta-block">
        <p>想把这套打法用在你的项目上？单次咨询、增长陪跑或 AI 增长员工搭建包。</p>
        <a class="btn" href="/services/">查看咨询服务 &rarr;</a>
      </div>
    </section>

    <section>
      <h2>相关阅读</h2>
      <div class="rel-grid">
{related}
          <a class="rel-card" href="/services/"><span>咨询服务 — 把打法装进你的团队</span><span class="arr">&rarr;</span></a>
          <a class="rel-card" href="/cases/"><span>返回实战案例库（全部 12 篇）</span><span class="arr">&rarr;</span></a>
      </div>
    </section>

    <nav class="pn-nav">
{prev_html}
{next_html}
    </nav>
  </div>

{FOOTER}
</body>
</html>
"""


def render_index(cases):
    url = f"{SITE}/cases/"
    title = "实战案例库 — 105+ 项目中的 12 个增长复盘（数据全真） | Gingiris"
    desc = ("Gingiris 实战案例库：105+ 项目实战中的 12 个代表性复盘——开源增长、发布战役、"
            "渠道归因、2B 商业化。除 AFFiNE 外全部匿名处理，数据全部真实可核证。")
    keywords = ("增长案例, 出海案例, 开源增长, Product Hunt, KOL 营销, 渠道归因, "
                "2B 商业化, AI 产品增长, growth case study")
    cards = "\n".join(
        f'''        <a class="case-card" href="/cases/{c['slug']}/">
          <span class="cc-cat">{html.escape(c['category'])} · {html.escape(c['year'])}</span>
          <span class="cc-title">{html.escape(c['h1'])}</span>
          <span class="cc-sum">{c['card_summary']}</span>
          <span class="cc-stat">{html.escape(c['card_stat'])}<span class="arr">&rarr;</span></span>
        </a>''' for c in cases)
    return f"""{head(title, desc, keywords, url,
                     "Gingiris 实战案例库 — 12 个增长复盘",
                     "105+ 项目 · 12 个匿名实战复盘 · 数据全真", jsonld_index(cases))}
<body>
{NAV}

  <div class="container">
    <nav class="crumbs"><a href="/">Home</a> / 实战案例库</nav>
  </div>

  <header class="hero">
    <div class="container narrow">
      <h1>实战案例库</h1>
      <p class="tag-line">105+ 项目 · 12 个匿名实战复盘 · 数据全真。除 AFFiNE（我自己的公司）外，
      案例一律依保密约定匿名处理——名字可以隐去，数字一个不改。</p>
      <div class="hero-stats">
        <div class="hs"><b>105+</b><span>服务过的项目（2024–2026）</span></div>
        <div class="hs"><b>30×</b><span>Product Hunt 日榜第一</span></div>
        <div class="hs"><b>60,000+</b><span>AFFiNE 开源 star（24 个月）</span></div>
        <div class="hs"><b>400+</b><span>深聊过的 AI 创业团队</span></div>
      </div>
      <p class="credentials">{CREDENTIALS}</p>
    </div>
  </header>

  <div class="container narrow">
    <section>
      <div class="case-grid">
{cards}
      </div>
    </section>

    <section>
      <div class="cta-block">
        <p>这些复盘背后的判断力，可以直接为你的项目所用——单次咨询、增长陪跑或 AI 增长员工搭建包。</p>
        <a class="btn" href="/services/">查看咨询服务 &rarr;</a>
      </div>
    </section>
  </div>

{FOOTER}
</body>
</html>
"""


def main():
    cases = load_cases()
    out = []
    for i, c in enumerate(cases):
        d = os.path.join(ROOT, "cases", c["slug"])
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, "index.html")
        prev_c = cases[i - 1] if i > 0 else None
        next_c = cases[i + 1] if i < len(cases) - 1 else None
        open(p, "w", encoding="utf-8").write(render_case(c, prev_c, next_c))
        out.append(f"/cases/{c['slug']}/  ->  {p}")
    idx = os.path.join(ROOT, "cases", "index.html")
    open(idx, "w", encoding="utf-8").write(render_index(cases))
    out.append(f"/cases/  ->  {idx}")
    print(f"Generated {len(out)} case pages:")
    for o in out:
        print("  " + o)

if __name__ == "__main__":
    main()
