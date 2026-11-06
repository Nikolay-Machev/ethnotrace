// Optional real-browser integration suite: npm install --no-save playwright
// npx playwright install chromium && node tests/browser_workflow.cjs
const assert = require('node:assert/strict'),
  fs = require('node:fs'),
  path = require('node:path'),
  http = require('node:http');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '..'),
  web = path.join(root, 'web');
(async () => {
  const server = http.createServer((req, res) => {
    const name = new URL(req.url, 'http://localhost').pathname;
    const file = path.join(web, name === '/' ? 'index.html' : name);
    if (!file.startsWith(web + path.sep) || !fs.existsSync(file)) {
      res.writeHead(404);
      return res.end();
    }
   }
   await page.locator('#claim').selectOption('T007');
   const supplement=page.locator('.supplementary-source').filter({hasText:'T007 · plant part'});
   await supplement.locator('summary').click();
   assert.match(await supplement.innerText(),/inner bark/);
   assert.ok(await supplement.locator('a').count()>0);
   assert.match(await supplement.innerText(),/Locator:/);
   await page.locator('#claim').selectOption('T008');
   assert.match(await page.locator('#gaps').textContent(),/Human confirmation recorded/);
   assert.doesNotMatch(await page.locator('#gaps').textContent(),/awaiting human verification/);
   await page.locator('#atlas-search').fill('no-such-account-xyz');
   assert.match(await page.locator('#atlas-body').innerText(),/No accounts match/);
   await page.locator('#atlas-search').fill('T008');
   await page.locator('[data-account="T008"][data-dimension="part"][data-bucket="different_parts"]').click();
   assert.equal(await page.locator('#results article').count(),1);
   assert.match(await page.locator('#results').innerText(),/E004/);
   assert.match(await page.locator('#results table').first().innerText(), /Part comparison/i);
   assert.match(await page.locator('#results table').first().innerText(), /different parts/i);
   assert.match(await page.locator('#gaps').innerText(),/Record when checked/);
   for(const mode of ['lexical','semantic','hybrid']){
    await page.locator('#ranking').selectOption(mode);
    assert.match(await page.locator('#results').innerText(),/E004/);
    assert.doesNotMatch(await page.locator('#results').innerText(),/E003/);
    const downloadPromise=page.waitForEvent('download');
    await page.locator('#export-report').click();
    const download=await downloadPromise;
    const report=fs.readFileSync(await download.path(),'utf8');
    assert.match(report,new RegExp('Selected ranker: '+mode));
    assert.ok(report.includes('E004')&&report.includes('E003')); // Export intentionally includes all evidence.
    assert.match(report,/Record when checked:/);
    assert.match(report,/1472-6882-12-245/);
   }
   await page.locator('#results article summary').click();
   const link=page.locator('#results article a').first();
   const href=await link.getAttribute('href');
   assert.match(href,/^https?:\/\//);
   // Test the actual click/new-tab wiring; remote availability is audited separately.
   await context.route(href,route=>route.fulfill({status:200,body:'External navigation intercepted for wiring test.'}));
   const popupPromise=page.waitForEvent('popup');
   await link.click();
   const popup=await popupPromise;
   await popup.waitForLoadState();
   assert.equal(popup.url(),href);
   await popup.close();
   await page.locator('#clear-drilldown').click();
   assert.ok(await page.locator('#results article').count()>=2);
   await page.locator('#claim').selectOption('T005');
   assert.match(await page.locator('#results').innerText(),/does not establish that no research exists/);
   await page.goto(base+'/evaluation.html');
   assert.match(await page.locator('#evaluation').innerText(),/Human-reviewed ranking comparison/);
   assert.match(await page.locator('#evaluation').innerText(),/10 of 10 reviews completed with assistant-label exposure/);
   assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'Evaluation overflow at '+width);
   await page.goto(base);
  }
})().catch((e) => {
  console.error(e);
  process.exitCode = 1;
});
