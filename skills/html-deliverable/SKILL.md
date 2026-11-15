---
name: html-deliverable
description: >
  Turn any finished client deliverable (audit, review, spec, plan, research,
  proposal) into one visual HTML page with its screenshots, instead of a
  Markdown file. Every service skill hands over this way. Use for "make the
  report", "client page", "deliver it", "send the findings", "صفحة التقرير".
---

# HTML deliverable

**Rule for every deliverable skill: the client gets a visual HTML page, never a
Markdown file.** A reader should understand it by looking, not by reading.
Markdown is only for our own notes (working drafts, `qa-self-check.md`, docs in
git) and for text pasted into a tool that wants plain text (a ticket, an
email). The skill that does the work decides the content; this skill decides
how it is handed over.

## Pick the starting point

| Deliverable | Start from |
|---|---|
| A list of findings with evidence: UX audit, implementation review, design QA, accessibility or SEO check | [`findings-template.html`](findings-template.html) |
| Anything else: spec, flow, plan, research, IA, proposal | A blank page that follows the layout and visual rules below |

The findings template has the columns **# · Issue · Evidence · Suggested**,
filter chips for each category (severity or status), stat tiles, the top
issues, and closing panels (quick wins, strengths, not covered, next steps,
assumptions and questions). Fill `LANGS`, `PAGE`, `KINDS` and `ROWS` at the
top; the rest draws itself. It has a severity set (UX audit, design QA) and a
status set (implementation review); keep the one you need.

## Layout

1. Header: small "Monjizeen" wordmark, title, product or link, date, author.
2. Status line: `Ready for review` or `Draft: waiting on <inputs>`, inputs
   used, what was not opened.
3. The one-sentence takeaway and 2–4 stat tiles (counts that come from the
   rows, never typed by hand).
4. The body, in the source deliverable's order, each section opening with its
   visual.
5. Closing panels: what was not covered and why, next steps, assumptions and
   open questions.

## Visual first

Replace prose with the form that fits it. A paragraph is the last resort and
never longer than 3 lines.

| Content | Show it as |
|---|---|
| Findings or recommendations | Rows (findings template) or cards, each with its screenshot |
| Counts by severity or status | Filter chips plus stat tiles, or a small inline SVG bar |
| Impact vs effort | A 2×2 grid with the items placed in it |
| A user flow | A step diagram with arrows; error branches in a warning colour |
| A screen proposal | A screenshot or mock of it, numbered pins with a legend |
| Information architecture | A tree |
| Comparisons | A compact table, only when it is really tabular |

## Screenshots are part of the deliverable

- Every finding a reader could doubt has a picture. Capture with the
  [`page-screenshots`](../page-screenshots/SKILL.md) skill: `crop.js` for the
  tight crop with the spot boxed in red at 2×, animations off, plus the wider
  context shot the crop opens to on click.
- Capture interactive states for real: hover, open menus, keyboard Tab for
  focus rings. A finding with nothing to see (a missing label) gets a small
  image of the code or accessibility readout.
- Name images by row number (`img/3.png`, `img/3-context.jpg`,
  `img/3-sug.png`) and ship them as files in an `img/` folder next to the
  page. Embed them as `data:` images only when the page must travel as a
  single file (an email attachment); then keep each under about 200 KB.

## Style (learned from owner feedback)

- Text fills its container; never cap paragraphs with a max-width that breaks
  lines mid-screen.
- Severity or status is a thin coloured stripe on the row's start edge plus
  the word; no row background tints. Colour is never the only signal.
- Chips: light tint of their colour, coloured text, border in their own
  colour; the selected chip is filled. Hide a chip whose count is 0.
- Sticky table header; group titles are light rows that never outshine it.
- No horizontal page scroll from 390 to 1920 px; below about 900 px rows stack
  into cards.
- Every fix is written as an action ("Move…", "Raise…", "Remove…"), never as a
  description of the end state.
- No footnote explaining colours or links; self-describing labels are enough.
- Colours as CSS variables with a dark theme; WCAG AA contrast; visible focus
  only on `:focus-visible`.

## Language

Write the page in the client's working language and direction. One language is
the norm. Add a second language (the template shows an AR / EN switch by
itself) only when the brief says the readers need both. Arabic inside an
English page (and the reverse) sits in its own element with `dir` and `lang`.

## Clean and private

The page never shows our internals: no internal tool or agent names, skill
names, CHECK keys or our ticket numbers. Use the client's own ticket keys.

## Hand over

1. Open the page at 1440 and 390 px (light and dark) with Playwright, look at
   the screenshots, and fix what breaks.
2. Check that every `src` and `href` resolves (no broken image, no dead
   link).
3. Publish it (an Artifact, or the client's place for files) or zip the page
   with its `img/` folder. Give the owner the link, the counts and the top
   issues; offer, don't send, anything that goes to the client's team.
4. A follow-up round updates the same page: keep the numbers and date each
   change in the row ("Major → Fixed, 2026-11-03").

## CHECKs

- CHECK [html-not-md]: The client gets an HTML page, not a Markdown file.
- CHECK [html-evidence]: Every finding of severity 2 or more (or every
  Wrong, Missing or Partly row) has a cropped screenshot with the spot boxed.
- CHECK [html-links]: Every image and link on the page resolves.
- CHECK [html-render]: The page was rendered and looked at, at 390 and 1440 px,
  with no horizontal scroll.
- CHECK [html-counts]: Tiles and chips are counted from the rows.
- CHECK [html-clean]: No internal names, CHECK keys or our ticket numbers.
