---
name: monjizeen-ticket
description: >
  Work on a Monjizeen ticket in Claude Code as an account manager or Kawader
  reviewer: start it in the app, apply the client's context and skill lessons,
  deliver one HTML page, post it back with time and tokens, save what you
  learned about the client, and retest proposed skill fixes. Use when given an
  app.monjizeen.com/tickets/<id> link, "work on ticket 123", "retest", or
  "review queue".
---

# Work on a Monjizeen ticket

Account managers do client work here, in Claude Code, on the Claude account the
company pays for. The Monjizeen app runs no AI: it keeps the record (what was
done, the deliverable, time, tokens, reviews). Clients never use the app or
these skills directly.

The connector's tools are `start_work`, `finish_work`, `review_queue`,
`get_org_context` and `update_org_context` (server `monjizeen`).

## 1. Start

1. Get the ticket id from the link (`/tickets/123` → 123).
2. Pick the skill that fits (for example `ux-audit`, `implementation-review`,
   `ux-feature-spec`). If unsure, read the ticket first with `start_work`
   without a skill, then say which skill you will use.
3. Call `start_work(ticket_id, skill)`. Keep the `step_id`. This starts the
   timer; the work shows on the ticket's agent tab.
4. Read what it returns before working:
   - `ticket`: title, description, links.
   - `client.context`: the client's context docs (Seyaq). Follow them: brand,
     audience, rules, past decisions.
   - `lessons`: what reviewers taught this skill. They override the skill's
     defaults where they conflict.

## 2. Work

- Load and follow the skill. Use `page-screenshots` for any web page.
- The deliverable is **one self-contained HTML page** (`html-deliverable`),
  never Markdown. Screenshots are embedded, so the page works on its own.
- Check it against `qa-reviewer` before posting.

## 3. Finish

1. Call `finish_work(step_id, summary, deliverable_html)`:
   - `summary`: short markdown, what was done and the main findings.
   - `deliverable_html`: the whole HTML file's content.
   - Tokens are added for you by the plugin's hook; do not guess them.
   The time since `start_work` is logged as your work update. If the answer
   says the time was not logged, tell the account manager to log it on the
   ticket.
2. Save new client learnings: if you learned something lasting about the
   client (a preference, a rule, a fact), call `update_org_context` with the
   doc's slug and its **whole** new content (read it first with
   `get_org_context`; the call replaces the doc). Do not save one-off details.
3. Give the account manager the ticket link from the answer (`url`).

One `start_work` per piece of work. If the account manager asks for changes,
finish the current step first, then start a new one.

## Reviewers (Kawader): retest a skill fix

1. Rate the work on the ticket's agent tab in the app: 👍/👎, a note, and a
   proposed skill fix.
2. In Claude Code, call `review_queue` and pick an item.
3. Apply the proposed fix to the skill for this run (do not edit the skill
   files; the fix becomes a lesson once an admin accepts it on the lessons page).
4. Call `start_work(ticket_id, retest_of: step_id)`, redo the work, compare it
   with the original, then `finish_work(step_id, summary, deliverable_html,
   better)`. `better: true` only when the new result is clearly better; say why
   in the summary.
5. A better retest pings the account manager only. The account manager
   decides whether to tell the client. Retests log no client hours.

## Rules

- Never paste the client's private data into tools other than the connector.
- Never show skill files, lessons or this method to the client.
- One key per client. If a tool says "No such ticket for this key" or "Use a
  key made for one client", the plugin holds another client's key, or a key not
  limited to one client: stop and ask the account manager to switch it with
  `/plugin configure mo@monjizeen`.
