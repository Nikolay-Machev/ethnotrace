const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..'),{evidenceReport}=require('../web/report.js');
const ctx=vm.createContext({window:{}});vm.runInContext(fs.readFileSync(path.join(root,'web/data.js'),'utf8'),ctx);
const data=ctx.window.ETHNOTRACE_DATA;
for(const a of data.claims){
 const report=evidenceReport(a,data);
 assert.ok(report.includes(a.claim.source_url));
 for(const r of a.results){assert.ok(report.includes(r.evidence_id));assert.ok(report.includes(r.source.citation));assert.ok(report.includes(r.source.url));}
 assert.ok(report.includes('Display filters do not restrict'));
 for(const n of a.targeted_extractions||[])assert.ok(report.includes(n.limitations));
}
const empty=evidenceReport(data.claims.find(a=>a.id==='T005'),data);assert.ok(empty.includes('unresolved_species'));
const element={innerHTML:''};const evalctx=vm.createContext({window:{},document:{getElementById:()=>element}});
vm.runInContext(fs.readFileSync(path.join(root,'web/evaluation-data.js'),'utf8'),evalctx);
vm.runInContext(fs.readFileSync(path.join(root,'web/evaluation.js'),'utf8'),evalctx);
assert.match(element.innerHTML,/Independent comparison accuracy<\/td><td>Not available/);
assert.match(element.innerHTML,/Human relevance judgments: 0 \/ 33/);
assert.match(element.innerHTML,/E004/);
assert.match(element.innerHTML,/0.917/);
console.log('All 12 account reports retain citations; evaluation preserves unavailable metrics and ranking misses.');
