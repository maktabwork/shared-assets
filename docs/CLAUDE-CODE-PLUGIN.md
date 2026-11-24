# Monjizeen plugin for Claude Code (`mo@monjizeen`)

Account managers and Kawader reviewers work on client tickets in Claude Code
with this plugin: our client-work skills, plus the Monjizeen connector that
posts the work, HTML deliverable, time and tokens to the ticket. The app runs
no AI. How the app side works: monjizeen `docs/CLAUDE_CODE_WORK.md`.

The plugin lives in the private GitHub repo **`maktabwork/plugins`**. It holds only
the plugin (no other skills, client files or workflows), so account managers
get read access to that repo alone.

## Set up a new account manager (admin, once)

1. **Claude account**: give them a Claude account (Pro, Max or a Team seat)
   paid by the company.
2. **GitHub**: they need a GitHub account. Add it to the GitHub team
   **account-managers** in the monjizeen organization
   (github.com/orgs/maktabwork/teams/account-managers → Add a member). That
   team has **Read** on `maktabwork/plugins` only.
3. **Monjizeen**: make them the account manager of each client organization
   they serve.

## Set up on their computer (account manager, once)

1. **Sign Claude Code in to GitHub**, so it can download the private plugin.
   Claude Code uses the computer's own git sign-in. The easiest is the GitHub
   CLI: install it, run `gh auth login`, choose GitHub.com and HTTPS, and say
   yes to "Authenticate Git with your GitHub credentials". Check with
   `git ls-remote https://github.com/maktabwork/plugins` (it lists refs, no error).
   For automatic plugin updates in the background, also set `GITHUB_TOKEN`
   in their shell profile, e.g. `export GITHUB_TOKEN=$(gh auth token)`.
2. **One Monjizeen key per client**: in Monjizeen, Settings → API keys → New
   key, limited to **one** organization (the client). An account manager with
   two clients makes two keys. A key for no or several organizations is
   refused by the work tools. Copy the key once; it is shown only then.
3. **Install** in Claude Code:
   ```
   /plugin marketplace add maktabwork/plugins
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

Installing the plugin gives the account manager **Mo**, our agent, not just
the skills. Mo is the entry point; the Maharat skills are what it uses.

- `/mo https://app.monjizeen.com/tickets/123` (or "Mo, work on ticket 123"):
  Mo reads the ticket and the client's Seyaq, says what it understood and
  waits for the OK, then delivers one requirement at a time as HTML pages,
  posting each step to the ticket with time and tokens, and saves new client
  learnings.
- To run a clear ticket in the background while you do something else: "ask
  the mo agent to do ticket 123". It reports back what it posted.
- Reviewers: `/mo review queue`, then "retest step 45".
- The Maharat skills still work on their own (for example `/ux-audit`), but
  only Mo posts the work to the ticket.

## Removing someone

Remove them from the **account-managers** team (no plugin updates) and revoke
their Monjizeen keys (Settings → API keys, or remove them as account manager).
The connector stops at once.

## How it is built (Monjizeen team)

- Sources in `maktabwork/shared-assets`: `plugin/plugin.json` (connector and key
  prompt), `plugin/marketplace.json`, `plugin/agents/mo.md` (Mo for background
  runs), `plugin/agents/lead-*.md` (the leads: one specialist per skill area,
  built on Claude Code subagents, that Mo calls from a task; each loads one
  existing skill, so a skill is never rewritten for a lead), `plugin/hooks/` (adds the tokens used
  since `start_work` to `finish_work`), and the skills listed in
  `plugin/skills.txt` (`skills/mo` is Mo itself).
- `scripts/build-plugin.sh <dir> [version]` builds the repo's content;
  `.github/workflows/publish-plugin.yml` publishes it to `maktabwork/plugins` on
  every change to main (version `0.1.<run>`). It pushes over SSH with a deploy
  key: a write deploy key on `maktabwork/plugins` only, whose private key is the
  Actions secret `PLUGINS_DEPLOY_KEY` in shared-assets. Until that secret
  exists the workflow skips with a notice.
