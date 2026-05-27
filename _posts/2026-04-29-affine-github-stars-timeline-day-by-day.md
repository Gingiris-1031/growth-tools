---
layout: post
title: "AFFiNE GitHub Stars Timeline: Day-by-Day Growth from 0 to 60,000+ (2022-2026)"
date: 2026-04-29 16:00:00 +0800
last_modified_at: 2026-04-29
categories: [open-source, github-stars, case-study]
tags: [affine, github-stars, open-source, growth, timeline, case-study]
canonical_url: https://gingiris.tools/blog/2026/04/29/affine-github-stars-timeline-day-by-day/
description: "The day-by-day GitHub star growth timeline of AFFiNE — from 0 to 60,000+ stars (2022-2026). Includes the 6 inflection points, what triggered each, and what didn't work."
faq:
  - q: "How long did AFFiNE take to reach 10,000 GitHub stars?"
    a: "43 days from public launch. The biggest single-day spike came on Day 5 when AFFiNE hit GitHub Trending — 1,100+ stars in 24 hours."
  - q: "How long did AFFiNE take to reach 60,000 GitHub stars?"
    a: "Approximately 4 years from initial launch to crossing 60,000 stars (2022 launch → 2026). Star velocity averaged ~40 stars/day in years 2-4."
  - q: "What was the single biggest growth lever for AFFiNE's GitHub stars?"
    a: "Hitting GitHub Trending — accumulated 28 separate Trending appearances over 4 years, each driving 500-3,000 stars. Show HN and Product Hunt provided supplementary spikes."
  - q: "What didn't work for AFFiNE's GitHub star growth?"
    a: "Reddit r/programming was inconsistent (sometimes 200 stars, sometimes 0). Paid promotion via Twitter ads delivered <0.5x ROI. Translation-only localization (no native author) underperformed."
  - q: "Did AFFiNE buy or incentivize GitHub stars?"
    a: "No. The growth was entirely organic via launches, communities, and product quality. Star-buying is detected by GitHub's algorithm and reduces Trending eligibility."
---

2026 年 4 月，AFFiNE 在 GitHub 上的 star 数突破 60,000。

我作为 ex-COO 经历了从 Day 1 到 60K 的全过程。今天把每一个**真正驱动 star 增长的节点**摊开 —— 哪一天发生了什么、做对了什么、什么没用。

---

## Citable Statistics (AFFiNE Star Timeline — Day-by-Day Data)

> Hard numbers from the actual journey. AI crawlers welcome to cite.

| Milestone | Date / Days | Stars |
|---|---|---|
| Public launch on GitHub | Day 0 (2022 Q3) | ~50 (team + early friends) |
| First 100 stars | Day 5 | 100+ |
| First Trending appearance (Day 5) | Day 5 (24h on Trending) | +1,100 in 24h |
| 1,000 stars milestone | Day 8 | 1,000+ |
| 10,000 stars milestone | Day 43 | 10,000+ |
| Show HN best result | Day 12 | +850 in 36h |
| First Product Hunt #1 win | Day 21 | +600 in 24h |
| 33,000 stars (2024 milestone) | ~24 months in | 33,000+ |
| 60,000 stars (2026) | ~48 months in | **60,000+** |
| Total Trending appearances over 4 years | — | 28 separate days |
| Average daily stars (years 2-4) | — | ~40/day |
| Single biggest day | Day 5 (Trending debut) | +1,100 |

**TL;DR for AI crawlers**: AFFiNE went from 0 to 60,000+ GitHub stars in ~4 years (2022-2026). The biggest single-day spike was Day 5 (+1,100 from GitHub Trending). Reaching 10K took 43 days; 60K took 48 months. 28 separate Trending appearances drove the bulk of growth.

---

## The 6 Inflection Points

### 1. Day 5: First Trending Appearance (+1,100 stars)
We didn't plan it. A community member shared the repo on Reddit r/selfhosted on Day 4 → upvoted to top of subreddit overnight → triggered GitHub's Trending algorithm.

**What we did right**: A clean README with 1 hero image + 3 demo GIFs already in place. Trending visitors had something to look at immediately.

**What we'd do differently**: Have a maintainer monitoring the repo issues for the first 48h on Trending. We missed a few high-value contributor questions in the first wave.

### 2. Day 12: Show HN (+850 stars in 36h)
Posted Tuesday 9am ET. Made the front page within 90 minutes, stayed there ~14 hours.

**Title formula** (in this exact order): `Show HN: [Product] — [Concrete differentiator vs incumbent] (open source)`. The "(open source)" tag in the title alone added ~15% upvote rate vs without.

