# Maharat (مهارات): skills

What each skill can do: its inputs, method, outputs and limits. Part of the
three layers described in the [repo README](../README.md#ai-workforce-maharat-adwar-masarat):
skills here, roles in [`../roles/`](../roles/), workflows in [`../workflows/`](../workflows/).

All custom skills live here — versioned on GitHub. **Do not edit copies** under `~/.claude/skills/` or `~/.cursor/skills/`.

## Skills

| Skill | Purpose |
|-------|---------|
| `start-work` | Sync main (QUICK) or confirm branch (WORKTREE); challenge scope before coding |
| `finish-work` | Test, commit, push when done — no auto PR or merge |
| `cleanup` | Sync main, prune branches, clean local git state |
| `new-project` | **Canonical** — bootstrap new repo: stack, GitHub, scaffold, repo list, OAuth, mnjz.in DNS/VPS |
| `init-project` | Alias for `new-project` |
| `pre-mvp-audit` | Pre-launch codebase audit tied to core user loop |
| `security-check` | Weekly security sweep of all repos and live sites; fixes safe issues, reports risky ones |
| `align-project-docs` | Keep a project's description, brief in the app and README in line; create projects through the Monjizeen MCP |
| `refresh` | Sync **active workspace** repo — pull, deps, migrate, restart dev server |

### Service skills

Our methods and standards for each service Monjizeen sells. Client context
plugs in through `client-context-brief`. Plan and status: [SERVICES.md](SERVICES.md).

**Rule for every service skill:** what a client or owner reads is a visual
HTML page with its screenshots, made with `html-deliverable`, never a
Markdown file. Markdown stays for our own notes.

| Skill | Purpose |
|-------|---------|
| `understand-requirements` | First step on a ticket: say back what will be built in short bullets, split into requirements delivered one at a time, with the skill for each (Maher) |
| `client-context-brief` | Build a client's kit at onboarding and turn it into a one-page brief per task |
| `social-media-graphic` | Social post, carousel, story and ad graphics, Arabic and English |
| `agent-requests` | Work the requests client agents send through our MCP: skills + context, do the work, QA, deliver; internal test flights |
| `qa-reviewer` | Check every delivery against the brief, context, CHECKs and our learnings before the client sees it |
| `feedback-auditor` | Sort client feedback into client-specific, global or disagree; we review before any skill changes |
| `org-environment` | Onboard, run and cut off a client org's Environment (the NAME = value keys our agents use), with setup prompts for us and for the org's own agent (Monjizeen MCP) |
| `html-deliverable` | Hand any deliverable over as one visual HTML page; findings template with screenshots, filter chips and an AR / EN switch |
| `mo` | Mo, our agent in Claude Code: reads a ticket and the client's Seyaq, agrees the understanding, delivers one requirement at a time as HTML, posts each step with time and tokens, saves client learnings, runs retests (plugin `mo@monjizeen`, see docs/CLAUDE-CODE-PLUGIN.md) |
| `get-to-the-point` | House writing rule for every message, summary and deliverable: the point first, no filler, no walls of text, no jargon, every fact kept (built into Mo, checked by `qa-reviewer`) |
| `page-screenshots` | Readable page screenshots: first screen plus the page in sections under the 8,000 px image limit, desktop and phone, after scrolling; red-boxed evidence crops |
| `ux-audit` | Usability review of a live product or prototype: ranked findings, each with its screenshot and a concrete fix |
| `implementation-review` | Check a build against what was asked (ticket, requirements, earlier comments): done, partly, wrong, missing, not asked for |
| `design-qa` | Check a build against the approved design frames and design comments: done, wrong, missing |
| `ux-feature-spec` | Feature or "Research" task to a UX spec: flow, states, rules, texts, definition of done |
| `ui-screen-design` | Screens and dashboards in Figma or hi-fi HTML, every state, both languages |
| `design-system-pattern` | One design-system component, pattern or template: usage rules and decision table |
| `information-architecture` | Content, navigation, labels and what to lead with per audience |
| `ux-writing` | Interface texts (buttons, errors, notices) in Arabic and English |
| `ux-ticket-writer` | Design tickets and epics in the client's format, with a checkable definition of done |

## Install

On a Mac, `scripts/init-project/bootstrap-mac.sh` links every skill here (and
every role in `../roles/`) into
`~/.cursor/skills/` and `~/.claude/skills/`. Claude project threads read them
straight from this repo. (MORA's `run-mora.sh` used to do this; MORA was retired
on 2026-11-01. The repo list is now [`../docs/REPOS.md`](../docs/REPOS.md).)

## Manual symlink (if needed)

```bash
MONO=~/Documents/work/projects/monjizeen
mkdir -p ~/.cursor/skills ~/.claude/skills
for skill in "$MONO"/shared-assets/skills/*/ "$MONO"/shared-assets/roles/*/; do
  name=$(basename "$skill")
  [[ -f "$skill/SKILL.md" ]] || continue
  ln -sfn "$skill" ~/.cursor/skills/"$name"
  ln -sfn "$skill" ~/.claude/skills/"$name"
done
```

## Usage

Invoke with `/` in Cursor or Claude Code:

```
/start-work
/finish-work
/cleanup
/refresh
/new-project
/init-project
/pre-mvp-audit
/cto      # role, in ../roles/
/ceo      # role, in ../roles/
```

Or trigger naturally: "start work on …", "finish work", "should we build this" → CEO review.

## File structure

```
skills/
├── start-work/SKILL.md
├── finish-work/SKILL.md
├── cleanup/SKILL.md
├── refresh/SKILL.md
├── new-project/SKILL.md
├── init-project/
│   ├── SKILL.md      # alias → new-project
│   └── reference.md
├── pre-mvp-audit/
│   ├── SKILL.md
│   └── CHECKLIST.md
└── README.md
```

## init-project scripts

See `../scripts/init-project/` — Gate 0 of `/new-project` runs `bootstrap-mac.sh`; it also links the skills.

## Updating

Edit `SKILL.md` in this repo. Commit + push. Symlinks pick up changes after `git pull`.

## Troubleshooting

**Skill not appearing:**
- Verify symlink: `ls -l ~/.cursor/skills/{name}` and `ls -l ~/.claude/skills/{name}`
- Both should point to `shared-assets/skills/{name}` (or `shared-assets/roles/{name}` for a role)
- Re-run `scripts/init-project/bootstrap-mac.sh`
- Restart Cursor or Claude Code

**Stale copy instead of symlink:**
- Remove the copy: `rm -rf ~/.claude/skills/{name}`
- Re-run `scripts/init-project/bootstrap-mac.sh`
