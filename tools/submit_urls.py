#!/usr/bin/env python3
"""
Gingiris Blog — Batch URL Submission Tool
==========================================
Submits all blog post URLs to IndexNow (Bing / Yandex / Seznam).

Google's Indexing API is intentionally not used here: ordinary blog and
landing-page URLs must be discovered through the sitemap or inspected in GSC.

Usage:
  # Submit all posts
  python3 tools/submit_urls.py

  # Dry-run: just print URLs
  python3 tools/submit_urls.py --dry-run

The script reads the already-published IndexNow key from the production site;
it never creates or stores a new secret locally.
"""

import os, re, sys, json, argparse, ssl
import urllib.request, urllib.error

# ── Config ────────────────────────────────────────────────────────────────────
SITE_URL      = "https://tools.gingiris.com"
POSTS_DIR     = os.path.join(os.path.dirname(__file__), "..", "_posts")
INDEXNOW_HOST = "tools.gingiris.com"
INDEXNOW_KEY_LOCATION = f"https://{INDEXNOW_HOST}/gingiris-indexnow-20260403.txt"


def tls_context():
    """Use certifi when available; otherwise keep the platform trust store."""
    try:
        import certifi
    except ImportError:
        return ssl.create_default_context()
    return ssl.create_default_context(cafile=certifi.where())


TLS_CONTEXT = tls_context()

# ── Helpers ───────────────────────────────────────────────────────────────────

def extract_canonical_urls():
    """Read all _posts/*.md and return a list of unique canonical_url values."""
    urls = []
    seen = set()
    pattern = re.compile(r'^canonical_url:\s*(.+)$', re.MULTILINE)

    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith(".md"):
            continue
        with open(os.path.join(POSTS_DIR, fname)) as f:
            content = f.read(3000)  # only need front matter

        m = pattern.search(content)
        if m:
            url = m.group(1).strip().strip('"').strip("'")
            if url not in seen:
                seen.add(url)
                urls.append(url)

    # Filter: only include URLs pointing to this site (skip intentional
    # canonicals to other domains)
    own_urls = [u for u in urls if SITE_URL in u]
    return own_urls


def get_indexnow_key():
    """Read the already-published IndexNow key; never generate an unusable key."""
    with urllib.request.urlopen(
        INDEXNOW_KEY_LOCATION, timeout=15, context=TLS_CONTEXT
    ) as resp:
        key = resp.read().decode().strip()
    if not key:
        raise RuntimeError(f"empty IndexNow key at {INDEXNOW_KEY_LOCATION}")
    return key


def submit_indexnow(urls, key):
    """Submit URLs to IndexNow (Bing endpoint covers Bing + Yandex + others)."""
    endpoint = "https://api.indexnow.org/indexnow"
    payload = {
        "host": INDEXNOW_HOST,
        "key": key,
        "keyLocation": INDEXNOW_KEY_LOCATION,
        "urlList": urls,
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        endpoint,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15, context=TLS_CONTEXT) as resp:
            status = resp.status
    except urllib.error.HTTPError as e:
        status = e.code
    except Exception as e:
        print(f"[IndexNow] ERROR: {e}")
        return False

    if status in (200, 202):
        print(f"[IndexNow] ✅ Submitted {len(urls)} URLs → status {status}")
        return True
    else:
        print(f"[IndexNow] ⚠️  Unexpected status {status}")
        return False


def print_urls(urls):
    print(f"\n{'─'*60}")
    print(f"  {len(urls)} URLs to submit")
    print(f"{'─'*60}")
    for u in urls:
        print(f"  {u}")
    print(f"{'─'*60}\n")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Batch URL submission to search engines")
    parser.add_argument("--dry-run",       action="store_true", help="Print URLs only, don't submit")
    args = parser.parse_args()

    urls = extract_canonical_urls()
    print_urls(urls)

    if args.dry_run:
        print("Dry-run mode — no submissions made.")
        return

    key = get_indexnow_key()
    submit_indexnow(urls, key)


if __name__ == "__main__":
    main()