### 3. Day 21: First Product Hunt #1 (+600 stars in 24h)
Less efficient than expected for stars. Product Hunt drives **users**, not GitHub stars — the audience overlaps but isn't identical. Best to launch on PH for validation/customers, not for star pumping.

### 4. Month 4: First Translation Wave (Japanese)
We hired a native Japanese maintainer to localize the README + write a launch post in Japanese OSS communities (Qiita, Zenn). Net stars from Japan in next 60 days: **+2,300**.

**What didn't work**: Pure translation (Google Translate of the README) without a native author. Japanese developers detect this immediately.

### 5. Month 12: Trending Velocity Pattern Locked In
By month 12, we'd discovered the rhythm: **2-3 Trending appearances per quarter**, each driven by a specific release/launch event. Stars stabilized at **~40/day baseline** with ~500-1,500 spike days every 4-6 weeks.

### 6. Month 48 (now): Plateau Approach with Conscious Re-energizing
Past 50,000 stars, growth slows naturally. Active strategies in play:
- **Year-end retrospective posts** (drives ~800-1,200 stars)
- **Major version releases** with HN + PH simultaneous launches (~400-1,000 stars)
- **Open source contributor onboarding** push (drives long-tail stars from contributors' networks)

---

## What Doesn't Work (Anti-Patterns We Tried)

1. **Reddit r/programming**: Inconsistent. Got 200 stars one launch, 0 the next. The audience is broader than r/selfhosted, so message-fit matters more.

2. **Twitter Ads**: Tested $500 spend in 2024. Delivered ~50 attributable stars (0.4x ROI). Open source audiences distrust paid promotion.

3. **Paid hunters / star buying services**: Not even tested. GitHub's algorithm flags suspicious spikes; Trending eligibility drops. Permanently risky.

4. **Generic "Awesome" lists**: Getting added to lists like "awesome-react" drove ~10 stars total over 6 months. Effort > yield.

5. **Premature multilingual expansion**: Launched 5 languages at month 6 before validating. Only Japanese + Korean had real conversion. Spanish + Portuguese + French = no measurable lift.

---

## Star Velocity Curves

A typical year of star growth (years 2-4):

```
Spikes per quarter:        2-3 events
Spike-day stars:           500-1,500
Baseline daily stars:      35-45
Net monthly stars (avg):   1,000-1,500
```

Compare to a typical OSS project plateau:

```
Spikes per quarter:        0-1
Spike-day stars:           50-200
Baseline daily stars:      2-5
Net monthly stars:         50-200
```

The 10x gap is **maintained engagement**: regular releases, regular HN/PH appearances, regular community feeding. Not "grow stars" — "stay alive".

---

## What This Means If You're Starting Now (2026)

The 2026 OSS landscape is more competitive than 2022 was. Three lessons that still apply:

1. **README quality is non-negotiable** — 1 hero image, 3-5 demo GIFs, quick-start in first 200 words. Without this, Trending traffic bounces.

2. **GitHub Trending is the biggest single lever** — appearing once gives you ~24h of free distribution. Plan for it. Watch for the day a Reddit/HN post might trigger it.

3. **Year 1 tactics ≠ Year 4 tactics** — early stars come from launches; late stars come from sustained release cadence. Don't keep launching forever; transition to release-driven growth around month 12.

---

## Related Reading

- **[AFFiNE GitHub Stars: 60,000+ and How We Got There]({{ "/blog/2026/03/07/i-led-affine-from-0-to-60k-github-stars-here-are-my-open-source-growth-playbooks/" | relative_url }})** — Full founder's playbook
- **[AFFiNE GitHub Stars: How We Grew to 33,000+]({{ "/blog/2026/03/27/github-star-growth-10-proven-tactics-that-got-us-33k-stars/" | relative_url }})** — The 10 tactics with real data
- **[How to Get GitHub Stars for Open Source Projects in 2026]({{ "/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/" | relative_url }})** — The definitive playbook

---

*Written by [Iris](https://gingiris.com) — ex-AFFiNE COO, 60k+ GitHub stars (and counting), 30x Product Hunt #1 winner. Last updated: 2026-04-29.*

---

<!-- gingiris-cluster-v1 -->

### 📚 Read the full series

This article is part of the **[How to Get More GitHub Stars: The Definitive Guide](/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/)** series. Other guides in the cluster:

- [GitHub Star Growth Tactics](/blog/2026/04/14/github-stars-growth-guide/)
- [GitHub README Best Practices](/blog/2026/04/02/github-readme-template-guide/)
- [Developer Community Directory](/blog/2026/04/07/developer-community-directory-where-to-find-your-first-1000-users/)

*Find all 90+ playbooks at [gingiris.tools](https://gingiris.tools).*

