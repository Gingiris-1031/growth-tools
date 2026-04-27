---
title: "I Shipped 4 Gingiris Claude Skills to skills.sh — One-Line Install, Zero Setup"
date: 2026-04-22
description: "Four production-grade Claude Skills for Product Hunt launch, open source marketing, B2B SaaS growth, and ASO are now live on skills.sh. Install via npx with a single command."
tags: [claude-skills, claude-code, product-hunt, open-source-marketing, b2b-saas, aso, developer-marketing]
canonical_url: https://gingiris.github.io/growth-tools/blog/2026/04/22/gingiris-claude-skills-on-skills-sh/
seo_title: "4 Gingiris Claude Skills on skills.sh — One-Line npx Install (2026)"
seo_description: "Four battle-tested growth playbooks — Product Hunt launch, open source marketing, B2B SaaS PLG, and ASO — now installable as Claude Skills. Copy the npx command and go."
keywords: [claude skills, skills.sh, npx skills add, product hunt launch skill, open source marketing skill, b2b saas growth skill, aso skill, claude code skills, agent skills]
---

# I Shipped 4 Gingiris Claude Skills to skills.sh — One-Line Install, Zero Setup

Tuesday morning in Kunshan — I opened skills.sh, searched "seo-audit," and stared at the leaderboard for three minutes. Thirty-plus skills, most of them thin wrappers around "write me a blog post." Nothing about **actually launching a product to the world**. No Product Hunt SOP. No GitHub-star growth playbook. No ASO checklist that understood how Chinese indie apps break through in non-Chinese markets.

So I spent the afternoon shipping four.

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

All four support Claude Code, Cursor, Codex, Amp, Cline — the standard Agent Skills runtime set. Each `SKILL.md` is quadrilingual (EN/ZH/JA/KO) so they trigger correctly regardless of which language you're prompting in.

---

## 1. gingiris-launch — The Product Hunt Launch Skill

```bash
npx skills add Gingiris/gingiris-launch
```

If you've read my *Product Hunt Launch Playbook* on Gumroad (~400 buyers, no refunds), this is the same content — restructured as agent instructions. The skill knows the **timezone math** (why 12:01 AM PT still beats 12:01 AM GMT+8 for global SaaS), the **hunter network handoff** (what to DM, when, and to whom), and the **maker comment sequence** that compounds comment-count ranking signal through the first 4 hours.

What makes this specific rather than generic: it refuses to recommend generic "post on Twitter" playbooks. When you activate it, the agent asks for product category, target ICP, and which of the three KOL tiers you already have relationships with — then branches into a tailored 14-day prep plan.

**Try it with**: "Help me plan a Product Hunt launch for my AI coding tool targeting dev teams in NA."

[View skill →](https://skills.sh/Gingiris/gingiris-launch) · [Source →](https://github.com/Gingiris/gingiris-launch)

---

## 2. gingiris-opensource — The 10k-Stars Skill

```bash
npx skills add Gingiris/gingiris-opensource
```

The skill I wish existed when AFFiNE had 300 stars. It encodes what actually worked on the path from 300 → 60k — not "write a good README" (everyone says that), but the **exact launch-week sequence**: HN submission timing windows, the `r/programming` flair that survives mod review, the three awesome-lists that actually move the needle (and the twenty that don't), and the **evergreen SEO** pattern that keeps pulling stars 18 months after the initial launch spike.

**Try it with**: "My open source project has 800 stars. How do I get to 5k in 90 days?"

[View skill →](https://skills.sh/Gingiris/gingiris-opensource) · [Source →](https://github.com/Gingiris/gingiris-opensource)

---

## 3. gingiris-b2b-growth — The PMF-to-ARR Skill

```bash
npx skills add Gingiris/gingiris-b2b-growth
```

Most "B2B SaaS growth" content on the internet stops at "do PLG." This skill goes the other direction — when **should you not do PLG**, how do you transition from PLG to SLG when usage hits $50k ARR, and what does Vercel's hybrid motion actually look like in practice (hint: it's not what their marketing says).

Case studies are specific, dated, and sourced: HeyGen's affiliate program mechanics, Deel's channel partnership terms, Supabase's self-serve-to-enterprise handoff, AWS's startup credit funnel conversion rates.

**Try it with**: "I have a $800k ARR devtool. Should I hire an AE or double down on PLG?"

[View skill →](https://skills.sh/Gingiris/gingiris-b2b-growth) · [Source →](https://github.com/Gingiris/gingiris-b2b-growth)

---

## 4. gingiris-aso-growth — The Mobile Cold Start Skill

```bash
npx skills add Gingiris/gingiris-aso-growth
```

The underdog of the four — ASO skills barely exist on skills.sh, and the ones that do are 2023-era keyword-stuffing guides. Mine covers the 2026 reality: **App Store AI-rewritten listings**, **TikTok/Reels/Shorts creator matrix** as UA channel (cheaper than Apple Search Ads, higher intent than Meta), and the AI-generated-content multi-account scaling pattern that Chinese indie apps used to crack US Top 100 Photography without paid UA.

**Try it with**: "My iOS app has 50 DAU. Help me plan a 90-day cold start with $2k budget."

[View skill →](https://skills.sh/Gingiris/gingiris-aso-growth) · [Source →](https://github.com/Gingiris/gingiris-aso-growth)

---

## How to install all four at once

```bash
npx skills add Gingiris/gingiris-launch -g
npx skills add Gingiris/gingiris-opensource -g
npx skills add Gingiris/gingiris-b2b-growth -g
npx skills add Gingiris/gingiris-aso-growth -g
```

The `-g` flag installs globally so every Claude Code session picks them up. First install takes ~5 seconds per skill; after that they live in `~/.agents/skills/` and trigger automatically when you prompt about the matching domain.

## What's next

I'm working on a fifth skill — `gingiris-growth-finder` — a meta-skill that routes growth questions to the right playbook automatically (modeled after Vercel's `find-skills`, which has 500K+ installs because agents auto-invoke it). Expect it within the week.

If you install any of these and hit a rough edge, open an issue on the corresponding GitHub repo — I read every one. The playbooks are opinionated; I'd rather hear "you're wrong about HN timing" than silence.

**Your move** — pick the one that matches your current launch and copy the `npx` line.
