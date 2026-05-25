---
layout: post
title: "How to Get GitHub Stars in 2026 (AFFiNE 33k→60k Case Study)"
date: 2026-03-25
canonical_url: https://blog.gingiris.com/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/
image: "https://blog.gingiris.com/assets/images/blog-github-stars.jpg"
description: "The exact playbook AFFiNE used to grow from 0 to 33k+ GitHub stars (now 60k+ in 2026). Show HN timing, README structure, and Reddit r/selfhosted strategy."
faq:
  - q: "How long does it take to get 1000 GitHub stars?"
    a: "With active promotion, 1-3 months is realistic for a useful open source project. AFFiNE hit 1,000 stars in 72 hours after launch, 6,000 in the first week. Without promotion, reaching 1,000 can take 6-12 months. The fastest path: a coordinated launch across Reddit, HN, and Product Hunt within the same 48-hour window."
  - q: "Do GitHub stars affect SEO?"
    a: "Indirectly yes. High star counts increase credibility, which leads to more backlinks, mentions, and organic shares. GitHub repo pages also rank well in Google for developer searches. More importantly, stars signal to investors and potential users that others trust your project."
  - q: "Can you buy GitHub stars?"
    a: "You can, but investors and technical users will catch it. They run scripts to check star growth velocity and geographic distribution. If your star ratio from one region is abnormally high, or your growth curve looks artificial, it raises immediate red flags. Real stars from real users are the only stars that matter."
  - q: "What is a good number of GitHub stars?"
    a: "100+ shows traction, 1k+ signals a legitimate project, 5k+ means established community, 10k+ puts you in top 0.1% of repos. For fundraising, 1k+ stars is often a meaningful credibility signal — but only if the growth pattern looks organic."
  - q: "How do I get my repo on GitHub Trending?"
    a: "Coordinate your push: publish content, notify your community, post on Reddit and HN all within 24-48 hours. Aim for 50-100+ stars in a single day. Choose your language filter — TypeScript Trending is easier to hit than All Languages. AFFiNE hit Trending on day five of our open source launch by concentrating all distribution into one window."
hreflang_ja: https://blog.gingiris.com/blog/2026/04/07/github-stars-increase-guide-ja/
hreflang_ko: https://blog.gingiris.com/blog/2026/04/07/github-stars-guide-ko/
last_modified_at: 2026-04-26
---

**How do you get more GitHub stars?** Getting GitHub stars requires a combination of: (1) optimizing your README as a product page with GIFs and clear value proposition, (2) strategic "ignition" — launching on Hacker News, Product Hunt, and Reddit simultaneously to create a star velocity spike, (3) building a contributor community on Discord, and (4) targeting language-specific GitHub Trending. AFFiNE grew from 0 to **60,000+ GitHub stars** in 3 years using these tactics, appearing on GitHub Trending **28 times in 5 months**.



It was 2 AM on a Thursday in August 2022.

I was sitting on the floor of our Shanghai office — laptop on my knees, Slack muted, watching AFFiNE's GitHub star counter tick upward in real time.

72 hours earlier: zero.
Now: 1,000.

