---
layout: post
title: "Adding a Remote MCP Server to Our SaaS in 200 Lines — and the 3 Bugs That Almost Shipped"
date: 2026-04-29 14:00:00 +0800
categories: [saas, mcp, dev]
description: "How we exposed Analook's competitor-analysis pipeline to Claude Desktop and Cursor as a Remote MCP server — including the 3 silent failures we caught only because we ran an independent code review on every change."
canonical_url: https://gingiris.tools/blog/2026/04/29/mcp-server-saas-200-lines-3-bugs/
---

It was 11:47 PM on a Sunday in April 2026. I was in my Kunshan apartment, my second matcha gone cold next to the laptop, watching a `curl` command return `HTTP 405 Method Not Allowed` from `https://www.analook.com/mcp` — the endpoint I'd just shipped 90 seconds ago.

The MCP integration was supposed to be the thing that let our 39-user-deep SaaS punch above its weight. Adding `https://www.analook.com/mcp` to a Claude Desktop config and getting a structured competitor report inside the agent context — that's the kind of feature that gets you onto Smithery, into directories, and into the hands of the AI builders who don't want to context-switch out of their editor.

But the curl was 405-ing. And it 405-ed for the next 47 minutes.

This post is what I actually shipped — the architecture, the 3 silent failures we caught only because we ran independent code reviews on every change, and the 200 lines that ended up in production.

## Key Stats

| Metric | Value |
|---|---|
| Lines of MCP code | 280 (`modules/mcp_app.py`) |
| Tools exposed | 5 (`analyze_competitor`, `get_report_status`, `get_report`, `get_report_markdown`, `list_my_reports`) |
| Transport | Streamable HTTP (MCP protocol 2026-04 / 2024-11-05) |
| Critical bugs caught pre-deploy | 3 (review-found) |
| Critical bugs caught post-deploy | 1 (Railway env var trailing space) |
| Time from "done" to actually working | ~6 hours |
| Listed on official MCP Registry | Yes — `io.github.Gingiris/analook` |

## What We Were Trying to Do

