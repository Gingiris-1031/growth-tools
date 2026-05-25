---
layout: post
title: "How to Get on GitHub Trending: The Algorithm, the Tactics, and the Real Data"
date: 2026-04-06
canonical_url: https://gingiris.tools/blog/2026/04/06/how-to-get-on-github-trending/
image: "https://gingiris.tools/assets/images/blog-github-stars.jpg"
description: "How GitHub Trending actually works — and how AFFiNE appeared on it 28 times in 5 months. The velocity thresholds, timing strategy, and channel coordination that trigger it."
faq:
  - q: "How does GitHub Trending work?"
    a: "GitHub Trending ranks repositories by star velocity — the number of stars gained in a specific time window (daily, weekly, monthly). It is not based on total star count. A repo with 500 total stars gaining 80 in one day can outrank a repo with 50,000 stars gaining 20 in one day. The exact algorithm is not public, but velocity within the past 24-48 hours is the dominant signal for daily Trending."
  - q: "How many stars do you need to get on GitHub Trending?"
    a: "Thresholds vary by category and competition level. For All Languages daily Trending: typically 80-150+ stars in a single day. For language-specific Trending (TypeScript, Python): 30-60 stars/day is often sufficient. For weekly Trending: 300-500 stars over 7 days. AFFiNE hit All Languages Trending on day 5 of our open source launch with approximately 200+ stars that day."
  - q: "How long does a repo stay on GitHub Trending?"
    a: "Typically 1-7 days for daily Trending, 1-4 weeks for weekly Trending. Duration depends on whether your star velocity stays elevated after the initial spike. AFFiNE appeared on Trending 28 times in 5 months — not because of one sustained spike, but because each Trending appearance raised our baseline, enabling the next spike to push us back onto Trending."
  - q: "Does GitHub Trending reset every day?"
    a: "Yes. The daily Trending list resets at midnight UTC. Weekly Trending resets on Mondays. Monthly resets on the first of each month. This means you can appear on daily Trending multiple times if you maintain elevated star velocity on different days."
  - q: "Is it worth trying to get on GitHub Trending?"
    a: "Yes — if you can trigger it. GitHub Trending is viewed by tens of thousands of developers daily who are actively looking for new projects. Unlike social media, Trending visitors are already in 'discovery mode,' which means conversion rates to stars and actual users are significantly higher than most other channels. The compound effect matters: each Trending appearance raises your baseline star rate, making the next appearance easier to trigger."
hreflang_ja: https://gingiris.tools/blog/2026/04/07/github-trending-guide-ja/
hreflang_ko: https://gingiris.tools/blog/2026/04/07/github-trending-guide-ko/
---

It was a Tuesday morning in August 2022. I had been awake since 5 AM, watching our GitHub star counter. Not because I was anxious — I had actually set an alarm. We had been building toward this push for weeks: timed content, coordinated posts, a spreadsheet with 40 developers ready to share. By noon, the counter had moved from 340 to 680. By 8 PM: 1,100.

On day five of AFFiNE's open source launch, I opened GitHub Trending for the first time expecting to scroll past our name. Instead: there it was. Row seven. All Languages. We hit it with approximately 200+ stars in a single day.

