---
name: page-screenshots
description: >
  Take screenshots of a web page that any reviewer or model can read: the
  first screen and the whole page in sections, at desktop (1440 px) and phone
  (390 px) width, after scrolling so lazy images and animated counters load.
  Also takes the evidence crop for one finding: the element boxed in red at
  2×, with a wider context shot. Use whenever any skill needs page
  screenshots (ux-audit, implementation-review, design-qa, ui-screen-design,
  qa-reviewer), or for "screenshot the page", "full-page screenshot",
  "screenshot this issue", "لقطة شاشة للصفحة".
---

# Page screenshots

One way to capture pages, so every skill gets the same, readable pictures.
The other skills say *what* to look at; this one says *how* to capture it.

## Why sections, never one tall image

- AI models refuse an image taller or wider than **8,000 px**, and the whole
  step fails. A long homepage at 1440 px is often 10,000–20,000 px tall.
- Models also shrink any image to about **1,568 px** on its long side, so a
  tall page in one image turns into unreadable text anyway.
- So: one picture of the **first screen**, then the page in **sections about
  1,600 px tall**, top to bottom. Each section is sharp enough to read.

## How to do it

1. **Use the script** when you have a shell:
   `node page-screenshots/capture.js <url> [outDir] [--widths=1440,390] [--lang=ar] [--max=12]`
   It needs Playwright (`npm i -D playwright` or a global install). It prints
   a list of the files it wrote. An agent whose browser tool can capture a
   full page in parts (for example `open_page` with `full_page: true`, then
   `part: 2, 3…`) follows the same rules.
2. **Both widths, every time**: 1440 px (desktop) and 390 px (phone), in each
   language the page ships. A phone screenshot is not a narrow desktop one:
   the script turns on touch and the phone viewport.
3. **Scroll before you capture.** The script scrolls to the bottom in steps,
   waits, and returns to the top, so lazy images load and number counters
   finish. If a counter still reads 0 or a section is blank, say "may not have
   loaded in the capture" instead of reporting it as a fact. Check it again
   by opening that part of the page on its own, or mark it as varying.
4. **Name files by width and order**: `1440-00-first-screen.jpg`,
   `1440-01.jpg`, `1440-02.jpg`… `390-00-first-screen.jpg`… Keep them in one
   folder per page.
5. **Sticky headers and pop-ups.** A sticky header shows in every section;
   ignore the repeats. Close a cookie banner or chat pop-up only when it
   hides the content, and say you closed it. Never submit a form, log in or
   pay to get past something.
6. **Very long pages.** The script stops after 12 sections per width (about
   19,000 px) and says how much is left. Capture the rest only if the task
   needs it (pass `--max`), and say which part you did not see.
7. **To show one problem**, use the crop script instead of sending a whole
   section:
   `node page-screenshots/crop.js <url> "<css selector>" img/3.png --context=img/3-context.jpg [--width=390] [--lang=ar] [--scheme=dark] [--state=hover|focus|open]`
   It turns animations off, captures at 2×, boxes the element in red with
   some room around it, and saves the wider shot of the same screen that the
   crop opens to in a report. `--state=focus` reaches the element with Tab so
   the real focus ring shows (if Tab never reaches it, that is a finding);
   `--state=open` clicks it to open a menu, never a submit, save, send or pay
   button. Name crops by finding number; they go next to the finding they
   prove.

## Rules

- Never send a model or a client an image over 8,000 px on any side.
- JPEG at quality 70–80 for pages; PNG only for crops where exact colours
  matter. Colours and contrast are **measured** with `ux-common/measure.js`,
  never read from screenshot pixels.
- Only public pages, or pages the client gave access to. Never screenshot
  personal data you do not need, and blur it if it shows.

## CHECKs

- CHECK [shots-size]: No image is taller or wider than 8,000 px; long pages
  are in sections of about 1,600 px.
- CHECK [shots-widths]: Both 1440 px and 390 px were captured (or the reason
  one was skipped is stated).
- CHECK [shots-loaded]: The page was scrolled before capture, and anything
  blank or zero is reported as "may not have loaded", not as a fact.
- CHECK [shots-crop]: Every finding's picture is a tight crop with the spot
  boxed, at 2×, with its wider context shot.
- CHECK [shots-coverage]: The report says which part of the page was not
  captured, if any.
