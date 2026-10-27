// Render each built poster to an A4 PDF and a 300 dpi grayscale-ready PNG.
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [outDir, ...names] = process.argv.slice(2);
  const browser = await chromium.launch();
  // 210mm at 96 css px/in = 793.7px; scale 3.125 gives ~2480px wide (300 dpi A4).
  const page = await browser.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 3.125 });
  for (const name of names) {
    await page.goto('file://' + path.join(outDir, name + '.html'));
    await page.evaluate(() => document.fonts.ready);
    await page.emulateMedia({ media: 'print' });
    await page.pdf({ path: path.join(outDir, name + '.pdf'), format: 'A4', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
    await page.locator('.poster').screenshot({ path: path.join(outDir, name + '.png') });
    console.log('rendered', name);
  }
  await browser.close();
})();
