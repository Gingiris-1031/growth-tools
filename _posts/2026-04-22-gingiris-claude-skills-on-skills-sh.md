---
title: "I Shipped 6 Gingiris Claude Skills to skills.sh — One-Line Install, Zero Setup"
date: 2026-04-22
description: "Six production-grade Claude Skills for Product Hunt launch, open source marketing, B2B SaaS growth, ASO, SEO/GEO, and a meta-router. Install via npx with a single command."
tags: [claude-skills, claude-code, product-hunt, open-source-marketing, b2b-saas, aso, seo, geo, developer-marketing]
canonical_url: https://gingiris.tools/blog/2026/04/22/gingiris-claude-skills-on-skills-sh/
seo_title: "6 Gingiris Claude Skills on skills.sh — One-Line npx Install (2026)"
seo_description: "Six battle-tested growth playbooks — Product Hunt launch, open source marketing, B2B SaaS PLG, ASO, SEO/GEO dual-engine, and a meta-router — now installable as Claude Skills. Copy the npx command and go."
keywords: [claude skills, skills.sh, npx skills add, product hunt launch skill, open source marketing skill, b2b saas growth skill, aso skill, seo geo skill, claude code skills, agent skills, growth finder, meta skill]
---

# I Shipped 6 Gingiris Claude Skills to skills.sh — One-Line Install, Zero Setup

Tuesday morning in Kunshan — I opened skills.sh, searched "seo-audit," and stared at the leaderboard for three minutes. Thirty-plus skills, most of them thin wrappers around "write me a blog post." Nothing about **actually launching a product to the world**. No Product Hunt SOP. No GitHub-star growth playbook. No ASO checklist that understood how Chinese indie apps break through in non-Chinese markets.

So I spent the afternoon shipping four — then the meta-router, then the SEO/GEO dual-engine playbook. Six total.