[Analook](https://www.analook.com/) is a competitor-analysis SaaS. You paste a URL, we pull data from 15+ sources (DataForSEO, TwitterAPI.io, Product Hunt, GitHub, Wayback Machine, etc.), and you get back a structured report with an AI verdict — *killer move*, *growth pattern*, *replicability*.

The problem: every time someone wanted to use it inside an agent loop, they had to call our REST API by hand. POST `/api/analyze`, poll `/api/v1/status/{id}`, fetch `/api/v1/report/{id}`. Three round-trips, manual JSON parsing, and the agent doesn't know what tools we have unless you spell it out.

MCP solves this. One config block, the agent introspects, and `analyze_competitor("lovable.dev")` Just Works inside Claude Desktop.

So I sat down to write it.

## The Plan

1. Use FastMCP's `streamable_http_app()` to mount an MCP HTTP transport
2. Wrap with a Starlette middleware that grabs `Authorization: Bearer` headers into a `ContextVar`
3. Mount it at `/mcp` on the existing FastAPI app
4. 5 tools, each calling the same internal logic the HTTP API uses

Sounded clean. Wasn't.

## Bug 1: The `progress` Schema Crash

Our code review (we use a discipline of running every diff through an independent agent that doesn't share context with the writer) flagged this immediately:

> **P1 — broken `progress` schema**: `analyze_competitor` writes `"progress": "🌐 排队中…"` (a string), but the existing `_run_analysis` does `job["progress"]["website"] = "running"` expecting a **dict**. Will crash on first progress update.

The MCP-submitted jobs would have crashed silently in the background task. The user would get a `job_id`, poll status, see `"running"` forever, and never know why.

Fix: copy the schema *exactly* from the HTTP path — the dict structure with 9 module keys. Not "approximate", not "similar", *exactly*.

```python
jobs[job_id] = {
    "status": "running",
    "progress": {
        "website": "pending",
        "social": "pending",
        # ... 7 more keys, all required
    },
    "results": {},
    # ...
}
```

Lesson: when two code paths share state, the schema is the contract. Treat schema drift like an API breaking change.

## Bug 2: The 8-Character UUID

Same review pass:

> **P1 — job_id collision**: `uuid.uuid4().hex[:8]` gives ~4B IDs, but the jobs dict is shared with HTTP-originated job_ids. Use full `uuid.uuid4().hex`.

A simple bug. But the symptom in production would have been: two users get the same job_id, and one user sees the other's report. **A privacy leak**, not a crash.

Fix:

```python
job_id = uuid.uuid4().hex
while job_id in jobs:
    job_id = uuid.uuid4().hex
```

Lesson: short IDs are fine for opaque slugs. They are not fine for auth-relevant identifiers in a shared dict. (I made this mistake once. Not twice.)

## Bug 3: The SSRF That Wasn't (Quite)

> **P2 — `normalize_url_or_raise` is dead code**: function doesn't exist; the fallback uses stdlib `urlparse` which accepts `file://`, `javascript:`, `http://localhost:8080/admin`. `_run_analysis` then **fetches** that URL.

The MCP `analyze_competitor` tool takes a URL from the user. Without scheme validation, an attacker calling `analyze_competitor("file:///etc/passwd")` would have made our backend fetch and try to "analyze" the local password file. Not exploitable for arbitrary read in our setup, but it was the kind of thing that ages badly.

Fix: explicit scheme allowlist before any fetch.

```python
if parsed.scheme not in ("http", "https"):
    return {"error": "INVALID_URL", "hint": "Only http/https URLs are supported"}
```

Lesson: every user-supplied URL that gets fetched server-side is an SSRF candidate until you've allowlisted the scheme *and* validated the host.

## The Bug We Didn't Catch in Review (Production Found It)

Three days after shipping, I tried to demo the MCP integration to myself. Got back `Server analook unable to connect`. Checked `/mcp` — `HTTP 404`.

Six hours of debugging later, the answer:

In Railway's dashboard, the environment variable was named:

```
SUPABASE_SERVICE_KEY    (with a trailing space)
```

You can't see trailing spaces in Railway's UI. Python's `os.environ.get("SUPABASE_SERVICE_KEY")` doesn't match `"SUPABASE_SERVICE_KEY "`. So the supabase client init returned `None`. So `_require_credits` fell through its "no Supabase = dev mode" branch. So MCP auth tools all returned `AUTH_REQUIRED`. So `save_report_to_db` silently no-op'd.

Three weeks of users had been running analyses where the report only ever lived on Railway's ephemeral container disk and got wiped on every redeploy.

The fix was a one-liner. The damage was 5 lost reports, including one from a real external user.

I wrote up the full diagnosis and pushed a `/api/debug/auth` endpoint that lists all `SUPABASE_*` environment variable keys (so trailing spaces become visible). Then I added a `_service_degraded_response()` helper that **refuses** with `HTTP 503` when `SUPABASE_URL` is set but the client failed to init — no more silent fallback to dev mode.

Lesson: any time your code has an `if config_present: real_path else: dev_mode_fallback` branch, the failure mode of "config is *kind of* present but broken" needs a third path. Otherwise you ship to prod and discover the bug three weeks later from your weekly metrics report.

## What's Live Now

Five tools, behind one `https://www.analook.com/mcp` URL:

```json
{
  "mcpServers": {
    "analook": {
      "url": "https://www.analook.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_ANALOOK_TOKEN>"
      }
    }
  }
}
```

Drop that into `~/Library/Application Support/Claude/claude_desktop_config.json`, restart Claude, and ask:

> "Use analook to analyze lovable.dev, then compare it side-by-side with linear.app and notion.so."

Claude will call `analyze_competitor` three times in parallel, poll `get_report_status` until done, fetch each report, and synthesize the comparison. Three minutes, 3 credits, one prompt.

Full setup docs at [analook.com/docs/mcp](https://www.analook.com/docs/mcp.html). Source code at [www.analook.com](https://www.analook.com).

## Three Things I'd Tell Past-Me

**1. Run independent code review on every commit, especially MCP-shaped ones.**
The agent that writes the code is the wrong agent to review it. We caught all 3 P1s before deploy because the reviewer didn't know what we'd intended — only what we'd written.

**2. Trailing spaces are real.**
Anywhere a string identifier gets typed by a human into a UI, treat trailing-space contamination as a default failure mode. Add `.strip()` in the reader, expose the *exact* keyset in a debug endpoint, and surface degraded states explicitly.

**3. The smallest MCP server that's actually useful is bigger than you think.**
The 5 tools I shipped are 280 lines of Python plus a Starlette wrapping layer plus a contextvar middleware plus 4 routes' worth of error mapping plus session + lifespan plumbing for FastMCP. The "200 lines" in the title was aspirational — by the time I had production-ready auth + structured errors + a deploy that didn't 404, it was 280.

That's still small. But it's not the "5-line hello world" the demos suggest.

---

If you're building an MCP server for your own SaaS, [I'm happy to chat](https://gingiris.com/en) — I do open-source growth consulting and this is the kind of thing I think about full-time. The Analook MCP itself is on the [official MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=analook) under `io.github.Gingiris/analook`.

*Written by [Iris](https://gingiris.com/en) — ex-AFFiNE COO, 60k GitHub stars, 30x Product Hunt #1.*
*Last updated: April 2026*
