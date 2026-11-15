---
name: understand-requirements
description: >
  Read a ticket (or the page its link points to) with its organization and
  project context, and say back in a few short bullets what will be built,
  split into requirements to deliver one at a time, with the skill for each.
  The first step of every Maher ticket, before any work starts. Use for
  "what did you understand", "break this ticket down", "plan this ticket".
---

# Understand requirements

The first thing Maher does on a ticket. Nothing is built until the person
who asked agrees with what was understood, so a wrong reading costs one
short message instead of a wrong deliverable.

## Inputs

- The ticket: title, description, checklist, links, comments, and its
  organization and project context.
- A link instead of a written ticket: open it and read it as the ticket.
- On a second try: your earlier understanding and the note on why it was
  disliked. Fix exactly what the note says; keep the rest.

## How to do it

1. **Read everything first,** including linked pages that are public. Note
   what the organization and project context say about audience, brand and
   rules; they apply to every requirement.
2. **Run the readiness checks** in monjizeen-core
   `checks/ticket-readiness.md` (Maher reads a copy next to this file,
   `ticket-readiness.md`) in your head (org, project, consistency,
   clarity, acceptance, inputs). Do not print the checklist; turn what it finds
   into assumptions and questions below.
3. **Split the work into requirements,** in the order they should be
   delivered. Each one:
   - is one deliverable a person can review on its own in a few minutes
     (a findings list, one screen, one spec section, one set of texts);
   - has a short title and one or two lines on what "done" means for it;
   - builds on the ones before it, so feedback on the first one improves
     the rest.
   Two to six requirements is normal. One is fine for a small ticket. Never
   more than ten: group them instead.
4. **Pick the skill for each** from the methods you are given, and name
   only the ones you will use.

## What to send back

Short. The person reads it in under a minute.

- **What I understood:** 3 to 6 bullets in plain words. Who it is for, what
  will be delivered, and what is out of scope.
- **Requirements:** numbered, title plus one line each, in delivery order.
- **Assumptions:** only the ones that would change the result if wrong.
- **Questions:** at most three, only where a guess would be risky. Each with
  the answer you will assume if nobody replies.

Write in the ticket's language. No method names, file names or internal
tool names; say what you will do, not which skill does it.

## Quality checks

- CHECK [understand-short]: The understanding is 3 to 6 bullets and fits on one screen.
- CHECK [understand-split]: Every requirement is one reviewable deliverable with what "done" means.
- CHECK [understand-order]: Requirements are in delivery order and later ones can build on earlier ones.
- CHECK [understand-grounded]: Every bullet comes from the ticket, its links or its context; guesses are listed as assumptions.
- CHECK [understand-redo]: On a second try, the note's point is fixed and everything it did not mention is unchanged.