They live on [skills.sh](https://skills.sh) now — Vercel's public directory for Claude Skills, the same surface that top skills pull 500K+ installs from. Each of mine is a single `npx` command away. No account, no setup, no config.

---

## What's a Claude Skill (and why it's different from a blog post)

A blog post sits on a page and waits for you to read it — the knowledge stays outside the agent. A Claude Skill is a structured `SKILL.md` file that gets **loaded into your Claude Code / Cursor / Codex session as working memory**. When you say "launch my product on Product Hunt," the agent already has the playbook, the KOL outreach templates, and the Manus/Devin case studies in context.

The same content, but executable.

## Key Stats

| Skill | What it covers | Real case studies | Install command |
|---|---|---|---|
| **gingiris-launch** | Product Hunt launch SOP, KOL outreach, UGC growth, hunter network | Manus, Devin, AFFiNE (30x #1 winner) | `npx skills add Gingiris/gingiris-launch` |
| **gingiris-opensource** | GitHub star growth, HackerNews launch, OSS go-to-market | AFFiNE 60k stars in 24 months | `npx skills add Gingiris/gingiris-opensource` |
| **gingiris-b2b-growth** | PLG/SLG, PMF validation, freemium conversion, enterprise motion | HeyGen, Deel, Vercel, Supabase, AWS | `npx skills add Gingiris/gingiris-b2b-growth` |
| **gingiris-aso-growth** | ASO keyword ranking, app cold start, TikTok/Reels/Shorts UGC matrix | Chinese indie app breakthroughs | `npx skills add Gingiris/gingiris-aso-growth` |
| **gingiris-seo-geo** | Dual-engine SEO + Generative Engine Optimization, E-E-A-T, JSON-LD, schema | AFFiNE organic growth, 150+ AI startup consults | `npx skills add Gingiris/gingiris-seo-geo` |
| **gingiris-growth-finder** | Meta-router that diagnoses your situation and invokes the right specialist | — (auto-routes to the five above) | `npx skills add Gingiris/gingiris-growth-finder` |

All six support Claude Code, Cursor, Codex, Amp, Cline — the standard Agent Skills runtime set. Each `SKILL.md` is quadrilingual (EN/ZH/JA/KO) so they trigger correctly regardless of which language you're prompting in.

---

## 1. gingiris-launch — The Product Hunt Launch Skill

```bash
npx skills add Gingiris/gingiris-launch
```

If you've read my *Product Hunt Launch Playbook* on Gumroad (~400 buyers, no refunds), this is the same content — restructured as agent instructions. The skill knows the **timezone math** (why 12:01 AM PT still beats 12:01 AM GMT+8 for global SaaS), the **hunter network handoff** (what to DM, when, and to whom), and the **maker comment sequence** that compounds comment-count ranking signal through the first 4 hours.

What makes this specific rather than generic: it refuses to recommend generic "post on Twitter" playbooks. When you activate it, the agent asks for product category, target ICP, and which of the three KOL tiers you already have relationships with — then branches into a tailored 14-day prep plan.

**Try it with**: "Help me plan a Product Hunt launch for my AI coding tool targeting dev teams in NA."

[View skill →](https://skills.sh/Gingiris/gingiris-launch) · [Source →](https://clawhub.ai/user/gingiris)

---

## 2. gingiris-opensource — The 10k-Stars Skill

```bash
npx skills add Gingiris/gingiris-opensource
```

The skill I wish existed when AFFiNE had 300 stars. It encodes what actually worked on the path from 300 → 60k — not "write a good README" (everyone says that), but the **exact launch-week sequence**: HN submission timing windows, the `r/programming` flair that survives mod review, the three awesome-lists that actually move the needle (and the twenty that don't), and the **evergreen SEO** pattern that keeps pulling stars 18 months after the initial launch spike.

**Try it with**: "My open source project has 800 stars. How do I get to 5k in 90 days?"

[View skill →](https://skills.sh/Gingiris/gingiris-opensource) · [Source →](https://clawhub.ai/user/gingiris)

---

## 3. gingiris-b2b-growth — The PMF-to-ARR Skill

```bash
npx skills add Gingiris/gingiris-b2b-growth
```

Most "B2B SaaS growth" content on the internet stops at "do PLG." This skill goes the other direction — when **should you not do PLG**, how do you transition from PLG to SLG when usage hits $50k ARR, and what does Vercel's hybrid motion actually look like in practice (hint: it's not what their marketing says).

Case studies are specific, dated, and sourced: HeyGen's affiliate program mechanics, Deel's channel partnership terms, Supabase's self-serve-to-enterprise handoff, AWS's startup credit funnel conversion rates.

**Try it with**: "I have a $800k ARR devtool. Should I hire an AE or double down on PLG?"

[View skill →](https://skills.sh/Gingiris/gingiris-b2b-growth) · [Source →](https://clawhub.ai/user/gingiris)

---

## 4. gingiris-aso-growth — The Mobile Cold Start Skill

```bash
npx skills add Gingiris/gingiris-aso-growth
```

The underdog of the four — ASO skills barely exist on skills.sh, and the ones that do are 2023-era keyword-stuffing guides. Mine covers the 2026 reality: **App Store AI-rewritten listings**, **TikTok/Reels/Shorts creator matrix** as UA channel (cheaper than Apple Search Ads, higher intent than Meta), and the AI-generated-content multi-account scaling pattern that Chinese indie apps used to crack US Top 100 Photography without paid UA.

**Try it with**: "My iOS app has 50 DAU. Help me plan a 90-day cold start with $2k budget."

[View skill →](https://skills.sh/Gingiris/gingiris-aso-growth) · [Source →](https://clawhub.ai/user/gingiris)

---

## 5. gingiris-seo-geo — The Dual-Engine SEO/GEO Skill

```bash
npx skills add Gingiris/gingiris-seo-geo
```

The strategic differentiator. Every other SEO skill on skills.sh teaches 2023-era keyword density and backlink tactics. Mine treats SEO and GEO (Generative Engine Optimization — getting cited by ChatGPT, Perplexity, Claude, Gemini) as **one problem with two surfaces**. Because structured data (JSON-LD), E-E-A-T signal, and comparison-page architecture serve both at once.

What's inside: copy-paste JSON-LD templates for SoftwareApplication/Article/FAQ/HowTo schemas, the E-E-A-T writing voice system (time-anchored openings, parenthetical asides, em-dash transitions — yes, the voice you're reading right now), keyword funnel strategy for programmatic SEO without thin-content penalties, IndexNow setup for instant Bing/Yandex push, and the comparison-page SOP that gets cited in AI overviews.

**Try it with**: "My SaaS landing page ranks #14 on Google for 'AI competitor analysis.' How do I also get cited by Perplexity when users ask the same question?"

[View skill →](https://skills.sh/Gingiris/gingiris-seo-geo) · [Source →](https://clawhub.ai/user/gingiris)

---

## 6. gingiris-growth-finder — The Meta-Router

```bash
npx skills add Gingiris/gingiris-growth-finder
```

The meta-skill that picks the right playbook for your situation. Modeled after Vercel's `find-skills` (500K+ installs, the highest on the directory) — agents auto-invoke it because routing is always step zero.

Growth questions sound similar but require wildly different playbooks. "How do I launch?" for a dev tool is nothing like "How do I launch?" for a mobile app. "How do I grow?" at $1M ARR is nothing like "How do I grow?" at 100 DAU. This skill diagnoses your situation across three dimensions — product type, growth stage, and primary channel gap — then invokes the matching specialist from the five above.

**Try it with** anything vague: "I want to grow my startup," "How do I launch X," "What's wrong with my acquisition funnel" — it asks the right diagnostic questions first.

[View skill →](https://skills.sh/Gingiris/gingiris-growth-finder) · [Source →](https://clawhub.ai/user/gingiris)

---

## How to install all six at once

```bash
npx skills add Gingiris/gingiris-growth-finder -g    # install the router first
npx skills add Gingiris/gingiris-launch -g
npx skills add Gingiris/gingiris-opensource -g
npx skills add Gingiris/gingiris-b2b-growth -g
npx skills add Gingiris/gingiris-aso-growth -g
npx skills add Gingiris/gingiris-seo-geo -g
```

The `-g` flag installs globally so every Claude Code session picks them up. First install takes ~5 seconds per skill; after that they live in `~/.agents/skills/` and trigger automatically when you prompt about the matching domain.

If you install any of these and hit a rough edge, open an issue on the corresponding GitHub repo — I read every one. The playbooks are opinionated; I'd rather hear "you're wrong about HN timing" than silence.

**Your move** — pick the one that matches your current launch and copy the `npx` line. Or just install `gingiris-growth-finder` and let it route.

---

<!-- gingiris-cluster-v1 -->

### 📚 Read the full series

This article is part of the **[SaaS Marketing 2026: The Complete Playbook](/blog/2026/04/03/saas-marketing-guide/)** series. Other guides in the cluster:

- [SaaS Marketing on a $0 Budget: 7 Tactics That Worked](/blog/2026/04/29/saas-marketing-on-a-budget/)
- [Go-to-Market Strategy 2026](/blog/2026/04/03/go-to-market-strategy-the-complete-2026-playbook-for-startups/)
- [Best Growth Tools for SaaS 2026](/blog/2026/04/02/best-growth-tools-for-saas-2026/)

*Find all 90+ playbooks at [gingiris.tools](https://gingiris.tools).*

