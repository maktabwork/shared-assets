---
name: implementation-review
description: >
  Check what was built against what was asked: a ticket, a list of
  requirements, a client's comments or an earlier audit. Every request gets a
  status (done, partly done, wrong, missing, can't check) with a screenshot
  of the build, and anything built that nobody asked for is listed apart.
  Use for "review the implementation", "did they build what we asked",
  "check the ticket was done", "verify the fixes", "مراجعة التنفيذ", "هل نُفذت
  الملاحظات", "مراجعة تحسينات المطورين".
---

# Implementation review

Answers one question for the person who asked: **was what we asked for built,
and built right?** The request is the yardstick, not general UX taste. This is
not a UX audit (that one looks for anything in the user's way, see
`ux-audit`) and not a design comparison (build vs approved frames, see
`design-qa`). New usability problems you notice go in a short list at the end,
apart from the rows.

Read [../ux-common/UX-STANDARDS.md](../ux-common/UX-STANDARDS.md) first.
Screenshots: [../page-screenshots/SKILL.md](../page-screenshots/SKILL.md).
The page: [../html-deliverable/SKILL.md](../html-deliverable/SKILL.md).

## Inputs (list any you cannot open, all at once)

- **The request**: the ticket with its description, checklist, acceptance
  criteria and comments; or the list of comments, the earlier audit report or
  the meeting notes the team worked from. Keep its numbers and links.
- **The build**: staging or live URL, app build, or screen recordings, with a
  test account for each role. Which version or date you reviewed.
- **Agreed changes since the request**: later comments or decisions that
  replaced part of it. A row follows the latest agreed version.

## How to do it

1. **Turn the request into rows first.** One row per thing that can be
   checked on its own: each acceptance criterion, each checklist item, each
   earlier comment or finding (with its number), each "should" sentence in
   the description. Split a sentence that asks for two things. Write each row
   as the request says it, shortened, with a link to where it says it.
   If the request is too vague to check ("make it nicer"), say what you will
   take it to mean and mark it as an assumption.
2. **Check each row in the build** as the user it was written for, at 390
   and 1440 px and in each language in scope, with realistic data, and in the
   states the row implies (empty, error, long text, the role that should not
   see it). On a live production site never submit forms; on staging with a
   test account you may.
3. **Take the evidence for every row**, done rows included, with
   `page-screenshots/crop.js` (crop at 2×, spot boxed in red, `--context=`
   for the wider shot, `--state=` for hover, menus and keyboard focus). Name
   files by row number.
4. **Give each row one status**:
   - **Done**: does what was asked, in every width and language in scope.
   - **Partly done**: some of it works; say exactly which part is missing
     ("works in English, the Arabic page still shows the old label").
   - **Wrong**: built, but not as asked; quote the request and say what the
     build does instead.
   - **Missing**: no sign of it in the build.
   - **Can't check**: no access, the state cannot be reached, or the request
     is too vague; say what is needed to check it.
5. **List what was built but not asked for** ("Not asked for"): changes you
   see that no row covers. Only those a reviewer should know about: they
   changed behaviour, text or layout someone agreed on, or they broke
   something.
6. **Rank** Missing, Wrong and Partly rows by how much they block the
   request's purpose (1–4, UX-STANDARDS §3); Done and Can't check rows keep
   the request's order.
7. **Write each fix for a developer**: the element, what the request asked
   for (quoted), what is there now, and the expected value or text.

## Output

**One HTML page** from
[`../html-deliverable/findings-template.html`](../html-deliverable/findings-template.html)
with its implementation review set of statuses, plus an `img/` folder. In the
client's working language, written once.

| Page part | Content |
|---|---|
| Header and status line | What was reviewed (build URL and version, date), against which request (ticket key, link), widths, languages, roles |
| Takeaway and tiles | One sentence (for example "9 of 12 done; the export and the Arabic labels are missing"); tiles for Done, Partly, Wrong, Missing |
| Rows, grouped by the request's own sections | **Issue**: the request (quoted short, with its number) → what the build does → the fix as an action. **Evidence**: the crop and link. **Suggested**: a hint when needed |
| Closing panels | Not asked for; new problems noticed (not in the request); can't check and what is needed; assumptions and questions |

Count the rows by status after writing them; the tiles and chips do this from
the rows. When the team works in tickets, offer (don't post) one comment per
Missing, Wrong or Partly row on the ticket; the page stays the summary.

A later round updates the same page: keep the row numbers and date each
change ("Missing → Done, 2026-11-20").

## Quality checks

The shared checks in UX-STANDARDS plus:

- CHECK [impl-every-request]: Every acceptance criterion, checklist item and
  earlier comment has a row with a status; none is skipped silently.
- CHECK [impl-quoted]: Every Wrong and Partly row quotes what was asked and
  says what the build does instead.
- CHECK [impl-evidence]: Every row has a cropped screenshot with the spot
  boxed (or the reason it can't, under Can't check).
- CHECK [impl-statuses]: Only the five statuses plus "Not asked for" are
  used, and the counts match the rows.
- CHECK [impl-separate]: New usability problems sit in their own panel, not
  mixed with the request's rows.
- CHECK [impl-latest]: Rows follow the latest agreed version of the request;
  changes agreed later are cited.
