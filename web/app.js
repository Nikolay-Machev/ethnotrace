'use strict';
const data=window.ETHNOTRACE_DATA;
let activeEvidenceIds=null;
const $=id=>document.getElementById(id);
const esc=value=>String(value??'Unknown').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const text=value=>esc(Array.isArray(value)?value.join(', '):value||'Unknown');
const human=value=>text(value?.replaceAll('_',' '));
// Display explanations only; source records retain their original terminology.
const settingLabel=value=>value==='animal_in_vivo'?'Animal study':value;
const endpointLabel=value=>typeof value==='string'?value.replace(/glycaemic AUC/gi,'Glycaemic AUC (blood-glucose exposure over time)'):value;
const link=(url,label)=>{try{const u=new URL(url);if(!['https:','http:'].includes(u.protocol))return text(label);}catch{return text(label);}return `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${text(label)}</a>`;};
const source=(s)=>`<p>${text(s.citation)}</p>${link(s.url,'Open original source ↗')}<blockquote>${text(s.supporting_passage)}</blockquote><p><strong>Where to look:</strong> ${text(s.locator)}</p><p class="small">Source rights: ${text(s.licence)}</p>`;
$('claim').innerHTML=data.claims.map(c=>`<option value="${c.id}">${esc(c.name)} · ${c.id}</option>`).join('');
function render(){
 const selected=data.claims.find(c=>c.id===$('claim').value),t=selected.claim;
 $('account').innerHTML=`<div class="eyebrow">DOCUMENTED USE</div><h3>${text(t.species)}</h3><p>${text(t.original_use_description)}</p><p class="small"><strong>Attribution</strong><br>${text(t.community_or_nation)}</p><details><summary>Traditional source & passage</summary>${source({citation:t.citation,url:t.source_url,supporting_passage:t.supporting_passage,locator:t.passage_locator,licence:t.licence})}</details>`;
 const all=selected.results,shown=all.filter(r=>(!$('extracted').checked||r.evidence_level==='selected_full_text_experimental_unit')&&(!activeEvidenceIds||activeEvidenceIds.includes(r.evidence_id)));
 $('count').textContent=`${shown.length} shown · ${all.length} same-species candidates`;
 const renderCard=r=>{
 const s=r.study,c=r.comparison,isExtracted=r.evidence_level==='selected_full_text_experimental_unit';
 const pairs=[['Species',t.species,s.species],['Plant part',t.plant_part,s.plant_part],['Preparation',t.preparation,s.preparation],['Use / outcome',t.original_use_description,endpointLabel(s.endpoint)],['Setting','Documented traditional account',settingLabel(s.study_setting)]];
 return `<article class="card"><span class="badge">${esc(r.evidence_id)}</span><span class="badge ${isExtracted?'':'warning'}">${isExtracted?'Extracted experiment':'Literature lead · not fully extracted'}</span><h3>${text(endpointLabel(r.title))}</h3><p class="small">${r.case_id?`${esc(r.case_id)} · ${r.human_comparison_reviews} human comparison review(s) · ${r.extraction_verifications} reported extraction verifications`:'Outside the 20-case review set · unreviewed'}</p>${r.human_judgments?.length?`<p class="small">Recorded human pair judgment: ${r.human_judgments.map(j=>`Reviewer ${esc(j.reviewer.toUpperCase())}: ${human(j.label)} (${human(j.provenance?.method)})`).join('; ')}. Dimension cells remain automated.</p>`:''}<table><thead><tr><th>Field</th><th>Traditional account</th><th>Experimental study</th></tr></thead><tbody>${pairs.map(([key,a,b])=>`<tr><td>${key}</td><td>${text(a)}</td><td>${text(b)}</td></tr>`).join('')}</tbody></table><div class="outputs"><section class="output"><h4>Experimental finding</h4><strong>${isExtracted?human(c.experimental_result_direction):'Not extracted'}</strong><p>${isExtracted?text(s.reported_use_or_outcome):'This entry is a literature lead. Consult the original paper before assigning an experimental finding.'}</p><p class="small">Model: ${text(s.model)}</p></section><section class="output compare"><h4>Claim comparability · baseline</h4><strong>${human(c.status)}</strong><ul>${c.reasons.map(reason=>`<li>${esc(reason)}</li>`).join('')}</ul></section></div><details><summary>Experimental source, passage & limitations</summary>${source(r.source)}<p>${text(s.notes)}</p><p class="small">Ranking score: ${r.score.total.toFixed(3)} · species ${r.score.taxon}, part ${r.score.parts}, solvent ${r.score.solvent}, text overlap ${r.score.lexical.toFixed(3)}. This is not a confidence score.</p></details></article>`;
 };
 const experiments=shown.filter(r=>r.evidence_level==='selected_full_text_experimental_unit');
 const leads=shown.filter(r=>r.evidence_level!=='selected_full_text_experimental_unit');
 $('results').innerHTML=(experiments.length?`<section aria-label="Extracted experiments"><h3>Extracted experiments · ${experiments.length}</h3>${experiments.map(renderCard).join('')}</section>`:'<p class="empty">No indexed extracted experiments in this view. This does not establish that no research exists.</p>')+(leads.length?`<section aria-label="Literature leads"><h3>Literature leads · ${leads.length}</h3><p class="hint">Candidates for further source extraction. Grouping reflects record completeness, not scientific quality. Baseline order is preserved within each group.</p>${leads.map(renderCard).join('')}</section>`:'');
}

