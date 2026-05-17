---
layout: post
title: "Show HN Guide 2026: Frontpage Tactics + Best Time to Post"
date: 2026-04-07
canonical_url: https://gingiris.github.io/growth-tools/blog/2026/04/07/how-to-launch-on-hacker-news-show-hn-guide/
image: "https://gingiris.github.io/growth-tools/assets/images/blog-github-stars.jpg"
description: "The exact Show HN playbook used to hit Hacker News frontpage. Tuesday 9 AM ET timing, title formula, comment strategy, and 5 reasons launches fail."
faq:
  - q: "What is Show HN and how does it work?"
    a: "Show HN is Hacker News's dedicated format for sharing projects with the community. Posts beginning with 'Show HN:' get special treatment: they appear on a dedicated /shownew page, receive a grace period where they can't be downvoted immediately, and are exempt from the 'no self-promotion' rule that applies to regular posts. The HN community actively looks at Show HN for genuinely interesting technical projects — it's one of the few places online where sophisticated early adopters seek out new tools."
  - q: "When is the best time to post on Hacker News?"
    a: "9–10 AM ET on a weekday (Monday–Thursday) gives you the best shot at front page. This is when HN traffic peaks and when power users who upvote early are most active. Sunday 10 AM ET also works well — less competition, and the weekend audience is slightly more exploratory. Avoid Friday afternoon and Saturday."
  - q: "How many upvotes does it take to reach the Hacker News front page?"
    a: "Roughly 30–50 upvotes in the first hour is enough to push a Show HN post onto the front page, assuming the velocity is genuine. HN's algorithm factors in vote velocity, comment engagement, and time decay heavily. A post that gets 20 upvotes in the first 10 minutes will rank higher than one that gets 50 upvotes spread over 3 hours. Front page posts typically end up with 200–600 points total."
  - q: "Can you resubmit a Show HN if it didn't gain traction?"
    a: "Yes — HN's guidelines allow resubmitting if the project has significantly changed or you believe the previous submission didn't represent it well. Wait at least a month. Change your title and first comment substantially. Don't submit the exact same post twice. Many projects that went unnoticed on first submission have broken through on a second attempt with better positioning."
  - q: "What kinds of projects do well on Hacker News?"
    a: "Developer tools, open source projects, technical infrastructure, AI/ML research projects, and unconventional technical approaches to well-known problems. HN responds strongly to: novel technical architecture, open source code they can inspect, clear articulation of what you built and why, and honest acknowledgment of limitations. Consumer apps, SaaS without technical depth, and marketing-heavy pitches consistently underperform."
hreflang_ja: https://gingiris.github.io/growth-tools/blog/2026/04/07/hacker-news-show-hn-guide-ja/
hreflang_ko: https://gingiris.github.io/growth-tools/blog/2026/04/07/hacker-news-guide-ko/
---

**What is Show HN on Hacker News?** Show HN is a Hacker News submission format for showcasing projects you've built. A successful Show HN front page placement reaches 50,000-200,000 highly technical readers — engineers, CTOs, and startup founders — and can generate 500-2,000 GitHub stars and 1,000+ signups in 24 hours. AFFiNE's Show HN appearance generated 1,200 GitHub stars overnight and drove signups from 3 countries.


Hacker News front page doesn't feel like other traffic spikes.

Reddit gives you volume. Product Hunt gives you votes. HN gives you something harder to measure — engineers who actually read what you built, file specific bug reports, and sometimes email you at midnight with architectural critiques better than anything your own team had raised.

The first time AFFiNE hit the HN front page, we got 300+ comments in 6 hours. Most were useful. Some were brutal. (One commenter wrote a 600-word technical teardown of our CRDT implementation. He was right about most of it.) All of them were from people who'd genuinely tried the product.

This guide is about how to get that kind of attention — and what to do with it when it arrives.

---

## Key Stats

| Metric | Data |
|--------|------|
| Upvotes needed for front page | ~30–50 in first hour |
| Typical front page Show HN total | 200–600 points |
| Best posting time | 9–10 AM ET weekdays |
| HN traffic to GitHub (front page) | 500–2,000 stars |
| AFFiNE HN front page appearances | Multiple (incl. month 12 spike) |
| Comment engagement on strong Show HN | 50–200 comments |
| Grace period (downvote-protected) | First few hours |

