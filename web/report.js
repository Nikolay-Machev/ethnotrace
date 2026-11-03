'use strict';
// Pure formatter: exports the whole selected account, regardless of display filters.
function evidenceReport(account,metadata){
 const fmt=v=>v===null||v===undefined||v===''?'Unknown':Array.isArray(v)?v.join(', '):String(v);
 const lines=[`# EthnoTrace evidence report: ${account.name} (${account.id})`,'',
  `Retrieval baseline: ${metadata.baseline_version}`,
  'Scope: all indexed candidates for this account, including literature leads. Display filters do not restrict this export.',
  'Research prototype. Findings and claim comparability are separate. Missing indexed evidence does not imply absence of published research. No clinical efficacy conclusion is made.',''];
 const field=(k,v)=>lines.push(`**${k}:** ${fmt(v)}`,'');
 const cite=s=>{field('Citation',s.citation);field('Source URL',s.url||s.source_url);field('Supporting passage',s.supporting_passage);field('Locator',s.locator||s.passage_locator);field('Source rights',s.licence);};
 const t=account.claim;lines.push('## Traditional account','');
 for(const k of ['species','original_plant_name','plant_part','preparation','original_use_description','community_or_nation','location','knowledge_tradition'])field(k,t[k]);cite(t);
 lines.push('## Evidence comparisons','');
 for(const r of account.results){lines.push(`### ${r.evidence_id}: ${r.title}`,'');field('Record type',r.evidence_level);field('Paper ID',r.paper_id);
  for(const [k,v] of Object.entries(r.study))field(k,v);
  field('Experimental finding',r.evidence_level==='selected_full_text_experimental_unit'?r.comparison.experimental_result_direction:'Not extracted');
  field('Automated claim comparability',r.comparison.status);
  field('Reasons',r.comparison.reasons);field('Human comparison review count',r.human_comparison_reviews);field('Extraction verification count',r.extraction_verifications);
  for(const j of r.human_judgments||[])field(`Reviewer ${j.reviewer}`,`${j.label}; ${j.provenance?.method||'Provenance not recorded'}`);
  cite(r.source);
 }
 if(!account.results.length)lines.push('No indexed candidates. Retrieval status: '+account.retrieval_status,'');
 lines.push('## Gaps and next steps','');
 for(const g of account.gaps||[]){lines.push(`### ${g.title}`,'',g.reason,'',`Next step: ${g.next_step}`,'',`Evidence IDs: ${g.evidence_ids.join(', ')||'None'}`,'');}
 lines.push('## Targeted extraction notes','Assistant notes, separate from experimental counts; human verification is not inferred.','');
 for(const n of account.targeted_extractions||[]){lines.push(`### ${n.extraction_id}`,'');field('Extraction depth',n.extraction_depth);field('Finding',n.reported_use_or_outcome);field('Preparation',n.preparation);field('Limitations',n.limitations);cite(n);}
 return lines.join('\n');
}
if(typeof module!=='undefined')module.exports={evidenceReport};
