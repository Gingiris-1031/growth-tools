#!/usr/bin/env python3
"""Generate per-skill landing pages at skills/<slug>/index.html from _data/skills.yml.

On-site SEO/GEO: each page gets its own <title>, meta description, canonical, hreflang,
OpenGraph/Twitter cards, and JSON-LD (SoftwareApplication + FAQPage + BreadcrumbList),
plus topic-cluster internal links and a single install CTA.

Usage:  python3 scripts/gen_skill_pages.py
"""
import os, json, html, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://gingiris.tools"

def load_skills():
    path = os.path.join(ROOT, "_data", "skills.yml")
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

def jsonld(s):
    url = f"{SITE}/skills/{s['slug']}/"
    soft = {
        "@type": "SoftwareApplication", "name": s["h1"],
        "applicationCategory": s.get("app_category", "BusinessApplication"),
        "applicationSubCategory": "Claude Skill",
        "operatingSystem": "Any (Claude Code, Cursor, Codex, Cline)",
        "description": s["software_description"], "url": url,
        "downloadUrl": f"https://huggingface.co/datasets/Gingiris/{s['hf']}",
        "installUrl": f"https://skills.sh/{s['install']}",
        "license": "https://opensource.org/licenses/MIT",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "author": AUTHOR, "keywords": s["keywords"],
    }
    howto = {"@type": "HowTo", "name": s["howto"]["title"],
        "step": [{"@type": "HowToStep", "position": i + 1, "name": st["name"],
                  "text": html.unescape(st["text"])}
                 for i, st in enumerate(s["howto"]["steps"])]}
    faq = {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": html.unescape(f["q"]),
         "acceptedAnswer": {"@type": "Answer", "text": html.unescape(f["a"])}}
        for f in s["faqs"]]}
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Skills", "item": f"{SITE}/skills/"},
        {"@type": "ListItem", "position": 2, "name": s["h1"], "item": url}]}
    graph = {"@context": "https://schema.org", "@graph": [soft, howto, faq, crumbs]}
    return json.dumps(graph, ensure_ascii=False, indent=2)