---

## TL;DR

- Show HN is the right format — it gets a dedicated queue, downvote grace period, and HN community actively browses it
- Post 9–10 AM ET weekdays; your first 30 minutes determine front page trajectory
- Title format: "Show HN: [What it is] – [one differentiator]" — no hype, no exclamation marks
- First comment = your pitch. Write it before you submit. Technical depth, honest limitations, specific ask
- Respond to every comment in the first 2 hours — engagement velocity matters to the algorithm
- A front page Show HN drives 500–2,000 GitHub stars for OSS tools; traffic drops fast but the HN point signal persists

---

## Why Hacker News Is Different

Most launch platforms optimize for volume. Hacker News optimizes for signal.

The community is ~10 million monthly readers, but the active voting core is a much smaller group of engineers, founders, and researchers who are genuinely hard to impress. They will immediately identify vague claims, marketing language, and anything that doesn't hold up technically. They will also — when something is genuinely interesting — drive it to the front page and generate the kind of discussion that gets your project noticed by journalists, investors, and developers who won't be found anywhere else.

For AFFiNE, Hacker News was part of the coordinated Day 1 launch with Reddit. The initial Show HN coincided with the Reddit push that drove 6,000 GitHub stars in week one. A later HN front page appearance at month 12 produced another significant spike — at that point we already had strong product-market fit, and the HN community could see it in the depth of user comments.

The dynamic is simple: HN doesn't reward polish. It rewards technical honesty and genuine novelty.

---

## The Show HN Format: What It Gets You

When you start a post with "Show HN:", three things happen:

1. **It appears on news.ycombinator.com/shownew** — a dedicated queue that HN regulars browse specifically for new projects to try
2. **It receives a downvote grace period** — new Show HN posts can't be downvoted immediately, giving them time to accumulate genuine interest before criticism
3. **The self-promotion rule doesn't apply** — HN normally discourages posting about your own work; Show HN is the sanctioned exception

There's also an implicit social contract: Show HN posts are expected to be genuinely showing something — a working product, an interesting open source repo, a tool you built. Not a blog post about why you might build something, not a landing page with no product behind it.

If you're launching an open source project or a developer tool with real functionality, Show HN is exactly the right format.

---

## Timing: When to Post

HN's front page algorithm is sensitive to early velocity. You need your core supporters to upvote within the first 30–60 minutes, which means you need them awake and at their computers.

**The optimal window:**
- **Monday–Thursday, 9–10 AM ET** — Peak HN activity. US East Coast engineers are starting work; West Coast is at their desks; European audience is mid-afternoon.
- **Sunday, 10 AM ET** — Second-best option. HN Sunday traffic is slightly lower but the audience is more exploratory. Competition is lower.
- **Avoid:** Friday afternoon, Saturday. Traffic drops and HN's weekend patterns favor long-read content over discovery.

One nuance: Monday has slightly more competition (experienced teams often launch early in the week). If you're concerned about a strong competitor launching the same day, Tuesday or Wednesday reduces collision risk.

**Practical setup:** Have your post drafted, preview it, then schedule your supporters to be ready before you submit. The first 30 minutes after posting are not the time to be sending messages asking people to look at it.

---

## Writing the Title

HN titles are unusually formulaic — and that's a feature, not a bug. The community has optimized the format over years of collective experience.

**The Show HN title format:**

`Show HN: [What it is] – [one specific differentiator]`

**Examples that work:**
- `Show HN: AFFiNE – an open-source Notion alternative with local-first storage`
- `Show HN: A Rust-based database that runs entirely in your browser`
- `Show HN: I rebuilt my photo management app after iCloud raised prices 3x`

**What doesn't work:**
- `Show HN: The future of note-taking is here!` — Hype language gets downvoted reflexively
- `Show HN: We launched our startup` — No technical signal
- `Show HN: Better than Notion` — Comparative claims without basis irritate HN readers
- `Show HN: ProjectName` — No information; nobody will click

The differentiator in your title should be the technically interesting part — the architecture choice, the open source angle, the local-first approach, the specific problem you solved. HN readers are scanning for novelty. Give them a reason to open the tab.

**Title length:** Keep it under 80 characters. Titles that wrap in HN's layout look amateurish.

