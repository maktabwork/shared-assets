# Monjizeen plugin for Claude Code

Account managers (and Kawader reviewers) work on client tickets in Claude Code
with this plugin: all our skills, plus the Monjizeen connector that posts the
work, HTML deliverable, time and tokens to the ticket. The app runs no AI.
How the app side works: monjizeen-app `docs/CLAUDE_CODE_WORK.md`.

## Set up (once per person)

1. Claude account: the company gives the account manager a Claude account
   (Pro, Max or Team seat) paid by the company.
2. GitHub: read access to `monjizeen/shared-assets` (this repo is the
   plugin's marketplace).
3. Monjizeen key: in the app, **Settings → API keys** → new key (no expiry or
   a long one). Copy it once.
4. In Claude Code:
   ```
   /plugin marketplace add monjizeen/shared-assets
   /plugin install monjizeen@monjizeen
   ```
   It asks for the Monjizeen API key and keeps it in the system's secure store.
   Restart Claude Code.
5. Check: ask "list my review queue". It should answer from Monjizeen (an
   empty queue is fine).

Update later with `/plugin update monjizeen@monjizeen`.

## Daily use

- "Work on https://app.monjizeen.com/tickets/123" → the `monjizeen-ticket`
  skill starts the work, applies the client context and lessons, delivers one
  HTML page and posts it back.
- Reviewers: "review queue", then "retest step 45".

## What is in it

- `.claude-plugin/plugin.json`: the connector (`https://app.monjizeen.com/mcp`
  with the person's key) and the key prompt.
- `skills/`: every skill in this repo, loaded automatically.
- `hooks/add-tokens.js`: before `finish_work`, adds the tokens used since
  `start_work` from the Claude Code transcript.
