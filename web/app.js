'use strict';
const data=window.ETHNOTRACE_DATA;
const $=id=>document.getElementById(id);
const esc=value=>String(value??'Unknown').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const text=value=>esc(Array.isArray(value)?value.join(', '):value||'Unknown');
const human=value=>text(value?.replaceAll('_',' '));
const link=(url,label)=>{try{const u=new URL(url);if(!['https:','http:'].includes(u.protocol))return text(label);}catch{return text(label);}return `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${text(label)}</a>`;};
const source=(s)=>`<p>${text(s.citation)}</p>${link(s.url,'Open original source ↗')}<blockquote>${text(s.supporting_passage)}</blockquote><p><strong>Where to look:</strong> ${text(s.locator)}</p><p class="small">Source rights: ${text(s.licence)}</p>`;
$('claim').innerHTML=data.claims.map(c=>`<option value="${c.id}">${esc(c.name)} · ${c.id}</option>`).join('');
function render(){
 const selected=data.claims.find(c=>c.id===$('claim').value),t=selected.claim;
 $('account').innerHTML=`<div class="eyebrow">DOCUMENTED USE</div><h3>${text(t.species)}</h3><p>${text(t.original_use_description)}</p><p class="small"><strong>Attribution</strong><br>${text(t.community_or_nation)}</p><details><summary>Traditional source & passage</summary>${source({citation:t.citation,url:t.source_url,supporting_passage:t.supporting_passage,locator:t.passage_locator,licence:t.licence})}</details>`;
 const all=selected.results,shown=all.filter(r=>!$('extracted').checked||r.evidence_level==='selected_full_text_experimental_unit');
 $('count').textContent=`${shown.length} shown · ${all.length} same-species candidates`;
 $('results').innerHTML=shown.length?shown.map(r=>{
 const s=r.study,c=r.comparison,isExtracted=r.evidence_level==='selected_full_text_experimental_unit';
 const pairs=[['Species',t.species,s.species],['Plant part',t.plant_part,s.plant_part],['Preparation',t.preparation,s.preparation],['Use / outcome',t.original_use_description,s.endpoint],['Setting','Documented traditional account',s.study_setting]];
 return `<article class="card"><span class="badge">${esc(r.evidence_id)}</span><span class="badge ${isExtracted?'':'warning'}">${isExtracted?'Extracted experiment':'Literature lead · not fully extracted'}</span><h3>${text(r.title)}</h3><p class="small">${r.case_id?`${esc(r.case_id)} · ${r.human_comparison_reviews} human comparison review(s) · ${r.extraction_verifications} reported extraction verifications`:'Outside the 20-case review set · unreviewed'}${r.case_id&&r.human_comparison_reviews===1?' · second comparison review pending':''}</p><table><thead><tr><th>Field</th><th>Traditional account</th><th>Experimental study</th></tr></thead><tbody>${pairs.map(([key,a,b])=>`<tr><td>${key}</td><td>${text(a)}</td><td>${text(b)}</td></tr>`).join('')}</tbody><div class="outputs"><section class="output"><h4>Experimental finding</h4><strong>${isExtracted?human(c.experimental_result_direction):'Not extracted'}</strong><p>${isExtracted?text(s.reported_use_or_outcome):'This entry is a literature lead. Consult the original paper before assigning an experimental finding.'}</p><p class="small">Model: ${text(s.model)}</p></section><section class="output compare"><h4>Claim comparability · baseline</h4><strong>${human(c.status)}</strong><ul>${c.reasons.map(reason=>`<li>${esc(reason)}</li>`).join('')}</ul></section></div><details><summary>Experimental source, passage & limitations</summary>${source(r.source)}<p>${text(s.notes)}</p><p class="small">Ranking score: ${r.score.total.toFixed(3)} · species ${r.score.taxon}, part ${r.score.parts}, solvent ${r.score.solvent}, text overlap ${r.score.lexical.toFixed(3)}. This is not a confidence score.</p></details></article>`;
 }).join(''):'<p class="empty">No evidence matches this filter. Try including literature leads.</p>';
}
$('claim').addEventListener('change',render);$('extracted').addEventListener('change',render);render();