---

## The First Comment: Your Most Important Asset

On Hacker News, the submitter's first comment is read before the product in most cases. It's visible directly below the title before anyone clicks your link. This is your pitch.

Write it before you submit. Do not improvise it after posting.

**Structure that consistently works:**

1. **What you built, in one sentence** — not the marketing version, the technical version
2. **Why you built it** — a specific, personal problem you faced, not "there was a gap in the market"
3. **The interesting technical choice** — what's architecturally different, why you made that tradeoff
4. **One honest limitation** — this is critical. HN rewards intellectual honesty. Admitting what doesn't work yet signals you're a serious engineer, not a marketer
5. **Specific ask** — what kind of feedback are you looking for?

**Example structure (AFFiNE-style):**

> We've been building AFFiNE for two years — it started as frustration with Notion's sync latency and Obsidian's collaboration limitations. Most of the note-taking tools we tried forced a choice: real-time collaboration OR local-first storage. We wanted both.
>
> The interesting technical piece: we built a conflict-free replicated data type (CRDT) layer underneath the editor so documents can live locally and sync when online, without a centralized server holding your data hostage.
>
> Current limitation: the mobile app is rough. Desktop and web are solid; iOS/Android still has performance issues we're working through.
>
> If you try it, I'm especially curious whether the canvas/block combination makes sense to you or whether it feels like too much — that's the feedback we haven't been able to resolve internally.

Notice: no "check out our amazing tool," no exclamation marks, no feature list. One real problem, one honest limitation, one specific question.

---

## Building Your Support Network Before Launch

The first 30 minutes after posting are what determines your front page trajectory. You need a small group (10–30 people) who are:

1. **Active HN users with karma** — votes from accounts with no history are worth less and are more likely to trigger HN's fraud detection
2. **Genuinely interested in your project** — they'll write comments that help, not hollow "+1 great project" posts that get flagged
3. **Available at the time you post** — timezone coordination matters

**Where to find them:**
- Your existing Discord/Slack community — ask who uses Hacker News
- Twitter/X connections who are engineers or founders
- Personal network of developers you've met at conferences or in communities

**What to ask for:**
> "I'm launching on Hacker News tomorrow at 9 AM ET. Link: [URL]. If it looks interesting to you, any feedback in the comments would mean a lot — I'm trying to figure out [specific question]."

Never say "please upvote." It reads as manipulation — and HN regulars will sometimes actively downvote your post if they see coordinated upvote requests. (I made this mistake once. Not twice.) and HN regulars will sometimes downvote your post specifically if they see coordinated upvote requests. Ask for engagement (comments, feedback) not votes. Genuine engagement produces votes as a byproduct.

---

## Managing the Comments Section

Once your post is live and gaining traction, the comments section is where HN launches succeed or fail.

**Respond within 15 minutes to every substantive comment** in the first 2 hours. HN's algorithm weights comment velocity as a signal of engagement quality. A post with 30 comments and active back-and-forth will continue to surface; a post with 30 comments and no replies from the submitter stalls.

**How to respond:**
- Technical objections: engage seriously. "Good point — we went with X because Y, but you're right that Z is a tradeoff." Don't be defensive.
- Feature requests: "That's on the roadmap / that's not something we've planned — here's why."
- "Why not just use [competitor]?" — The most common HN comment. Have a prepared answer that's honest. Not marketing.
- Genuine compliments: A short thank-you + one piece of additional context keeps the thread active.

**What not to do:**
- Don't argue with critics. If someone is wrong, calmly state the accurate information and move on.
- Don't ask people to upvote in the comments.
- Don't self-promote repeatedly in your own thread. One maker comment + responses only.

A well-managed comment section can sustain a front page post for 18–24 hours. A post where the founder disappears after submitting typically fades in 4–6 hours.

---

## The Technical Depth Requirement

Hacker News has an implicit minimum standard for "technically interesting." Consumer apps, landing pages, and non-technical products routinely underperform — not because HN is elitist, but because the audience is self-selecting toward technical depth.

For developer tools and open source projects, this works strongly in your favor. Things that reliably resonate:

**Architecture choices:** "We replaced [standard approach] with [novel approach] because of [specific constraint]." HN loves reading about tradeoffs.

