# Deploy growth-tools to blog.gingiris.com

> Migrated from `gingiris.github.io/growth-tools` (404'd after GitHub spam-flag) to independent Cloudflare Pages deploy at `blog.gingiris.com`.

## Recommended: Cloudflare Pages

**Why CF Pages over Vercel for this**: native Jekyll auto-detect (no config needed), unlimited bandwidth on free tier, China-friendly CDN, no cold-start.

### One-time setup (Iris does this, ~10 min)

1. **Cloudflare account** → Pages → Create Project → **Connect to Git**
2. Authorize the **new** GitHub account (`Gingiris-1031`)
3. Select repo: `Gingiris-1031/growth-tools`
4. Build settings (auto-detected):
   - **Framework preset**: Jekyll
   - **Build command**: `bundle install && bundle exec jekyll build`
   - **Build output directory**: `_site`
   - **Root directory**: `/` (default)
   - **Environment variables**:
     - `RUBY_VERSION` = `3.2.3`
     - `BUNDLE_PATH` = `vendor/bundle`
5. **Save and Deploy** — first build takes 2-5 minutes
6. Once green: **Custom domains** → Set up → enter `blog.gingiris.com`
7. CF will give you a CNAME record. Go to Namecheap → Advanced DNS → add:
   - **Type**: CNAME
   - **Host**: `blog`
   - **Value**: `<the cf pages domain>.pages.dev`
   - **TTL**: Automatic
8. Wait 5-30 min for DNS propagation + SSL cert auto-issued

### Verify

```bash
curl -I https://blog.gingiris.com/
# Should return HTTP 200 with `server: cloudflare`

curl -s https://blog.gingiris.com/blog/2026/04/03/saas-marketing-guide/ | head -5
# Should return the saas marketing post HTML (preserves URL structure)
```

## Alternative: Vercel

If you prefer Vercel: same connect-repo flow, but Vercel requires manual Jekyll setup since it's not first-class. Use the `Gemfile` already in this repo + set:
- Framework Preset: Other
- Build command: `bundle install && bundle exec jekyll build`
- Output directory: `_site`
- Install command: leave blank (Vercel auto-detects Gemfile)

## After deploy

1. **Tell Google about new URLs**: GSC → add property `blog.gingiris.com` → submit `https://blog.gingiris.com/sitemap.xml`
2. **301 from old (if you regain access to gingiris.github.io)**: Add a `_redirects` file at repo root with `/* https://blog.gingiris.com/:splat 301`
3. **Update dev.to canonical_url** (where they currently point at `gingiris.github.io/growth-tools/blog/...`): batch PATCH via dev.to API
4. **Update analook.com cross-links** (already done in commit `ae91fa7`, points to dev.to fallback)

## Rollback / what's not affected

- **dev.to articles still work** — independent of GitHub
- **analook.com** — unaffected (deployed on Railway from a separate repo)
- **MCP Registry listing** — uses `io.github.Gingiris/analook` name (will need update if we transfer the analook repo)
