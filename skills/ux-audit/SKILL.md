---
name: ux-audit
description: >
  Review the usability of a live product, staging build, prototype or Figma
  file and hand back a ranked list of problems with concrete fixes. Use for
  "UX audit", "usability review", "review the dashboard", "test the user
  experience", "مراجعة تجربة المستخدم", "اختبار تجربة الاستخدام", "review the
  website", or a design review of a page someone else built. To check a
  build against what was asked (a ticket, a list of requirements), use
  `implementation-review`; against approved design frames, `design-qa`.
---

# UX audit

Our method for finding what makes a product hard to use and saying exactly
what to change. The output is a ranked findings list, not a redesign,
handed over as one visual HTML page where every finding shows its screenshot.
An audit is about the user's goals, not about matching a spec.

Read [../ux-common/UX-STANDARDS.md](../ux-common/UX-STANDARDS.md) first.
Screenshots: [../page-screenshots/SKILL.md](../page-screenshots/SKILL.md).
The page: [../html-deliverable/SKILL.md](../html-deliverable/SKILL.md).
Common problems to sweep for: [CHECKLIST.md](CHECKLIST.md).

## Before you start

1. Get the brief and the client context (UX-STANDARDS §1).
2. **Pin the scope in one line**: product, the user role you act as, the
   journeys, platforms and languages. A dashboard audit "from the content
   editor's view, entry to publish" is a scope; "review the system" is not.
   If the brief limits the kind of change (for example "only fonts, labels,
   fields and spacing, no feature changes"), that limit is a rule: every
   recommendation must fit inside it.
3. **Collect, in one message, whatever is missing**: access (as environment
   keys, never in chat), the users and their 3–7 key tasks, roles, widths,
   languages, themes, the design system or glossary (its names are the
   right ones; a deviation is a finding), and **known decisions** already
   agreed (for example "template colours are set by each customer"): never
   re-flag those. Ask whether the client wants the report page, comments on
   their prototype or design file, or both.
4. **Pick 2–4 key journeys** from the brief (the tasks users come for). If
   the brief names none, take the product's main job and say so. List each
   journey's steps once in Scope (J1.1, J1.2…) so findings can cite them.

## How to do it

1. **Walk each journey as the user**, step by step, at phone width (390 px)
   and desktop (1440 px), in each language the product ships. Use realistic
   data: long names, Arabic and English, an empty account, a wrong input.
   Take the evidence picture of every problem as you find it, with
   `page-screenshots/crop.js`: a tight crop at 2×, animations off, the spot
   boxed in red, plus a wider context shot (`--context=`). Capture states for
   real: `--state=hover`, `--state=open` for menus, `--state=focus` to reach
   an element with Tab. Note the exact page link and state for each.
2. **Break it on purpose**: try empty and wrong inputs (client-side
   validation only), go back mid-flow, reload, open a deep link logged
   out, try keyboard only, zoom to 200 %. **On a live production site never
   press a submit button at all** (an empty or invalid submit still counts):
   check validation only by what the page shows while typing or on blur.
   Never send a form that creates data or contacts people (questions, sign-ups,
   emails, payments); on staging with a test account you may. When a
   journey is blocked (a quota, a login wall, a step that would send
   data), go as far as is safe, record where and why it stopped, and list
   the rest as not reviewed.
   Write down the date, time and time zone of the walk; quotas, content and
   banners change. If any submit was pressed or tried, even by mistake or
   refused by the environment, say so in the Status line.
3. **Sweep the lenses** after the walk (UX-STANDARDS §3): heuristics,
   WCAG essentials, Arabic/RTL (§5), states (§4), then go screen by screen
   through [CHECKLIST.md](CHECKLIST.md) for what the journeys missed. An
   inconsistency between two screens of the same product is a finding. Measure contrast and the
   tap target sizes of the main actions at 390 px with `ux-common/measure.js`
   (a colour picked from a screenshot pixel is not a measurement). States
   you could not reach are listed as not reviewed.
4. **Write one finding per problem**: where (exact screen, element, state,
   width, language), what happens, why it matters (the user's goal, a
   heuristic or a WCAG criterion), the fix, severity 1–4, effort S/M/L, and
   confidence (*seen*: reproduced; *signal*: likely, needs data to prove).
   When one finding mixes a seen part and a signal part, give each part
   its own confidence ("seen at 390 px; signal on Google search").
   Merge duplicates; split a finding that hides two problems. One cause in
   several places (the same colour failing on buttons and titles) is one
   finding with every place listed, unless the places need different
   fixes.
5. **Make every fix concrete and small**: name the element, the change and
   the new value or text. Take values from the client's design system, or,
   with none, from the product itself (a colour it already uses that
   passes), and say where it came from ("Move 'نشر' to the top bar of the editor, primary
   style", "Raise the label to 14 px and contrast to 4.5:1"). When the brief
   allows code-level advice, give the CSS or HTML change.
6. **Rank**: severity first, then how many users and how often, then effort.
   Number the findings after ranking, then name the screenshots by those
   numbers (`img/3.png`, `img/3-context.jpg`). On a re-audit keep the old
   numbers and add new ones at the end. Severity is about effect, not about workarounds alone: 3 when
   the problem is frequent or hard to notice and costs the user the task or
   real effort, 2 when it is easy to get round. Pick up
   to five quick wins (high impact, S effort).
6b. **Check each finding against its own evidence**: re-read the Issue
   sentence next to its screenshot or measured value. If the screenshot
   shows something else, fix the finding. Values that change between loads
   or days (result counts, ranking, dates, Hijri dates, quotas) are quoted
   exactly as the screenshot shows them, with "(varies; seen <date>)". A *signal* finding's fix is the
   validation step that would prove it (or it moves to Next steps).
   Each fix must work at every width named in Where.
7. **Keep what works**: two to four strengths the fix list must not break.
8. **Say what would raise confidence**: a 5-user test of journey X, an
   analytics check on step Y. Never present your walk as user research.

## Output

**The client gets one HTML page**, made from
[`../html-deliverable/findings-template.html`](../html-deliverable/findings-template.html)
with its severity set, and an `img/` folder with every screenshot. No
Markdown report goes to the client.

Write the page in the client's working language: the language the client
writes the brief or tickets in. Only when the brief says the page is for the
product's own users or team in another language, use that one. Write each
finding once, in that language; add the second language (the page then shows
an AR / EN switch) only when the brief says the readers need both. Image alt
texts follow the page's language.

Severity words in Arabic: 4 حرج، 3 كبير، 2 صغير، 1 شكلي; in English: Critical,
Major, Minor, Cosmetic. Cite lenses by their own names (Nielsen #4, WCAG
1.4.3), never our standards file.

What goes where on the page:

| Page part | Content |
|---|---|
| Header and status line | Product, URL, date, scope in one line; `Status / Inputs used / Not opened / Walked on: <date, time, zone>` |
| Takeaway and tiles | 2–4 sentences cut to one: state, top problem, the change with the most impact; counts by severity |
| Top issues | The five most severe, one line each (drawn from the rows) |
| Rows, grouped by journey or screen | **Issue**: where (screen, element, state, width, language) → what the user experiences → why it matters (muted) → the fix as an action → effort tag (S/M/L), and "Likely, not yet proven" for a *signal* finding → "Also seen in" |
| | **Evidence**: the crop (click opens the context shot), its width and language, and a link to the exact page and state; steps for interactions |
| | **Suggested**: a mock or reference picture, or a one-line CSS or behaviour hint, when the fix text is not enough; "—" otherwise |
| Closing panels | Quick wins (up to 5, by number), strengths to keep, not covered and why, next steps (what would raise confidence), assumptions and open questions |

**Comments on a prototype or design file**, only when the client asked: one
comment per finding, on the exact element, short and in the product's language
("Show errors only on save", "Make the row clickable"). The page stays the
summary.

Our QA notes (`qa-self-check.md`) stay internal and may be Markdown.

**Writing**: plain and specific; say what is shown; no references to other
tickets or things the reader has not seen. Not everything that can be said
should be said.

## Standards for MENA work

- Audit the Arabic version as a first-class product, not a translation:
  mirroring, mixed text, digits, line height and truncation (UX-STANDARDS §5).
- Religious and charity products: check that honorifics and verses render
  intact, and that donation amounts, fees and receipts are always visible
  before confirming.
- Note where an English-first pattern does not fit (a left-swipe to delete
  that is a right-swipe in RTL, an English-only search that misses Arabic
  spelling variants such as ة/ه and أ/ا).

## Quality checks

The shared checks in UX-STANDARDS plus:

- CHECK [audit-journeys]: The key journeys are named and each was walked end
  to end; findings say which journey and step they come from.
- CHECK [audit-severity]: Every finding has severity 1–4, effort S/M/L and
  confidence, and the table is sorted by severity.
- CHECK [audit-self-consistent]: Every Issue matches its own screenshot or
  measured value.
- CHECK [audit-page]: The client gets the HTML page (not Markdown), with its
  `img/` folder (or images embedded when it must be one file), every image
  and link resolves, and it opens with the status line. Every Arabic phrase
  in an English page (and English in an Arabic page) sits in one element
  per whole quoted string (numbers and punctuation inside, quote marks
  outside) with its own `dir` and `lang`, alt texts carry their own `lang`, and mapping
  rules across scripts (ة → ه) are a small table, not inline arrows. Render
  it at 390 px at 2× and read every mixed line before handing over; counting
  spans is not a check.
- CHECK [audit-fix]: Every finding has a concrete fix that names the element
  and the change; no "improve the UX".
- CHECK [audit-limits]: Every fix fits the limits in the brief (no feature or
  structure changes when the brief rules them out).
- CHECK [audit-screens]: Each finding of severity 2 or more has a cropped
  screenshot with the spot boxed in red (or a Figma node picture), and a link
  to the exact page or node.
- CHECK [audit-decisions]: Nothing listed as a known decision is flagged.
- CHECK [audit-quick-wins]: Quick wins and strengths to keep are listed.
- CHECK [audit-no-submit]: No submit reached production. A press that
  reached the site fails; a press the environment blocked before anything
  was sent passes only when it is stated in the Status line.
- CHECK [audit-varies]: Every changing value (counts, ranking, dates) matches
  its screenshot and is marked "varies; seen <date>"; a crop that also shows
  an older uncited value says its capture date in the caption.
- CHECK [audit-religious]: For religious products, the delivery says whether
  honorifics and verses render intact, with a screenshot (N/A otherwise).
