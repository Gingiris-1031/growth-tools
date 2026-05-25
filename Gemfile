source "https://rubygems.org"

# Cloudflare Pages and Vercel default Jekyll setup.
# Cloudflare Pages auto-detects this Gemfile and runs `bundle install && bundle exec jekyll build`.
gem "jekyll", "~> 4.3"

group :jekyll_plugins do
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
  gem "jekyll-feed"
  gem "jekyll-paginate"
end

# Required on platforms without native Ruby `webrick` (Jekyll 4 dropped the default dep)
gem "webrick"

# Lock to a tested Ruby version for reproducible builds
ruby ">= 3.2"