**Open source code:** Link directly to GitHub. A repo the community can inspect is substantially more trusted than a closed-source product. "You can read the implementation here" is a strong signal.

**Real numbers:** Benchmarks, query speeds, memory usage, scale metrics. Not "10× faster" but "10× faster at 10M rows on an M2 MacBook, benchmark code in /tests."

**Honest failure stories:** "We tried X and it didn't work because Y. So we built Z." HN appreciates intellectual honesty about the path you took.

If your product doesn't have technical depth yet — if it's mostly UI/UX innovation on top of standard infrastructure — wait. HN Show HN is not the right channel until you have something technically interesting to say.

---

## What Happens After Front Page

Traffic from HN front page is fast and focused. Unlike Reddit (broad awareness) or Product Hunt (wide developer audience), HN traffic tends to be:

- High-intent: they clicked through specifically because of the technical angle
- Comment-heavy: expect more GitHub issues, Discord questions, and direct emails per visitor than from other platforms
- Conversion-variable: OSS tools see strong star conversion (500–2,000 stars for a front page appearance); SaaS products see lower trial conversion but higher-quality leads

The traffic pattern: 60% of your HN-referred traffic arrives in the first 6 hours, 80% within 24 hours. By day three, HN traffic is negligible.

**What to prepare before your post goes live:**
- GitHub README updated and star CTA visible
- Email capture on your landing page
- Discord/Slack invite link in your maker comment
- Response drafts for the most predictable comments ("why not X?" "how does this compare to Y?")

**After the spike — the persistent value:**
The HN submission URL (`news.ycombinator.com/item?id=XXXXX`) becomes a permanent link that continues to drive occasional traffic for months. Developers who search for your product category sometimes land on old HN threads. A well-commented thread with substantive discussion is evergreen content.

More importantly: journalists and investors regularly monitor HN for interesting projects. A front page appearance with 200+ points is visible in their HN monitoring. The AFFiNE launch threads contributed to several inbound media mentions that wouldn't have found us otherwise.

---

## Show HN vs. Other HN Formats

**Show HN** — for working products, tools, open source projects. Use this.

**Ask HN** — for genuine questions where you want community input. Sometimes appropriate pre-launch ("Ask HN: Best architecture for [problem]?"). Don't pitch your product in an Ask HN.

**Regular submission** — for blog posts, technical articles, research. If you write a "how we built X" post about your project, you can submit the article as a regular link. This is a second-bite approach: write a deep technical post about your project 2–4 weeks after your Show HN, then submit the article. Different format, different audience, second exposure.

One useful pattern: **Show HN on launch → technical blog post 2–3 weeks later → submit blog post.** The first submission establishes you in the HN community; the blog post submission reaches people who missed the original Show HN.

---

## Checklist: Day Before, Launch Day, Follow-Up

**Day before:**
- [ ] Write your first comment (the pitch) and save it
- [ ] Prepare answers to the 5 most predictable technical objections
- [ ] Alert 10–20 genuine supporters to be available at posting time
- [ ] Ensure GitHub README has a clear star CTA and demo link
- [ ] Set up email capture on landing page

**Launch day (post at 9–10 AM ET):**
- [ ] Submit with correct title format: "Show HN: [What] – [differentiator]"
- [ ] Immediately post your first comment
- [ ] Notify supporters with the live link
- [ ] Respond to every substantive comment within 15 minutes for the first 2 hours
- [ ] Monitor HN ranking — if you're not front page within 1 hour, consider whether to resubmit another day

**Follow-up (days 2–7):**
- [ ] Write a "we just launched Show HN" post in relevant Reddit communities (link to HN thread, not product page)
- [ ] Thank people who commented with direct replies or DMs if they left contact info
- [ ] Begin drafting your technical blog post for submission in 2–4 weeks
- [ ] Check GitHub issues — HN users file detailed bug reports and feature requests

---

## Common Mistakes That Kill Show HN Posts

**Marketing language in the title.** "Revolutionary," "game-changing," "10× better" — these phrases trigger HN's collective allergic response. Describe, don't hype.

**Not being available for the first 2 hours.** Post at a time when you can monitor and respond. Posting at midnight in your timezone because "that's 9 AM ET" and then sleeping means your launch window passes without engagement.

