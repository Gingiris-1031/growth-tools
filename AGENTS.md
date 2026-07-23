# Repository operating rules

## GitHub account safety red lines (P0)

- The only active GitHub identity is `Gingiris-1031`; never add links or
  references to the suspended legacy account.
- Use `Iris Wei <iris.wei@gingiris.com>` for commits, with one natural,
  single-line message and no AI/co-author trailer.
- Batch reviewed site changes into one commit and at most one push per release
  window. Never create daily SEO commits or scheduled daily GitHub workflows.
- Never enable GitHub Pages for this repository; production is deployed by
  Vercel from `main`.
- Inspect the dirty worktree before editing. Stage explicit files only and never
  use `git add .`.
- Never commit credentials, `.env` files, local agent settings, OAuth files, or
  generated secrets. Git remotes must not contain embedded tokens.
- Never force-push or rewrite published history. Fetch before committing and
  stop if local and remote histories diverge.
- Before committing, run the site build, `git diff --cached --check`, and a
  staged secret/account-reference scan.
- Do not batch-write more than five repositories per hour, exceed ten commits
  per hour, create more than one repository per week, automate stars/follows,
  or mass-open external pull requests.
