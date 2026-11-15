// Takes the evidence picture for one finding: a tight crop around one element
// with the spot boxed in red, at 2x, animations off, plus a wider "context"
// shot of the same screen (the box stays on it) for the click-to-open view.
// Usage:
//   node page-screenshots/crop.js <url> <selector> <out.png>
//     [--width=1440] [--lang=en] [--pad=24] [--scheme=light|dark]
//     [--state=hover|focus|open] [--context=<out-context.jpg>] [--nobox]
// --state=focus reaches the element with the keyboard (Tab), so the real
// focus ring shows. --state=open clicks it (menus, dropdowns): never use it on
// a submit, save, send or pay button.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const args = process.argv.slice(2);
  const opt = (name, def) => (args.find((a) => a.startsWith(`--${name}=`)) || `=${def}`).split('=').slice(1).join('=');
  const flag = (name) => args.includes(`--${name}`);
  const [url, selector, out] = args.filter((a) => !a.startsWith('--'));
  if (!url || !selector || !out) {
    console.error('Usage: node crop.js <url> <selector> <out.png> [--width=1440] [--lang=en] [--pad=24] [--scheme=light] [--state=hover|focus|open] [--context=file.jpg] [--nobox]');
    process.exit(1);
  }
  const width = Number(opt('width', '1440'));
  const phone = width <= 500;
  const pad = Number(opt('pad', '24'));
  const state = opt('state', '');
  const context = opt('context', '');
  const lang = opt('lang', 'en');

  const browser = await chromium.launch();
  const page = await (await browser.newContext({
    viewport: { width, height: phone ? 844 : 900 },
    deviceScaleFactor: 2,
    isMobile: phone,
    hasTouch: phone,
    locale: lang,
    colorScheme: opt('scheme', 'light'),
    reducedMotion: 'reduce',
  })).newPage();

  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForLoadState('networkidle', { timeout: 8000 }).catch(() => {});
  await page.addStyleTag({ content: '*,*::before,*::after{animation-duration:0s!important;animation-delay:0s!important;transition:none!important;caret-color:transparent!important}' });

  const el = page.locator(selector).first();
  await el.waitFor({ state: 'visible', timeout: 15000 });
  await el.scrollIntoViewIfNeeded();

  if (state === 'hover') await el.hover();
  if (state === 'open') await el.click();
  if (state === 'focus') {
    // Tab from the start of the page until the element (or something inside it) has focus.
    await page.evaluate(() => { document.activeElement && document.activeElement.blur(); window.focus(); });
    let reached = false;
    for (let i = 0; i < 200 && !reached; i++) {
      await page.keyboard.press('Tab');
      reached = await el.evaluate((n) => n === document.activeElement || n.contains(document.activeElement));
    }
    if (!reached) console.error('Could not reach the element with Tab: that is a finding (keyboard access).');
  }
  await page.waitForTimeout(300);

  const box = await el.boundingBox();
  if (!box) { console.error('Element has no box (hidden?)'); await browser.close(); process.exit(1); }

  // Draw the red box and an invisible frame (box + padding) to capture.
  await page.evaluate(({ b, pad, nobox }) => {
    const sx = window.scrollX, sy = window.scrollY;
    const docW = document.documentElement.scrollWidth;
    const mk = (id, css) => { const d = document.createElement('div'); d.id = id; d.style.cssText = css; document.body.appendChild(d); return d; };
    if (!nobox) mk('__mark', `position:absolute;left:${b.x + sx - 4}px;top:${b.y + sy - 4}px;width:${b.width + 8}px;height:${b.height + 8}px;border:3px solid #e01e1e;border-radius:6px;pointer-events:none;z-index:2147483647;box-sizing:border-box`);
    const left = Math.max(0, b.x + sx - pad), top = Math.max(0, b.y + sy - pad);
    const right = Math.min(docW, b.x + sx + b.width + pad);
    mk('__frame', `position:absolute;left:${left}px;top:${top}px;width:${right - left}px;height:${b.height + pad * 2}px;pointer-events:none;z-index:2147483646`);
  }, { b: box, pad, nobox: flag('nobox') });

  fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
  await page.locator('#__frame').screenshot({ path: out, animations: 'disabled' });
  console.log(out);

  if (context) {
    // Centre the element in the viewport for the wider shot.
    await page.evaluate((b) => window.scrollBy(0, b.y - window.innerHeight / 2 + b.height / 2), box);
    await page.waitForTimeout(200);
    await page.screenshot({ path: context, type: context.endsWith('.png') ? 'png' : 'jpeg', ...(context.endsWith('.png') ? {} : { quality: 75 }), animations: 'disabled' });
    console.log(context);
  }
  await browser.close();
})().catch((e) => { console.error(e.message); process.exit(1); });