def render(s):
    url = f"{SITE}/skills/{s['slug']}/"
    stats = "\n".join(
        f'        <tr><td>{html.escape(k)}</td><td class="v">{html.escape(v)}</td></tr>'
        for k, v in s["stats"])
    faqs = "\n".join(
        f'        <div class="faq-item"><p class="faq-q">{f["q"]}</p><p class="faq-a">{f["a"]}</p></div>'
        for f in s["faqs"])
    related = "\n".join(
        f'          <a class="rel-card" href="{u}"><span>{t}</span><span class="arr">&rarr;</span></a>'
        for t, u in s["related"])
    takeaways = "\n".join(f'          <li>{t}</li>' for t in s["takeaways"])
    notice_html = (
        f'\n      <p class="body" style="border-left:3px solid #f59e0b;'
        f'padding-left:12px;margin-top:12px;">{s["notice"]}</p>'
        if s.get("notice") else "")
    steps = "\n".join(
        f'        <li class="step"><span class="step-n">{i+1}</span><div>'
        f'<p class="step-t">{st["name"]}</p><p class="step-d">{st["text"]}</p></div></li>'
        for i, st in enumerate(s["howto"]["steps"]))
    cmp = s["compare"]
    cmp_head = "".join(f"<th>{c}</th>" for c in cmp["columns"])
    cmp_body = "\n".join(
        "        <tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>"
        for row in cmp["rows"])
    donts = "\n".join(f'          <li>{d}</li>' for d in s["donts"]["items"])
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(s['title'])}</title>
<meta name="description" content="{html.escape(s['meta_description'])}">
<meta name="keywords" content="{html.escape(s['keywords'])}">
<meta name="author" content="Iris Wei">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(s['h1'])}">
<meta property="og:description" content="{html.escape(s['tagline'])}">
<meta property="og:image" content="{SITE}/assets/images/og-banner.jpg">
<meta property="og:site_name" content="Gingiris Growth Tools">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(s['h1'])}">
<meta name="twitter:description" content="{html.escape(s['tagline'])}">
<meta name="twitter:image" content="{SITE}/assets/images/og-banner.jpg">
<meta name="twitter:creator" content="@WeiYipei">
<script type="application/ld+json">
{jsonld(s)}
</script>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  :root {{
    --bg:#f8f7f4; --surface:#ffffff; --surface-hover:#f3f2ef;
    --border:#e8e6e1; --border-hover:#c8c5be;
    --text:#1a1a1a; --text-secondary:#6b6860; --text-muted:#9b9890;
    --accent:#16a34a; --accent-hover:#15803d;
    --code-bg:#1f2937; --code-text:#e5e7eb;
  }}
  body {{ font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif; background:var(--bg); color:var(--text); line-height:1.6; -webkit-font-smoothing:antialiased; }}
  .container {{ max-width:1200px; margin:0 auto; padding:0 24px; }}
  .narrow {{ max-width:760px; margin:0 auto; }}
  a {{ color:inherit; }}
  /* Header */
  .site-nav {{ background:var(--surface); border-bottom:1px solid var(--border); padding:14px 0; position:sticky; top:0; z-index:10; }}
  .site-nav .container {{ display:flex; justify-content:space-between; align-items:center; }}
  .site-nav a.logo {{ font-weight:800; font-size:18px; color:var(--text); text-decoration:none; }}
  .site-nav .nav-links {{ display:flex; gap:24px; font-size:14px; }}
  .site-nav .nav-links a {{ color:var(--text-secondary); text-decoration:none; }}
  .site-nav .nav-links a:hover {{ color:var(--accent); }}
  /* Breadcrumb */
  .crumbs {{ font-size:13px; color:var(--text-muted); padding:20px 0 0; }}
  .crumbs a {{ color:var(--text-secondary); text-decoration:none; }}
  .crumbs a:hover {{ color:var(--accent); }}
  /* Hero */
  .hero {{ padding:40px 0 8px; text-align:center; }}
  .hero h1 {{ font-size:clamp(28px,5vw,44px); font-weight:800; line-height:1.15; letter-spacing:-0.02em; margin-bottom:16px; }}
  .hero .tag-line {{ font-size:18px; color:var(--text-secondary); margin:0 auto 28px; max-width:660px; }}
  .meta-install {{ display:inline-flex; align-items:center; gap:10px; background:var(--code-bg); color:var(--code-text); font-family:'JetBrains Mono',monospace; font-size:15px; padding:12px 14px 12px 20px; border-radius:8px; }}
  .meta-install b {{ color:#4ade80; font-weight:500; }}
  .copy-btn {{ background:transparent; border:1px solid #374151; color:var(--code-text); font:inherit; font-size:13px; padding:5px 11px; border-radius:6px; cursor:pointer; transition:background .15s; }}
  .copy-btn:hover {{ background:#374151; }}
  .copy-btn.copied {{ background:var(--accent); border-color:var(--accent); }}
  .credentials {{ font-size:14px; color:var(--text-muted); margin-top:14px; }}
  .credentials strong {{ color:var(--accent); }}
  /* Sections */
  section {{ padding:40px 0 0; }}
  section h2 {{ font-size:24px; font-weight:800; letter-spacing:-0.01em; margin-bottom:16px; }}
  section p.body {{ font-size:16px; color:var(--text-secondary); }}
  /* Key results card */
  .stats {{ background:var(--surface); border:1px solid var(--border); border-radius:12px; padding:8px 22px; }}
  .stats table {{ width:100%; border-collapse:collapse; font-size:15px; }}
  .stats td {{ padding:13px 0; border-bottom:1px solid var(--border); }}
  .stats tr:last-child td {{ border-bottom:none; }}
  .stats td.v {{ text-align:right; font-weight:700; }}
  /* Key takeaways */
  .takeaways {{ background:#f0fdf4; border:1px solid #bbf7d0; border-left:4px solid var(--accent); border-radius:10px; padding:20px 24px; margin-top:8px; }}
  .takeaways h2 {{ font-size:15px; text-transform:uppercase; letter-spacing:0.04em; color:var(--accent-hover); margin-bottom:10px; }}
  .takeaways ul {{ margin:0; padding-left:20px; }}
  .takeaways li {{ font-size:15.5px; color:var(--text); padding:5px 0; line-height:1.55; }}
  /* HowTo steps */
  ol.steps {{ list-style:none; counter-reset:none; padding:0; margin:0; }}
  ol.steps .step {{ display:flex; gap:16px; padding:18px 0; border-bottom:1px solid var(--border); }}
  ol.steps .step:last-child {{ border-bottom:none; }}
  .step-n {{ flex:0 0 30px; height:30px; width:30px; border-radius:50%; background:var(--accent); color:#fff; font-weight:700; font-size:14px; display:flex; align-items:center; justify-content:center; }}
  .step-t {{ font-weight:700; font-size:16px; margin-bottom:4px; }}
  .step-d {{ font-size:15px; color:var(--text-secondary); line-height:1.6; }}
  /* Comparison table */
  .cmp-intro {{ font-size:15px; color:var(--text-secondary); margin-bottom:14px; }}
  .cmp {{ width:100%; border-collapse:collapse; font-size:15px; background:var(--surface); border:1px solid var(--border); border-radius:12px; overflow:hidden; }}
  .cmp th {{ text-align:left; background:var(--surface-hover); font-weight:700; padding:12px 18px; border-bottom:1px solid var(--border); }}
  .cmp td {{ padding:12px 18px; border-bottom:1px solid var(--border); }}
  .cmp tr:last-child td {{ border-bottom:none; }}
  .cmp td:nth-child(2) {{ font-weight:700; color:var(--accent-hover); white-space:nowrap; }}
  /* Don'ts */
  ul.donts {{ list-style:none; padding:0; margin:0; }}
  ul.donts li {{ position:relative; padding:10px 0 10px 30px; border-bottom:1px solid var(--border); font-size:15px; color:var(--text-secondary); }}
  ul.donts li:last-child {{ border-bottom:none; }}
  ul.donts li::before {{ content:'✕'; position:absolute; left:4px; color:#dc2626; font-weight:700; }}
  /* FAQ */
  .faq-item {{ padding:20px 0; border-bottom:1px solid var(--border); }}
  .faq-item:last-child {{ border-bottom:none; }}
  .faq-q {{ font-size:17px; font-weight:600; margin-bottom:8px; }}
  .faq-q::before {{ content:'Q '; color:var(--accent); font-weight:700; }}
  .faq-a {{ font-size:15px; color:var(--text-secondary); line-height:1.65; }}
  /* Related cards */
  .rel-grid {{ display:grid; gap:12px; }}
  .rel-card {{ display:flex; justify-content:space-between; align-items:center; gap:12px; background:var(--surface); border:1px solid var(--border); border-radius:10px; padding:16px 18px; text-decoration:none; color:var(--text); font-weight:600; font-size:15px; transition:border-color .15s, transform .15s; }}
  .rel-card:hover {{ border-color:var(--accent); transform:translateY(-1px); }}
  .rel-card .arr {{ color:var(--accent); }}
  /* Footer */
  .site-footer {{ padding:40px 0; border-top:1px solid var(--border); margin-top:56px; text-align:center; font-size:14px; color:var(--text-muted); }}
  .site-footer a {{ color:var(--text-secondary); text-decoration:none; margin:0 8px; }}
  .site-footer a:hover {{ color:var(--accent); }}
  @media (max-width:640px) {{
    .container {{ padding:0 14px; }}
    .site-nav .nav-links {{ gap:14px; font-size:12px; overflow-x:auto; white-space:nowrap; }}
    .hero {{ padding:24px 0 4px; }}
    .meta-install {{ font-size:13px; max-width:100%; overflow-x:auto; }}
  }}
</style>
</head>
<body>
  <nav class="site-nav">
    <div class="container">
      <a href="/" class="logo">Gingiris Growth Tools</a>
      <div class="nav-links">
        <a href="/blog/">Blog</a>
        <a href="/tools/">Free Tools</a>\n                <a href="/cases/">Cases</a>\n                <a href="/services/">Services</a>\n                <a href="/playbook/2b-deals/">Playbook</a>
        <a href="/skills/" style="color:var(--accent)">Skills</a>
        <a href="https://huggingface.co/datasets/Gingiris" target="_blank" rel="noopener">HuggingFace &rarr;</a>
      </div>
    </div>
  </nav>

  <div class="container">
    <nav class="crumbs"><a href="/">Home</a> / <a href="/skills/">Skills</a> / {html.escape(s['h1'])}</nav>
  </div>

  <header class="hero">
    <div class="container narrow">
      <h1>{html.escape(s['h1'])}</h1>
      <p class="tag-line">{s['tagline']}</p>
      <div class="meta-install" id="install">
        <span>npx skills add <b>{s['install']}</b></span>
        <button class="copy-btn" onclick="navigator.clipboard.writeText('npx skills add {s['install']}');this.classList.add('copied');this.textContent='✓ copied'">copy</button>
      </div>
      <p class="credentials">By <strong>Iris Wei (生姜)</strong> · ex-COO of AFFiNE (60K+ GitHub stars) · 30× Product Hunt #1</p>
    </div>
  </header>

  <div class="container narrow">
    <section>
      <div class="takeaways">
        <h2>Key takeaways</h2>
        <ul>
{takeaways}
        </ul>
      </div>
    </section>

    <section>
      <h2>What this is</h2>
      <p class="body">{s['what']}</p>{notice_html}
    </section>

    <section>
      <h2>Key results</h2>
      <div class="stats"><table><tbody>
{stats}
      </tbody></table></div>
    </section>

    <section>
      <h2>{s['howto']['title']}</h2>
      <ol class="steps">
{steps}
      </ol>
    </section>

    <section>
      <h2>{cmp['title']}</h2>
      <p class="cmp-intro">{cmp['intro']}</p>
      <table class="cmp">
        <thead><tr>{cmp_head}</tr></thead>
        <tbody>
{cmp_body}
        </tbody>
      </table>
    </section>

    <section>
      <h2>{s['donts']['title']}</h2>
      <ul class="donts">
{donts}
      </ul>
    </section>

    <section>
      <h2>FAQ</h2>
{faqs}
    </section>

    <section>
      <h2>Related playbooks</h2>
      <div class="rel-grid">
{related}
          <a class="rel-card" href="/skills/"><span>Browse all 60 playbooks</span><span class="arr">&rarr;</span></a>
          <a class="rel-card" href="/"><span>Find a growth tool for live data or execution</span><span class="arr">&rarr;</span></a>
          <a class="rel-card" href="/services/"><span>Get Gingiris advisory or a custom AI growth employee</span><span class="arr">&rarr;</span></a>
      </div>
    </section>
  </div>

  <footer class="site-footer">
    <div class="container">
      <p>
        <a href="https://huggingface.co/datasets/Gingiris/{s['hf']}" target="_blank" rel="noopener">Hugging Face</a> ·
        <a href="https://dev.to/iris1031" target="_blank" rel="noopener">Dev.to</a> ·
        <a href="https://x.com/WeiYipei" target="_blank" rel="noopener">X / Twitter</a> ·
        <a href="/blog/">Blog</a>
      </p>
      <p style="margin-top:12px">© Iris (生姜iris) · Community skill licensed under MIT · Hosted services separate</p>
    </div>
  </footer>
</body>
</html>
"""

def main():
    skills = load_skills()
    out = []
    for s in skills:
        d = os.path.join(ROOT, "skills", s["slug"])
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, "index.html")
        open(p, "w", encoding="utf-8").write(render(s))
        out.append(f"/skills/{s['slug']}/  ->  {p}")
    print(f"Generated {len(out)} skill pages:")
    for o in out:
        print("  " + o)

if __name__ == "__main__":
    main()
