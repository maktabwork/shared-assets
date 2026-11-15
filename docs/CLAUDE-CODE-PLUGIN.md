# Monjizeen plugin for Claude Code (`mo@monjizeen`)

Account managers and Kawader reviewers work on client tickets in Claude Code
with this plugin: our client-work skills, plus the Monjizeen connector that
posts the work, HTML deliverable, time and tokens to the ticket. The app runs
no AI. How the app side works: monjizeen-app `docs/CLAUDE_CODE_WORK.md`.

The plugin lives in the private GitHub repo **`monjizeen/tools`**. It holds only
the plugin (no other skills, client files or workflows), so account managers
get read access to that repo alone.

## Set up a new account manager (admin, once)

1. **Claude account**: give them a Claude account (Pro, Max or a Team seat)
   paid by the company.
2. **GitHub**: they need a GitHub account. Add it to the GitHub team
   **account-managers** in the monjizeen organization
   (github.com/orgs/monjizeen/teams/account-managers → Add a member). That
   team has **Read** on `monjizeen/tools` only.
3. **Monjizeen**: make them the account manager of each client organization
   they serve.

## Set up on their computer (account manager, once)

1. **Sign Claude Code in to GitHub**, so it can download the private plugin.
   Claude Code uses the computer's own git sign-in. The easiest is the GitHub
   CLI: install it, run `gh auth login`, choose GitHub.com and HTTPS, and say
   yes to "Authenticate Git with your GitHub credentials". Check with
   `git ls-remote https://github.com/monjizeen/tools` (it lists refs, no error).
   For automatic plugin updates in the background, also set `GITHUB_TOKEN`
   in their shell profile, e.g. `export GITHUB_TOKEN=$(gh auth token)`.
2. **One Monjizeen key per client**: in Monjizeen, Settings → API keys → New
   key, limited to **one** organization (the client). An account manager with
   two clients makes two keys. A key for no or several organizations is
   refused by the work tools. Copy the key once; it is shown only then.
3. **Install** in Claude Code:
   ```
   /plugin marketplace add monjizeen/tools
   /plugin install mo@monjizeen
   ```
   It asks for the Monjizeen key and keeps it in the system's secure store.
   Restart Claude Code.
4. **Switch client**: run `/plugin configure mo@monjizeen` and paste that
   client's key. Keep one folder per client and work on one client at a time.
5. **Check**: ask "show my review queue". It should answer from Monjizeen
   (an empty queue is fine).

Updates: `/plugin update mo@monjizeen` (or automatic with `GITHUB_TOKEN`).

## Daily use

- "Work on https://app.monjizeen.com/tickets/123": the `monjizeen-ticket`
  skill starts the work, applies the client context and lessons, delivers one
  HTML page and posts it back.
- Reviewers: "review queue", then "retest step 45".

## Removing someone

Remove them from the **account-managers** team (no plugin updates) and revoke
their Monjizeen keys (Settings → API keys, or remove them as account manager).
The connector stops at once.

## How it is built (Monjizeen team)

- Sources in `monjizeen/shared-assets`: `plugin/plugin.json` (connector and key
  prompt), `plugin/marketplace.json`, `plugin/hooks/` (adds the tokens used
  since `start_work` to `finish_work`), and the skills listed in
  `plugin/skills.txt`.
- `scripts/build-plugin.sh <dir> [version]` builds the repo's content;
  `.github/workflows/publish-plugin.yml` publishes it to `monjizeen/tools` on
  every change to main (version `0.1.<run>`). It needs the secret
  `TOOLS_REPO_TOKEN`: a fine-grained token with Contents read and write on
  `monjizeen/tools` only.