const dimensionNames={species:'Species',part:'Plant part',preparation:'Preparation',outcome:'Outcome',setting:'Study setting',finding:'Experimental finding'};
// Explain missing record fields without asserting that the source omits them.
function bucketLabel(account,dimension,key,fallback){
 if(dimension==='preparation'&&key==='not_established')return account.claim.preparation?'Preparation equivalence unresolved':'Traditional preparation not recorded';
 if(dimension==='outcome'&&key==='not_established')return 'Use–outcome relationship unresolved';
 return fallback;
}
function reviewSummary(account){
 const counts={};
 for(const r of account.results){
  if(r.evidence_level==='selected_full_text_experimental_unit'&&r.human_comparison_reviews>0)counts[r.human_comparison_reviews]=(counts[r.human_comparison_reviews]||0)+1;
 }
 return Object.entries(counts).map(([n,total])=>`${n} human ${n==='1'?'review':'reviews'}`).join(' · ')||'No human comparison reviews recorded';
}
function resetDrilldown(){activeEvidenceIds=null;$('drilldown').hidden=true;}
function renderAtlas(){
 const query=$('atlas-search').value.toLowerCase(),setting=$('atlas-setting').value;
 const accounts=data.claims.filter(c=>`${c.id} ${c.name} ${c.claim.community_or_nation||''} ${c.claim.original_use_description||''}`.toLowerCase().includes(query)&&(!$('atlas-missing').checked||!c.claim.preparation)&&(!setting||c.atlas.dimensions.setting[setting]));
 $('atlas-count').textContent=`${accounts.length} of ${data.claims.length} documented accounts · filters select accounts; cells retain all evidence for each account`;
 $('atlas-body').innerHTML=accounts.map(c=>{
  const a=c.atlas;
  const cells=Object.keys(dimensionNames).map(d=>{
   const buckets=Object.entries(a.dimensions[d]);
   return `<td>${buckets.length?buckets.map(([key,b])=>`<button class="atlas-cell" data-account="${esc(c.id)}" data-dimension="${d}" data-bucket="${esc(key)}">${esc(bucketLabel(c,d,key,b.label))} <strong>${b.evidence_ids.length}</strong></button>`).join(''):`<span class="small">${c.retrieval_status==='unresolved_species'?'Species unresolved':'No indexed extracted experiment'}</span>`}</td>`;
  }).join('');
  return `<tr><td><button class="account-link" data-account="${esc(c.id)}">${esc(c.name)} · ${esc(c.id)}</button><p class="small">${text(c.claim.original_use_description)}</p><p class="small">${text(c.claim.community_or_nation)}</p><span class="small">${a.experimental_units} units · ${a.unique_publications} ${a.unique_publications===1?'paper':'papers'} · ${a.literature_leads} leads<br>${esc(reviewSummary(c))}</span></td>${cells}</tr>`;
 }).join('')||'<tr><td colspan="7">No accounts match these filters.</td></tr>';
}
$('atlas-body').addEventListener('click',event=>{
 const button=event.target.closest('button[data-account]');if(!button)return;
 const c=data.claims.find(c=>c.id===button.dataset.account);$('claim').value=c.id;
 resetDrilldown();
 if(button.dataset.dimension){const d=button.dataset.dimension,b=c.atlas.dimensions[d][button.dataset.bucket];activeEvidenceIds=b.evidence_ids;$('extracted').checked=true;$('drilldown-label').textContent=`${c.name} · ${dimensionNames[d]}: ${bucketLabel(c,d,button.dataset.bucket,b.label)} · ${b.evidence_ids.length} experimental units`;$('drilldown').hidden=false;}
 else {$('extracted').checked=c.atlas.experimental_units>0;}
 render();$('explorer').scrollIntoView({behavior:'smooth',block:'start'});$('claim').focus({preventScroll:true});
});
$('clear-drilldown').addEventListener('click',()=>{resetDrilldown();render();});
for(const id of ['atlas-search','atlas-setting','atlas-missing'])$(id).addEventListener(id==='atlas-search'?'input':'change',renderAtlas);
$('claim').addEventListener('change',()=>{resetDrilldown();render();});$('extracted').addEventListener('change',render);render();renderAtlas();