**Submitting before the product is ready.** HN users will try your product immediately. If the onboarding is broken, if the demo doesn't work, if it's clearly not ready — the comments will reflect that, and those comments are permanent.

**Posting to your own account with no karma.** A fresh account submitting a Show HN looks like marketing. If possible, have someone with HN karma and genuine community standing submit on your behalf, or build up some HN karma by commenting substantively on other posts before your launch.

**Ignoring the thread.** The single most common mistake. You post, it gains traction, and then you're unavailable for 4 hours. The engagement dies, the ranking drops, the opportunity closes. Block your calendar for the morning of your launch.

---

## 📚 Related Reading

| Category | Article |
|----------|---------|
| 📖 | [How to Get More GitHub Stars: The Definitive Guide](https://gingiris.github.io/growth-tools/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/) |
| 📖 | [How to Get on GitHub Trending](https://gingiris.github.io/growth-tools/blog/2026/04/06/how-to-get-on-github-trending/) |
| 📖 | [Product Hunt Launch: The 2026 Playbook](https://gingiris.github.io/growth-tools/blog/2026/03/18/product-hunt-launch-the-2026-playbook-for-winning-1/) |
| 📖 | [Reddit Marketing Without Getting Banned](https://gingiris.github.io/growth-tools/blog/2026/03/30/reddit-marketing-guide-how-to-promote-without-getting-banned/) |
| 📖 | [GitHub Star Growth: 10 Proven Tactics](https://gingiris.github.io/growth-tools/blog/2026/03/27/github-star-growth-10-proven-tactics-that-got-us-33k-stars/) |

*More tools → [Growth Tools Directory](https://gingiris.github.io/growth-tools/)*

## Key Takeaways

- **Title is 90% of success**: factual, specific, no hype — include tech stack and a clear comparator
- **Post at 7-9 AM Pacific Time** (11 PM-1 AM JST) on Tuesday-Thursday for maximum front page probability
- **Post a founder comment immediately** explaining your "why" — HN rewards authenticity and technical depth
- **Build karma first**: contribute quality comments for 3+ months before your big launch
- **Respond to criticism constructively** — defensive replies tank posts; thoughtful responses can save them
- HN readers are **CTOs, engineers, and investors** — one front page post can be worth months of other marketing

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do you get on the Hacker News front page?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "To get on the Hacker News front page: (1) Write a title that is factual and specific — avoid hype, include the tech stack and a concrete differentiator, (2) Submit between 7-9 AM Pacific Time on weekdays for peak US traffic, (3) Post a founder comment immediately after submission explaining your motivation and technical decisions, (4) Have 3-5 colleagues upvote within the first 30 minutes to trigger algorithmic momentum, (5) Build HN karma beforehand by contributing quality comments for 3+ months. Accounts with higher karma have their posts weighted more heavily."
      }
    },
    {
      "@type": "Question",
      "name": "What makes a good Show HN title?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A good Show HN title is factual, specific, and includes: (1) What the product does in plain language, (2) The tech stack or key technical detail if relevant, (3) A comparison to known products if it helps understanding. Good example: 'Show HN: AFFiNE – An open-source Notion/Miro alternative written in TypeScript'. Bad example: 'Show HN: The best note-taking app you've ever seen'. HN readers are technical and distrust marketing language."
      }
    },
    {
      "@type": "Question",
      "name": "What is the best time to post on Hacker News?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The best time to post on Hacker News is between 7 AM and 10 AM Pacific Time (PT) on Tuesday, Wednesday, or Thursday. This aligns with US East Coast morning (10 AM-1 PM ET) when traffic peaks. In Japan Standard Time (JST), this is 11 PM to 2 AM JST. Avoid weekends and Monday mornings. Posts submitted during peak hours have 3x higher front page probability than off-peak submissions."
      }
    },
    {
      "@type": "Question",
      "name": "How much traffic does a Hacker News front page post get?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A Hacker News front page post typically generates 5,000-50,000 unique visitors in 24 hours depending on rank and time on front page. Top 3 positions can drive 100,000+ visitors. The audience is high quality: primarily software engineers, technical founders, and investors. AFFiNE's HN appearance drove 1,200 GitHub stars and significant developer signups in a single day — quality of traffic is often more valuable than quantity."
      }
    }
  ]
}
</script>
