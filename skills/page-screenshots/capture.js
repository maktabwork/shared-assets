// Screenshots a page the way models and people can read it: the first
// screen, then the whole page in sections about 1,600 px tall (never one
// image over 8,000 px), at desktop and phone width, after scrolling so lazy
// images and counters load.
// Usage: node page-screenshots/capture.js <url> [outDir] [--widths=1440,390] [--lang=ar] [--max=12]
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const SECTION = 1600;

async function scrollThrough(page) {
  await page.evaluate(async () => {
    const step = Math.max(400, Math.floor(window.innerHeight * 0.8));
    for (let y = 0; y < document.documentElement.scrollHeight; y += step) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 250));
    }
    window.scrollTo(0, document.documentElement.scrollHeight);
    await new Promise((r) => setTimeout(r, 800));
    window.scrollTo(0, 0);
  });
  await page.waitForLoadState('networkidle', { timeout: 5000 }).catch(() => {});
  await page.waitForTimeout(500);
}

(async () => {
  const args = process.argv.slice(2);
  const opt = (name, def) => (args.find((a) => a.startsWith(`--${name}=`)) || `=${def}`).split('=').slice(1).join('=');
  const [url, outDir = 'screenshots'] = args.filter((a) => !a.startsWith('--'));
  if (!url) { console.error('Usage: node capture.js <url> [outDir] [--widths=1440,390] [--lang=ar] [--max=12]'); process.exit(1); }
  const widths = opt('widths', '1440,390').split(',').map(Number);
  const lang = opt('lang', 'en');
  const max = Number(opt('max', '12'));
  fs.mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch();
  const written = [];
  for (const width of widths) {
    const phone = width <= 500;
    const context = await browser.newContext({
      viewport: { width, height: phone ? 844 : 900 }, isMobile: phone, hasTouch: phone,
      deviceScaleFactor: 1, locale: lang === 'ar' ? 'ar-SA' : 'en-US',
    });
    const page = await context.newPage();
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForLoadState('networkidle', { timeout: 10000 }).catch(() => {});
    await scrollThrough(page);

    const first = path.join(outDir, `${width}-00-first-screen.jpg`);
    await page.screenshot({ path: first, type: 'jpeg', quality: 75 });
    written.push(first);

    const height = await page.evaluate(() => document.documentElement.scrollHeight);
    const sections = Math.ceil(height / SECTION);
    for (let i = 0; i < Math.min(sections, max); i++) {
      const y = i * SECTION;
      const file = path.join(outDir, `${width}-${String(i + 1).padStart(2, '0')}.jpg`);
      await page.screenshot({ path: file, type: 'jpeg', quality: 75, fullPage: true,
        clip: { x: 0, y, width, height: Math.min(SECTION, height - y) } });
      written.push(file);
    }
    const note = sections > max ? ` (stopped after ${max} of ${sections} sections; ${height - max * SECTION}px not captured)` : '';
    console.log(`${width}px: page is ${height}px tall, ${Math.min(sections, max)} sections${note}`);
    await context.close();
  }
  await browser.close();
  console.log(written.join('\n'));
})().catch((e) => { console.error(e.message); process.exit(1); });
