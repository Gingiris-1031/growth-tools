// Local-only OG image generator for gingiris.tools blog posts.
// Satori (layout) -> SVG -> resvg -> PNG (1200x630). Run: node generate-og.mjs [--all] [--slug=foo]
// Fonts + node_modules are gitignored; only generated PNGs + this script are committed.

import fs from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";
import satori from "satori";
import { Resvg } from "@resvg/resvg-js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, "../..");
const POSTS = path.join(REPO, "_posts");
const OUT = path.join(REPO, "assets/images/og");
const FONTS = path.join(__dirname, "fonts");

const GREEN = "#16a34a";
const GREEN_LIGHT = "#4ade80";

// ---------- frontmatter ----------
function parseFrontmatter(raw) {
  const m = raw.match(/^---\n([\s\S]*?)\n---/);
  if (!m) return {};
  const fm = {};
  for (const line of m[1].split("\n")) {
    const kv = line.match(/^([a-zA-Z_]+):\s*(.*)$/);
    if (!kv) continue;
    let [, k, v] = kv;
    v = v.trim().replace(/^["']|["']$/g, "");
    fm[k] = v;
  }
  // tags: [a, b]
  const tm = m[1].match(/^tags:\s*\[(.*)\]/m);
  if (tm) fm.tags = tm[1].split(",").map((s) => s.trim().replace(/^["']|["']$/g, "")).filter(Boolean);
  return fm;
}

function slugFromFile(file) {
  return path.basename(file, ".md").replace(/^\d{4}-\d{2}-\d{2}-/, "");
}

const CAT_MAP = {
  seo: "SEO", geo: "GEO", "product-hunt": "PRODUCT HUNT", producthunt: "PRODUCT HUNT",
  github: "OPEN SOURCE", opensource: "OPEN SOURCE", "open-source": "OPEN SOURCE",
  b2b: "B2B GROWTH", saas: "SAAS", aso: "ASO", marketing: "MARKETING",
  ai: "AI", devrel: "DEVREL", startup: "STARTUP", growth: "GROWTH",
};
function categoryFor(fm, slug) {
  const tags = fm.tags || [];
  for (const t of tags) {
    const key = String(t).toLowerCase();
    if (CAT_MAP[key]) return CAT_MAP[key];
  }
  for (const k of Object.keys(CAT_MAP)) if (slug.includes(k)) return CAT_MAP[k];
  return "GROWTH TOOLS";
}

// ---------- layout ----------
function el(type, style, children) {
  return { type, props: { style, ...(children !== undefined ? { children } : {}) } };
}

function card({ title, category, domainLabel }) {
  const len = title.length;
  const titleSize = len > 95 ? 46 : len > 70 ? 54 : len > 45 ? 62 : 70;

  return el("div", {
    width: 1200, height: 630, display: "flex", flexDirection: "column",
    justifyContent: "space-between", position: "relative",
    padding: "70px 80px", fontFamily: 'Inter, "NotoSC", "NotoJP", "NotoKR"',
    background:
      "radial-gradient(1100px 560px at 88% -12%, rgba(22,163,74,0.30), rgba(11,15,14,0) 55%), linear-gradient(158deg, #0b0f0e 0%, #0e1512 100%)",
    color: "#f6faf8",
  }, [
    // header row
    el("div", { display: "flex", justifyContent: "space-between", alignItems: "center" }, [
      el("div", { display: "flex", alignItems: "center" }, [
        el("div", { width: 18, height: 18, borderRadius: 5, background: GREEN, marginRight: 14, display: "flex" }),
        el("div", { fontSize: 27, fontWeight: 700, letterSpacing: "0.20em", color: "#e8f5e9" }, "GINGIRIS"),
      ]),
      el("div", {
        display: "flex", fontSize: 20, fontWeight: 700, letterSpacing: "0.10em",
        color: GREEN_LIGHT, padding: "10px 20px", borderRadius: 999,
        border: `1px solid rgba(74,222,128,0.45)`, background: "rgba(22,163,74,0.12)",
      }, category),
    ]),
    // title
    el("div", {
      display: "flex", fontSize: titleSize, fontWeight: 800, lineHeight: 1.16,
      letterSpacing: "-0.02em", color: "#f8fbfa", maxWidth: 1040,
    }, title),
    // footer
    el("div", { display: "flex", flexDirection: "column" }, [
      el("div", { width: "100%", height: 4, borderRadius: 4, marginBottom: 22,
        background: `linear-gradient(90deg, ${GREEN} 0%, ${GREEN_LIGHT} 60%, rgba(74,222,128,0) 100%)` }),
      el("div", { display: "flex", justifyContent: "space-between", alignItems: "center" }, [
        el("div", { display: "flex", fontSize: 26, fontWeight: 700, color: GREEN_LIGHT }, domainLabel),
        el("div", { display: "flex", fontSize: 21, fontWeight: 400, color: "#7c8f84" }, "Growth tools & global-launch playbooks"),
      ]),
    ]),
  ]);
}

// ---------- main ----------
async function loadFonts() {
  const f = async (file, name, weight) => ({ name, weight, style: "normal", data: await fs.readFile(path.join(FONTS, file)) });
  return Promise.all([
    f("Inter-400.ttf", "Inter", 400),
    f("Inter-700.ttf", "Inter", 700),
    f("Inter-800.ttf", "Inter", 800),
    f("NotoSC-700.ttf", "NotoSC", 700),
    f("NotoJP-700.ttf", "NotoJP", 700),
    f("NotoKR-700.ttf", "NotoKR", 700),
  ]);
}

async function render(fonts, data) {
  const svg = await satori(card(data), { width: 1200, height: 630, fonts });
  const png = new Resvg(svg, { fitTo: { mode: "width", value: 1200 } }).render().asPng();
  return png;
}

async function main() {
  const args = process.argv.slice(2);
  const all = args.includes("--all");
  const slugArg = (args.find((a) => a.startsWith("--slug=")) || "").split("=")[1];

  await fs.mkdir(OUT, { recursive: true });
  const fonts = await loadFonts();
  const files = (await fs.readdir(POSTS)).filter((f) => f.endsWith(".md"));

  let done = 0, skipped = 0;
  for (const file of files) {
    const raw = await fs.readFile(path.join(POSTS, file), "utf8");
    const fm = parseFrontmatter(raw);
    const slug = slugFromFile(file);
    if (slugArg && slug !== slugArg) continue;
    // default behavior: only posts WITHOUT a custom image. --all overrides.
    if (!all && !slugArg && fm.image) { skipped++; continue; }
    const title = (fm.title || slug).trim();
    const data = { title, category: categoryFor(fm, slug), domainLabel: "gingiris.tools" };
    const png = await render(fonts, data);
    await fs.writeFile(path.join(OUT, `${slug}.png`), png);
    done++;
    console.log(`  ✓ ${slug}.png  [${data.category}]`);
  }
  console.log(`\nGenerated ${done}, skipped ${skipped} (already have custom image).`);
}

main().catch((e) => { console.error(e); process.exit(1); });
