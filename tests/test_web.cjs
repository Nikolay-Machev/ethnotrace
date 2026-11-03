// Renderer and event-handler regression checks without a browser.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.resolve(__dirname,'..');
const nodes={};
for(const id of ['claim','account','extracted','count','results','atlas-search','atlas-setting','atlas-missing','atlas-count','atlas-body','drilldown','drilldown-label','clear-drilldown','explorer'])nodes[id]={value:'',checked:false,hidden:true,innerHTML:'',textContent:'',events:{},addEventListener(k,f){this.events[k]=f},scrollIntoView(){},focus(){}};
nodes.claim.value='T011';nodes.extracted.checked=true;
const ctx=vm.createContext({window:{},document:{getElementById:id=>nodes[id]},URL});
vm.runInContext(fs.readFileSync(path.join(root,'web/data.js'),'utf8'),ctx);
vm.runInContext(fs.readFileSync(path.join(root,'web/app.js'),'utf8'),ctx);
assert.match(nodes['atlas-count'].textContent,/12 of 12/);
assert.match(nodes.results.innerHTML,/reviewer confirmation after assistant judgments/);
nodes['atlas-search'].value='T008';nodes['atlas-search'].events.input();assert.match(nodes['atlas-count'].textContent,/1 of 12/);
nodes['atlas-body'].events.click({target:{closest:()=>({dataset:{account:'T008',dimension:'part',bucket:'different_parts'}})}});
assert.match(nodes.results.innerHTML,/E004/);assert.doesNotMatch(nodes.results.innerHTML,/E003/);assert.equal(nodes.drilldown.hidden,false);
nodes['clear-drilldown'].events.click();assert.match(nodes.results.innerHTML,/E003/);assert.equal(nodes.drilldown.hidden,true);
nodes.claim.value='T005';nodes.claim.events.change();assert.match(nodes.results.innerHTML,/does not establish that no research exists/);
nodes['atlas-search'].value='';nodes['atlas-setting'].value='animal_in_vivo';nodes['atlas-setting'].events.change();assert.match(nodes['atlas-count'].textContent,/4 of 12/);
nodes['atlas-setting'].value='';nodes['atlas-missing'].checked=true;nodes['atlas-missing'].events.change();assert.match(nodes['atlas-count'].textContent,/8 of 12/);
console.log('Atlas renderer, filters, cited drill-down, clear and empty states passed.');
