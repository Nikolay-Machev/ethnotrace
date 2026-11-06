'use strict';
// Pure formatter: exports the whole selected account, regardless of display filters.
function evidenceReport(account, metadata, method = 'lexical') {
  // Orders results by a ranked list of evidence IDs; unlisted IDs sort first, as with indexOf.
  function sortByRanking(results, order) {
    const position = new Map();
    order.forEach((id, i) => position.has(id) || position.set(id, i));
    const rank = (r) => position.get(r.evidence_id) ?? -1;
    return [...results].sort((a, b) => rank(a) - rank(b));
  }
  const fmt = (v) =>
    v === null || v === undefined || v === '' ? 'Unknown' : Array.isArray(v) ? v.join(', ') : String(v);
  const lines = [
    `# EthnoTrace evidence report: ${account.name} (${account.id})`,
    '',
    `Retrieval baseline: ${metadata.baseline_version}`,
    `Selected ranker: ${method}`,
    `Semantic model: ${metadata.retrieval_provider?.semantic_model || 'Not enabled'}`,
    `Model revision: ${metadata.retrieval_provider?.semantic_revision || 'Not enabled'}`,
    `Ranking input snapshot: ${metadata.retrieval_provider?.input_sha256 || 'Not available'}`,
    'Scope: all indexed candidates for this account, including literature leads. Display filters do not restrict this export.',
    'Research prototype. Findings and claim comparability are separate. Missing indexed evidence does not imply absence of published research. No clinical efficacy conclusion is made.',
    '',
  ];
  const field = (k, v) => lines.push(`**${k}:** ${fmt(v)}`, '');
  const cite = (s) => {
    field('Citation', s.citation);
    field('Source URL', s.url || s.source_url);
    field('Supporting passage', s.supporting_passage);
    field('Locator', s.locator || s.passage_locator);
    field('Source rights', s.licence);
  };
  const t = account.claim;
  lines.push('## Traditional account', '');
  for (const k of [
    'species',
    'original_plant_name',
    'plant_part',
    'preparation',
    'original_use_description',
    'community_or_nation',
    'location',
    'knowledge_tradition',
  ])
    field(k, t[k]);
  cite(t);
  lines.push('## Evidence comparisons', '');
  const order = account.rankings?.[method];
  const results = order ? sortByRanking(account.results, order) : account.results;
  for (const r of results) {
    lines.push(`### ${r.evidence_id}: ${r.title}`, '');
    field('Record type', r.evidence_level);
    field('Paper ID', r.paper_id);
    for (const [k, v] of Object.entries(r.study)) field(k, v);
    field(
      'Experimental finding',
      r.evidence_level === 'selected_full_text_experimental_unit'
        ? r.comparison.experimental_result_direction
        : 'Not extracted',
    );
    field('Automated claim comparability', r.comparison.status);
    field('Reasons', r.comparison.reasons);
    field('Human comparison review count', r.human_comparison_reviews);
    field('Extraction verification count', r.extraction_verifications);
    for (const j of r.human_judgments || [])
      field(`Reviewer ${j.reviewer}`, `${j.label}; ${j.provenance?.method || 'Provenance not recorded'}`);
    cite(r.source);
  }
  if (!account.results.length)
    lines.push('No indexed candidates. Retrieval status: ' + account.retrieval_status, '');
  lines.push('## Gaps and next steps', '');
  for (const g of account.gaps || []) {
    lines.push(
      `### ${g.title}`,
      '',
      g.reason,
      '',
      `Next step: ${g.next_step}`,
      '',
      `Record when checked: ${g.completion_criterion || 'Record a cited finding and any remaining uncertainty.'}`,
      '',
      `Evidence IDs: ${g.evidence_ids.join(', ') || 'None'}`,
      '',
    );
  }
  lines.push(
    '## Targeted extraction notes',
    'Source notes, separate from experimental counts; recorded verification and its provenance are reported below.',
    '',
  );
  for (const n of account.targeted_extractions || []) {
    lines.push(`### ${n.extraction_id}`, '');
    field('Extraction depth', n.extraction_depth);
    field('Human verification recorded', n.human_verified);
    field('Reviewer', n.human_review?.reviewer_id);
    field('Review status', n.human_review?.status);
    field('Sections checked', n.human_review?.source_and_sections_checked);
    field('Verification method', n.human_review?.verification_provenance?.method);
    field(
      'Independent blinded annotation',
      n.human_review?.verification_provenance?.independent_blinded_annotation,
    );
    field('Finding', n.reported_use_or_outcome);
    field('Preparation', n.preparation);
    field('Limitations', n.limitations);
    cite(n);
  }
  const supplementary = account.supplemental_missing_field_evidence || [];
  if (supplementary.length)
    lines.push(
      '## Supplementary source evidence',
      '',
      'Related source context only. Original records, automated comparisons and rankings are unchanged.',
      '',
    );
  for (const n of supplementary) {
    lines.push(`### ${n.record_id}: ${n.field}`, '');
    field('Original recorded value', n.original_record_value);
    field('Value supported in related source', n.source_supported_value);
    field('Source context status', n.source_context_status);
    field('Evidence and limits', n.evidence_basis);
    field(
      'Assisted research not independent human verification',
      n.assisted_research_not_independent_human_verification,
    );
    if (n.other_source_context) {
      field('Related context', n.other_source_context.related_value);
      field('Context status', n.other_source_context.status);
      field('Context limitation', n.other_source_context.reason);
    }
    for (const src of n.source_urls || []) {
      field('Source URL', src.url);
      field('Locator', src.locator);
    }
  }
  return lines.join('\n');
}
if (typeof module !== 'undefined') module.exports = { evidenceReport };
