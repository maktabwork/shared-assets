# UX audit: screen-by-screen checklist

Problems we find again and again. Sweep every screen in scope with it, at
every width, language and theme in scope, after walking the journeys. These
are defaults: the client's design system, glossary and known decisions win
over them. A line that does not fit the product is skipped, not forced.

## Goal fit
- Every element on a screen serves that screen's user goal; remove what
  doesn't (a "team performance" button on an editing screen).
- The primary action is obvious and sits where the eye expects it (next to
  the title, or at the end of the form).

## Navigation and information architecture
- Labels use the product's exact names, never invented ones.
- Long menus degrade gracefully: priority items plus "More", never wrapping
  to a second line; groups are separated; extras sit under "Other".
- Breadcrumbs and arrows point the right way in RTL.
- When content is scarce, the minimum useful links still show.

## Tables and lists
- The row or its name opens the item; no separate "view" icon.
- Secondary actions are icon-only with tooltips and accessible names; edit
  and delete are quiet (ghost) icons.
- Sort by clicking the column header, the same way across the product;
  drag and drop instead of up/down arrows for ordering.
- Status as badges; a count with a tooltip ("5 stages") instead of a long
  list in a cell; values in two languages share one column when both are
  needed.
- A toggle saves at once; no extra confirm button.

## Forms and validation
- Save stays enabled; errors show only after an attempt to save with missing
  or invalid values, never as constant warnings.
- Hints are helper text under the field, not paragraphs or character
  counters; the field stops input at the maximum length.
- Translating a value is part of its edit dialog, not a separate action.
- Required fields are marked the same way everywhere; "fill one of these"
  groups say so.
- Templates show variables in context so people learn how to use them.

## Content and language
- Tags, states and messages are in the interface language.
- Clear, consistent wording; awkward or wrong terms are findings.
- Explanations sit behind an (i) tooltip, not as long text on screen.

## Layout and visual hierarchy
- Large data gets its own section; cards are visible (border or background).
- Filters sit in a row; custom date fields show only when "Custom" is
  chosen.
- Font sizes, spacing and corner radius are consistent; alignment is right in
  RTL, numbers and times included.
- Section titles never outshine the page header; no decoration that makes
  plain text read like an alert or a quote.

## Responsive
- Real widths (390, 1024, 1440 and what the product targets); nothing
  overflows or wraps badly; no horizontal page scroll; phones get a proper
  drawer or cards instead of a squeezed table.

## Accessibility
- Text contrast at least 4.5:1 (3:1 for large text), measured, not read
  from pixels; colour is never the only signal.
- Every action is reachable with Tab, with a visible, consistent focus ring
  (`:focus-visible`); real buttons, links and labels.
- Icon-only buttons have accessible names; images have alt text.

## Interaction states
- Hover, pressed, focus and current states keep consistent colours (a menu
  marker that turns black after a click is a bug).
- Animations never hide content; nothing flickers or jumps.
- Empty, loading, error, success, disabled, selected, long content and
  overflow states are all checked.