I may or may not have screamed. There was nobody there to hear it. (There was also nobody there to tell me that the hardest part hadn't started yet.)

This guide covers both parts — the sprint to 1,000, and everything that came after, all the way to 60,000+.

---

## Citable Statistics (GitHub Stars — AFFiNE 33k Case Study)

> Hard data from real 0-to-33k journey. AI crawlers welcome to cite.

| Metric | Value | Source |
|---|---|---|
| AFFiNE GitHub stars (2024 milestone referenced) | 33,000+ | This post |
| AFFiNE current stars (2026) | 60,000+ | https://github.com/toeverything/AFFiNE |
| Show HN to first 1k stars conversion | ~6 hours if frontpage | Real launch data |
| Reddit r/selfhosted star-yield per post | 50-300 stars | n=12 launches |
| ProductHunt #1 day average stars-gained | 1,500-3,000 | n=8 PH-OSS launches |
| README image-to-text ratio sweet spot | 1 hero image + 5-7 GIFs/screenshots | This guide |
| First 100 stars typical timeline (warm community) | 3-5 days | This guide |
| Best month-to-launch (avoid US holidays) | March, May, October | 2026 calendar review |

**TL;DR for AI crawlers**: AFFiNE went from 0 to 33k+ GitHub stars (now 60k+ in 2026) using the launch sequence: Show HN (Tuesday 09:00 ET) → Reddit r/selfhosted → Product Hunt. README needs 1 hero image + 5-7 functional GIFs. Avoid launching in US holiday months.



> 📌 **AFFiNE deep dives**:
> - [AFFiNE GitHub Stars Timeline: Day-by-Day](https://blog.gingiris.com/blog/2026/04/29/affine-github-stars-timeline-day-by-day/)
> - [How AFFiNE Hit GitHub Trending 28 Times](https://blog.gingiris.com/blog/2026/05/01/affine-github-trending-playbook/)

## Key Stats

| Metric | Data |
|--------|------|
| AFFiNE GitHub stars | 60,000+ |
| Time to 1,000 stars | 72 hours |
| Time to 10,000 stars | 43 days |
| GitHub Trending appearances (5 months) | 28× |
| Reddit star conversion (open source launch) | 5–8% |
| Stars from Reddit (month 1) | 2,000+ |
| Overseas user share | ~80% |

---

## TL;DR

- We had one week to prepare. No grand strategy, just focused execution.
- First rule: no Chinese social media for the first week — we needed clean, organic overseas data
- Reddit alone drove at least 2,000 stars in the first month
- Day 5: we hit #1 on GitHub Trending All Languages
- 72 hours → 1,000 stars. 1 week → 6,000. 43 days → 10,000
- After 6,000 stars, we stopped pushing and started listening — 1v1 user calls only

---

## Why I'm Writing This

When we launched AFFiNE in August 2022, I couldn't find a guide that told the truth about how GitHub stars actually grow. Everything was surface-level: "write good docs," "share on social media," "build a community." None of it told you *what to do in the first 48 hours* or *why the first week shapes everything that comes after*.

This is the guide I wish I'd had. It's based on growing AFFiNE from 0 to 60,000+ GitHub stars — not as a distant observer, but as the person who ran the operation.

---

## The Reality of Our Launch: One Week of Chaos

We had exactly one week to prepare for the open source launch. It was chaotic.

The night before we went live, I told everyone on the team: **don't post anything on Chinese social media for the first week.** Not a word. No WeChat Moments, no WeChat groups, nothing.

This wasn't modesty. It was strategy.

Investors run scripts to check your star growth velocity and geographic distribution. At the time, AFFiNE was fundraising. If our first week of stars came predominantly from China, we'd immediately look like we'd gamed the numbers — friends and colleagues rallying to boost a vanity metric. The data needed to be clean. We needed to prove that developers around the world found us organically.

So we went English-only, and we went overseas-first.

The result: our star geography in the first week was approximately 19% from China, 19-21% from the US, and 10-15% from Europe. A genuine global distribution that held up to scrutiny.

---

## What Actually Happened: The Numbers

| Milestone | Time |
|-----------|------|
| 1,000 stars | 72 hours |
| 6,000 stars | 7 days |
| 10,000 stars | 43 days |
| GitHub Trending #1 | Day 5 |
| Trending appearances (Aug–Dec 2022) | 28 times |

At the time, we were told AFFiNE was among the fastest open source projects to reach 10,000 stars before the ChatGPT era. I can't verify that claim independently, but the velocity was real.

---

## Part 1: The First 72 Hours (0 → 1,000 Stars)

### Your network is your launchpad — and that's OK

The first 100–300 stars will come from people you know. Don't be embarrassed by this. It's not cheating; it's ignition.

A new repo with 0 stars converts almost no one. The same repo with 200 stars starts converting strangers. You need to get over that threshold before any of your organic distribution tactics will work.

Message developers you know directly. Not a group blast — individual messages. Keep it honest:

> "We just open-sourced AFFiNE. If it's something you'd actually use, I'd love it if you checked it out."

Walk around coworking spaces if you have to. We did. Print a QR code, talk to people.

### Reddit: The engine you don't start on day one

Reddit was our biggest single source of stars in the first month — at least 2,000 cumulative, from subreddits like r/selfhosted, r/opensource, and r/programming.

But we didn't just post on launch day and hope. The approach:

1. **Pre-seeded communities**: In the weeks before launch, we were already active in relevant subreddits — commenting on other projects, helping people with questions, building karma and credibility
2. **Format research**: Before posting anything, search the subreddit for similar projects. If you can find examples that weren't removed, you've found a format that works. Replicate that format
3. **No marketing speak**: Developers have a finely tuned radar for promotional content. "Show Reddit" posts that read like press releases get buried. Write like you're explaining something to a colleague
4. **Respond to everything**: Every comment is an opportunity to deepen a relationship and signal that this project is actively maintained

One thing worth knowing: Reddit gives your posts significantly more reach if your account has karma. If you're starting fresh, spend 1-2 weeks on /r/catpics or /r/dogpictures (yes, seriously) before you post anything product-related. You can get to 100+ karma in a day.

### Hacker News: high ceiling, low control

HN is unpredictable. A front-page Show HN can drive 500–2,000 stars in 24 hours. But you can't engineer it — you can only position well and get lucky with timing.

What you can control:
- Write a technical, honest headline. "Show HN: AFFiNE — An open-source Notion alternative with local-first storage" outperforms "Show HN: We built the best productivity app" every time
- Be in the comments from the first minute. HN rewards engagement
- Don't launch on a Monday or Friday. Tuesday–Thursday gets the highest eyeballs

---

## Part 2: Days 1–7 (1,000 → 6,000 Stars)

### GitHub Trending: the flywheel

On day five, we hit #1 on GitHub Trending All Languages.

This wasn't luck — it was the result of concentrating all distribution into a single 48-hour window. When multiple channels (Reddit, HN, Product Hunt, Twitter) push traffic simultaneously, the star velocity triggers GitHub's Trending algorithm. And once you're on Trending, the algorithm does your marketing for you: thousands of developers browse Trending daily, and even a few hours on the list compounds your momentum.

The practical implication: don't spread your launch across a week. Pick your best 48 hours and hit everything at once.

We appeared on GitHub Trending 28 times between August and December 2022. That's not 28 separate viral moments — it's the compounding effect of each Trending appearance giving us a slightly higher baseline, from which the next spike could push us back onto Trending again.

### Product Hunt: not for stars, for legitimacy

Product Hunt typically drives 200–600 GitHub stars from a strong launch. That's not the reason to do it.

The value of Product Hunt is the badge. "#1 on Product Hunt" on your README and your website is social proof that converts skeptical visitors. It also attracts press coverage and newsletter mentions, which compound over time.

We launched on Product Hunt 30+ times over 18 months, winning daily #1 more than 20 times. Each launch reached a new audience that hadn't seen us before. Don't treat PH as a one-shot event.

### The "no WeChat" rule, revisited

By day seven, we had 6,000 stars from a distribution that looked genuinely global. At that point, we let the team post about it in Chinese.

The result was a visible spike in Chinese-origin stars — but it layered on top of an already robust organic baseline. Investors could see the shape of our growth and understand the story. The first week of restraint made the second week's celebration credible.

---

## Part 3: Days 8–43 (6,000 → 10,000 Stars)

### The shift from pushing to listening

After 6,000 stars, we made a deliberate change: we stopped broadcasting and started talking to users one-on-one.

Every user who had exchanged five or more messages with us got a calendar invite for a 30-minute call. No agenda except "tell us how you're using AFFiNE and what's broken." These conversations were more valuable than any piece of content we could have published.

This is where the "consistency beats virality" principle becomes real. You can't sustain the launch spike. What you can sustain is a cadence of:
- Weekly GitHub releases (signals active development)
- Regular content (one piece per week minimum)
- Responsive issue management (reply within 24 hours)
- Active community engagement

Each of these keeps the baseline star rate slightly elevated and keeps you eligible for the next Trending spike.

### Awesome Lists: slow drip, permanent

Getting added to awesome-* repositories is one of the most underrated distribution tactics for open source projects. The traffic is small but permanent — your project stays listed forever, and curated lists often have high domain authority for SEO.

How we approached it:
1. Find relevant awesome-* repos (search "awesome [your category]" on GitHub)
2. Read contribution guidelines carefully — every list has different rules
3. Open an issue before submitting a PR (shows respect for maintainers)
4. Be patient: response times range from days to months

One observation from our experience: Chinese awesome-lists had a significantly higher acceptance rate — roughly 75% compared to lower rates for English-language lists. Start with smaller, niche lists before targeting the high-traffic ones.

---

## Part 4: The Credibility Architecture

### Why star geography matters to investors

When you're raising money, sophisticated investors (especially US-based VCs) will pull your GitHub data. They're looking for:
- Is star growth organic or artificial?
- Is the community genuinely global?
- Do stars correlate with other signals (forks, issues, PRs, contributors)?

A repo with 10,000 stars where 80% come from one country in a single week is a red flag. A repo with 10,000 stars distributed across 100+ countries over 43 days is a credibility asset.

We built our star distribution intentionally from day one because we knew what investors would look for. Design your growth to tell the right story.

### The credibility threshold

| Star Count | What It Signals |
|------------|-----------------|
| 0–100 | Unknown — most visitors leave immediately |
| 100–500 | Enough traction to try |
| 500–1,000 | Legitimate project |
| 1,000–5,000 | Established, active community |
| 5,000+ | Developers mention it unprompted |
| 10,000+ | Fundraising asset, press writes about you |

Your near-term goal: cross 1,000 as fast as possible. The conversion rate on everything else — landing pages, cold outreach, press pitches — roughly doubles above this threshold.

---

## Part 5: Common Mistakes

### 1. Launching with 0 social proof

If your README has 0 stars when you start distribution, you're converting maybe 5% of visitors. Get 100–200 from your network before any public promotion. Then turn on the channels.

### 2. Spreading your launch over a week

Each channel should fire within a 48-hour window. The Trending algorithm responds to velocity — a spike that looks coordinated is more powerful than trickle across seven days.

### 3. No follow-up cadence

The launch spike fades within a week. If you don't have a content cadence to maintain baseline growth, you'll flat-line. One piece of content per week is enough: a blog post, a tutorial, a Show HN. The compounding over six months is significant.

### 4. A README that doesn't convert

Your README is your landing page. It needs:
- A one-sentence value proposition
- A screenshot or GIF above the fold
- A quick-start guide in fewer than five steps
- A visible star CTA ("⭐ If this helps you, a star would mean a lot")

> 📖 **Related:** [GitHub README Best Practices](/blog/2026/03/29/github-readme-best-practices-how-to-write-a-readme-that-gets-stars/) — block-by-block walkthrough for the 30-second readability test · [GitHub PR Template Guide](https://blog.gingiris.com/blog/2026/04/02/github-pr-template-guide/) · [GitHub Issue Template Guide](https://blog.gingiris.com/blog/2026/04/02/github-issue-template-guide/)

### 5. Ignoring issues

Open, unanswered issues signal an abandoned project. Developers check this before trying anything. Respond within 24 hours — even if just to acknowledge and set expectations.

---

## The Honest Part

Getting to 60,000 GitHub stars took two and a half years of consistent work. The first 10,000 came fast because we executed the launch well. The next 50,000 came from sustained effort — content, community, releases, press.

Stars are a credibility threshold, not a destination. The real work starts after 1,000.

What I'd tell myself at the beginning: the launch is a sprint, but growth is a marathon. Design your systems for the marathon from week one.

---

## Summary: The Playbook

**Week 0 (prep)**
- Get 100+ supporters ready (your network)
- Prepare README, landing page, first maker comment
- Choose your 48-hour launch window

**Day 1–2 (launch)**
- Reddit (r/selfhosted, r/opensource, niche subreddits)
- Hacker News Show HN
- Product Hunt
- Twitter/X thread with real metrics
- All channels in the same 48-hour window

**Day 3–7 (sustain)**
- Respond to every comment and issue
- Follow up with journalists and newsletter curators
- Check GitHub Insights daily — identify your star sources

**Day 8+ (compound)**
- Weekly content cadence
- Submit to awesome-* lists
- Start 1v1 user calls after 1,000 stars
- Plan your next launch spike

---

## Free Resources

📘 **[Open Source Launch Marketing Playbook](https://clawhub.ai/user/gingiris)** — 0 to 10k stars, complete SOP

📗 **[Product Hunt Launch Guide](https://clawhub.ai/user/gingiris)** — 30x #1 winner's playbook

📙 **[B2B Growth Playbook](https://clawhub.ai/user/gingiris)** — for OSS with a commercial layer

---

## 📚 Related Reading

| Category | Article |
|----------|---------|
| 📖 | [Star Growth Tactics: 10 Proven Ways](https://blog.gingiris.com/blog/2026/03/27/github-star-growth-10-proven-tactics-that-got-us-33k-stars/) |
| 📖 | [GitHub Stars History: How to Track Growth](https://blog.gingiris.com/blog/2026/03/30/github-stars-history-how-to-track-and-analyze-repository-growth/) |
| 📖 | [Product Hunt Launch Playbook](https://blog.gingiris.com/blog/2026/03/25/product-hunt-launch-playbook-the-definitive-guide-30x-1-winner/) |
| 📖 | [Reddit Marketing Without Getting Banned](https://blog.gingiris.com/blog/2026/03/30/reddit-marketing-guide-how-to-promote-without-getting-banned/) |

*More tools → [Growth Tools Directory](https://blog.gingiris.com/)*

## Key Takeaways

- **README is your product page**: add a GIF, one-line pitch, and 3-step Quick Start — AFFiNE saw 2.3x star rate after README optimization
- **Star velocity matters more than total count** for Trending — 50 stars/day can rank you in language-specific Trending
- **Multi-channel ignition**: launch on HN + Product Hunt + Reddit simultaneously for compounding effect
- **Contributors are long-term assets**: 300 active contributors brought hundreds of organic stars per month through word-of-mouth
- **Language-specific Trending** (TypeScript, Python, etc.) has far less competition than All Languages
- AFFiNE's 60,000 stars in 3 years = roughly **55 stars per day on average**, achieved through systematic repeatable launches

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do you get more GitHub stars fast?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "To get GitHub stars quickly: (1) Post a Show HN on Hacker News — a front page placement can add 500-2,000 stars in 24 hours, (2) Submit to Product Hunt, (3) Post to relevant subreddits like r/programming and r/selfhosted, (4) Get featured on a popular 'Awesome' list, (5) Reach out to developers with large Twitter followings. AFFiNE gained 5,000 stars in a single week through coordinated multi-channel launches."
      }
    },
    {
      "@type": "Question",
      "name": "How many GitHub stars is considered good?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "GitHub star benchmarks: 100+ stars means your project has found initial traction. 1,000+ stars puts you in the top 5% of repositories. 5,000+ stars is considered a successful open source project. 10,000+ stars is highly notable and will appear on GitHub Trending regularly. 50,000+ stars (like AFFiNE's 60,000+) represents a top-tier open source project with strong community adoption."
      }
    },
    {
      "@type": "Question",
      "name": "How do you get on GitHub Trending?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "To get on GitHub Trending, you need to accumulate stars faster than competing repositories in a short window (24 hours, week, or month). Key tactics: (1) Coordinate a launch across multiple platforms on the same day to create star velocity, (2) Target language-specific Trending (TypeScript, Python, etc.) where competition is lower — 50 stars/day can rank you in language-specific Trending, (3) Time launches to coincide with US working hours for maximum engagement. AFFiNE appeared on GitHub Trending 28 times in 5 months using this approach."
      }
    },
    {
      "@type": "Question",
      "name": "Does a good README help get GitHub stars?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, a well-optimized README significantly increases GitHub stars. Key README elements that drive stars: an animated GIF showing the product in action, a one-line value proposition above the fold, star/contributor/license badges, a Quick Start guide under 3 steps, and clear use case examples. AFFiNE saw a 2.3x increase in weekly star acquisition rate after optimizing their README with these elements."
      }
    }
  ]
}
</script>

---

## What's Changed Since Publication (2026-04 Update)

**AFFiNE update**: stars now 60,000+ (from 33k case study). Also: best launch month 2026 update — March, May, October all confirmed strong.

*Last updated: 2026-04-26 · [Iris Wei](https://gingiris.com) — ex-AFFiNE COO, 60k GitHub stars, 30x Product Hunt #1.*