I screenshotted it. I sent it to the team with zero context. (The context was: I had no idea this was going to happen. The algorithm worked before I understood it. I'm writing this so you can make it happen on purpose.)

## Key Stats

| Metric | Data |
|--------|------|
| AFFiNE Trending appearances (5 months) | 28× |
| First Trending appearance | Day 5 of open source launch |
| All Languages Trending threshold (est.) | 80–150 stars/day |
| Language-specific Trending threshold (est.) | 30–60 stars/day |
| Star baseline increase per Trending appearance | ~10–20 stars/day |

---

## TL;DR

- GitHub Trending ranks by star **velocity**, not total count
- AFFiNE hit Trending on day 5 and appeared 28 times in 5 months
- The trigger: concentrate all distribution channels into a single 48-hour window
- All Languages Trending needs ~80–150 stars/day; language Trending needs ~30–60
- Each appearance raises your baseline, making the next one easier

---

## Why GitHub Trending Is Worth Engineering

GitHub Trending is not an accident. It's a distribution channel — one that most founders treat as luck but can be deliberately triggered.

When AFFiNE appeared on GitHub Trending All Languages for the first time, we saw approximately 300–500 stars in a single day from organic discovery alone. Developers who browse Trending are actively looking for new tools. They're not scrolling past an ad — they came specifically to find something worth trying. The conversion rate from Trending view to star is significantly higher than almost any other channel.

More importantly: Trending compounds. We appeared 28 times between August and December 2022. Each appearance raised our daily baseline by 10–20 stars. After 28 appearances, our organic baseline was nearly self-sustaining — we were getting meaningful daily stars without any active promotion.

---

## How GitHub Trending Actually Works

GitHub does not publish its Trending algorithm. But from years of observation and testing, the dominant signal is clear: **star velocity in the past 24–48 hours.**

What this means practically:
- A repo gaining 100 stars today ranks above one that gained 10,000 stars last year
- Your total star count is almost irrelevant for Trending eligibility
- Timing matters: stars gained at the right moment count more than stars spread across a week

### The three Trending lists

**Daily Trending** — resets at midnight UTC, most competitive, highest traffic
**Weekly Trending** — resets Mondays, easier to achieve, sustained exposure
**Monthly Trending** — resets on the 1st, hardest to achieve, maximum exposure

### Category filters

GitHub Trending can be filtered by programming language. This is important:

- **All Languages** — hardest to rank, highest visibility
- **TypeScript / Python / Go / Rust** — significantly easier, still high-value
- **Niche languages (Lua, Elixir, etc.)** — much easier to rank, but smaller audience

If your project is language-specific, targeting your language filter first is the right strategy. AFFiNE is primarily TypeScript, so we could have targeted TypeScript Trending with a much lower threshold than All Languages.

---

## Part 1: The Trigger — 48-Hour Concentration

The single most important tactic for getting on Trending is channel concentration.

**Don't spread your launch across a week. Compress everything into 48 hours.**

Here's why this works: GitHub's Trending algorithm looks at velocity within a short window. If you post on Reddit Monday, HN Tuesday, Product Hunt Thursday, and Twitter Friday, each post drives a modest spike. None of them is large enough to hit Trending individually, and by the time the last post goes up, the first spike has already decayed.

If instead you post on Reddit, HN, Product Hunt, and Twitter all within a 24–48 hour window, the velocity from all four channels adds together. What would have been four small spikes becomes one large spike — large enough to cross the Trending threshold.

**This is what happened with AFFiNE.** We launched on Reddit and HN on day one, then Product Hunt and coordinated Twitter posting on day two. By day five, the compounding effect of all these channels plus the organic momentum they created pushed us to #1 on GitHub Trending All Languages.

### The 48-hour launch sequence

**Hour 0–6:** Post on the most relevant Reddit subreddits (r/selfhosted, r/opensource, r/programming, or your niche)
**Hour 6–12:** Submit to Hacker News (Show HN format)
**Hour 12–24:** Launch on Product Hunt (if you haven't already)
**Hour 24–36:** Twitter/X thread with metrics from the first day ("We just hit X stars in 24 hours...")
**Hour 36–48:** Follow-up posts in secondary subreddits, Dev.to cross-post, newsletter outreach

---

## Part 2: Velocity Thresholds by Category

Based on observation (not GitHub's official data):

| Category | Daily Trending (est.) | Weekly Trending (est.) |
|----------|----------------------|----------------------|
| All Languages | 80–150 stars/day | 400–600/week |
| TypeScript | 40–80 stars/day | 200–350/week |
| Python | 50–100 stars/day | 250–400/week |
| Go / Rust | 30–60 stars/day | 150–250/week |
| JavaScript | 60–120 stars/day | 300–500/week |

These thresholds shift based on competition. Watch [GitHub Trending](https://github.com/trending) for 1–2 weeks before your launch to calibrate what's actually showing up. If the repos on daily TypeScript Trending are gaining 45 stars/day, you need at least that.

---

## Part 3: The Baseline Effect — Why 28 Appearances

Most people think about Trending as a one-time event. Get lucky, spike onto the list, done. That's not how it works if you do it right.

Each time AFFiNE appeared on Trending, we attracted new developers who:
- Starred the repo (immediate stars)
- Bookmarked it or shared it (delayed stars)
- Wrote about it (backlinks and secondary mentions)

The net effect: our daily organic star rate after each Trending appearance was slightly higher than before. After the first appearance, we went from ~50 stars/day organic to ~70. After several appearances, we were at ~150. After 28 appearances over 5 months, our organic baseline was approximately 200 stars/day — enough that a modestly successful piece of content could push us back onto Trending without a full launch effort.

**The compounding model:**

```
Trending appearance → raised baseline → lower threshold for next appearance
→ easier to reach Trending again → another baseline raise → ...
```

This is why 28 appearances happened: not because we did 28 full launches, but because after the first few, the threshold we needed to cross got lower and lower relative to our baseline.

---

## Part 4: Supporting Tactics

### README optimization (prerequisite)

Before you try for Trending, your README needs to convert. A developer who lands on your repo from Trending has 10–15 seconds to decide whether to star it. If the README doesn't immediately answer "what is this and why does it matter," they leave without starring — and you lose the Trending benefit.

Your README must have:
- **Hero GIF or screenshot above the fold** — developers are visual, show don't tell
- **One-sentence value proposition** — what does this do, for whom
- **Quick start in five steps or fewer** — can they try it right now?
- **Star CTA** — a simple "⭐ If this is useful, a star helps others find it" at the top converts meaningfully

### Awesome-list submissions (slow compound)

Awesome-* repositories are curated GitHub lists with their own large audiences. Getting added gives you:
- A permanent backlink from a high-star repo
- Periodic discovery traffic as new developers browse the list
- A small but sustained baseline lift

Submit to niche awesome-lists in your category first (higher acceptance rate, ~75% for Chinese awesome-lists in our experience). Then target larger lists as your star count provides credibility.

### Newsletter outreach (post-Trending amplification)

When you first hit Trending, email 5–10 developer newsletters in your niche with a short pitch: "We just launched X and hit GitHub Trending — might be worth covering for your readers." Your Trending placement is social proof that makes the outreach credible. This turns a 1-day Trending spike into a 2–3 week media tail.

### GitHub Insights as feedback loop

During your launch window, check GitHub Insights every few hours. The Traffic section shows:
- Where your visitors are coming from (which channel is working)
- Star velocity in near-real-time
- Geographic distribution of traffic

Use this to know which subreddit or post to double down on. If Reddit is driving 60% of traffic, post a follow-up in a related subreddit. If HN is driving the most, respond to every comment to keep the post active.

---

## Part 5: Timing

### Day of week

**Tuesday–Thursday** consistently outperform other days for launch spikes. Developers are most active on these days, and Trending competition (the number of other repos also trying to spike) is similar to weekdays but without the Monday catch-up effect.

**Avoid Monday** for launches — everyone who missed the weekend does their catch-up browsing, making it harder to stand out.

**Friday–Sunday** have lower Trending competition but also lower developer browsing activity, so the tradeoff is roughly neutral.

### Time of day

Target **9am–12pm Pacific Time** for your main launch posts. This captures:
- US West Coast engineers at work
- US East Coast engineers mid-morning
- European engineers in the afternoon

Stars gained during peak hours weight more heavily in the daily Trending calculation because they represent genuine developer activity, not bot traffic.

---

## Part 6: What Doesn't Work

**Launching on multiple separate days** — each post needs to be big enough to spike individually, and they rarely are.

**Buying stars** — GitHub Trending accounts for account age and authenticity signals. A spike of stars from young or inactive accounts is discounted. Investors also check star growth patterns; fake stars will be visible in your star-history chart.

**Posting without community credibility on Reddit** — Reddit requires karma and community presence before your posts gain traction. A first-time post from a new account gets buried regardless of content quality. Build karma before you need it.

**Waiting for the perfect README** — Trending requires velocity, and velocity requires a launch. Ship with a 90% README, get on Trending, and improve based on the feedback you get from Trending traffic.

---

## The AFFiNE Timeline, Expanded

| Day | Action | Stars Gained | Notes |
|-----|--------|-------------|-------|
| Day 1 | Reddit (r/selfhosted, r/opensource) + HN Show HN | ~800 | English-only, no Chinese social media |
| Day 2 | Product Hunt launch + Twitter thread | ~1,200 | Concentrated spike |
| Day 3–4 | Follow-up subreddits, Dev.to | ~600 | Decaying but still elevated |
| Day 5 | — | — | GitHub Trending #1 All Languages triggered |
| Day 5–7 | Organic from Trending | ~1,400 | Trending drove discovery without any active posting |
| Week 2–4 | SEO content + community engagement | ~100/day | Settling to new baseline |
| Month 2–6 | Periodic relaunch + content | Variable | 28 total Trending appearances |

Total week 1: ~6,000 stars. Total day 43: 10,000 stars.

---

## Quick Reference Checklist

**Before launch:**
- [ ] README has hero GIF, one-liner, quick start, star CTA
- [ ] Karma built in target subreddits (80+ karma minimum)
- [ ] Launch date chosen: Tuesday–Thursday
- [ ] All posts drafted and ready to fire simultaneously

**Launch day (48-hour window):**
- [ ] Reddit posts live in target subreddits
- [ ] HN Show HN submitted
- [ ] Product Hunt live (if applicable)
- [ ] Twitter/X thread posted with real-time metrics
- [ ] GitHub Insights monitored every 3–4 hours

**Post-Trending:**
- [ ] Newsletter outreach with Trending as proof
- [ ] Secondary subreddit posts
- [ ] Dev.to cross-post
- [ ] Awesome-list submissions started

---

## 📚 Related Reading

| Category | Article |
|----------|---------|
| 📖 | [AFFiNE GitHub Stars: 0 to 60K — The Full Story](https://gingiris.tools/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/) |
| 📖 | [10 Proven Star Growth Tactics](https://gingiris.tools/blog/2026/03/27/github-star-growth-10-proven-tactics-that-got-us-33k-stars/) |
| 📖 | [GitHub Stars History: How to Track & Analyze Growth](https://gingiris.tools/blog/2026/03/30/github-stars-history-how-to-track-and-analyze-repository-growth/) |
| 📖 | [Reddit Marketing Without Getting Banned](https://gingiris.tools/blog/2026/03/30/reddit-marketing-guide-how-to-promote-without-getting-banned/) |
| 📖 | [I Led AFFiNE from 0 to 60K Stars](https://gingiris.tools/blog/2026/03/07/i-led-affine-from-0-to-60k-github-stars-here-are-my-open-source-growth-playbooks/) |

*More tools → [Growth Tools Directory](https://gingiris.tools/)*

