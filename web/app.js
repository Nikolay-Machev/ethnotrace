'use strict';
const data = window.ETHNOTRACE_DATA;
let activeEvidenceIds = null;
let activeGapDimension = null;
const $ = (id) => document.getElementById(id);
const esc = (value) =>
  String(value ?? 'Unknown').replace(
    /[&<>"']/g,
    (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c],
  );
const text = (value) => esc(Array.isArray(value) ? value.join(', ') : value || 'Unknown');
const human = (value) => text(value?.replaceAll('_', ' '));
// Display explanations only; source records retain their original terminology.
const settingLabel = (value) => (value === 'animal_in_vivo' ? 'Animal study' : value);
const endpointLabel = (value) =>
  typeof value === 'string'
    ? value.replace(/glycaemic AUC/gi, 'Glycaemic AUC (blood-glucose exposure over time)')
    : value;
const link = (url, label) => {
  try {
    const u = new URL(url);
    if (!['https:', 'http:'].includes(u.protocol)) return text(label);
  } catch {
    return text(label);
  }
  return `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${text(label)}</a>`;
};
const source = (s) =>
  `<p>${text(s.citation)}</p>${link(s.url, 'Open original source ↗')}<blockquote>${text(s.supporting_passage)}</blockquote><p><strong>Where to look:</strong> ${text(s.locator)}</p><p class="small">Source rights: ${text(s.licence)}</p>`;
$('ranking').innerHTML =
  '<option value="lexical">Lexical baseline (default)</option>' +
  (data.retrieval_provider.semantic_enabled
    ? '<option value="semantic">Semantic challenger (MiniLM)</option><option value="hybrid">Hybrid challenger (rank fusion)</option>'
    : '');
$('ranking').value = 'lexical';
$('claim').innerHTML = data.claims
  .map((c) => `<option value="${c.id}">${esc(c.name)} · ${c.id}</option>`)
  .join('');
function render() {
  const selected = data.claims.find((c) => c.id === $('claim').value),
    t = selected.claim;
  $('account').innerHTML =
    `<div class="eyebrow">DOCUMENTED USE</div><h3>${text(t.species)}</h3><p>${text(t.original_use_description)}</p><p class="small"><strong>Attribution</strong><br>${text(t.community_or_nation)}</p><details><summary>Traditional source & passage</summary>${source({ citation: t.citation, url: t.source_url, supporting_passage: t.supporting_passage, locator: t.passage_locator, licence: t.licence })}</details>`;
  const mode = $('ranking').value || 'lexical';
  const order = selected.rankings?.[mode];
  const all = order
    ? [...selected.results].sort((a, b) => order.indexOf(a.evidence_id) - order.indexOf(b.evidence_id))
    : selected.results;
  $('ranking-note').textContent =
    mode === 'lexical'
      ? 'Species, plant-part, solvent and text-overlap baseline.'
      : 'Pretrained semantic challenger. Similarity and rank fusion are not evidence quality, medical equivalence or confidence scores.';
  const shown = all.filter(
    (r) =>
      (!$('extracted').checked || r.evidence_level === 'selected_full_text_experimental_unit') &&
      (!activeEvidenceIds || activeEvidenceIds.includes(r.evidence_id)),
  );
  renderGaps(selected);
  $('count').textContent = `${shown.length} shown · ${all.length} same-species candidates`;
  const renderCard = (r) => {
    const s = r.study,
      c = r.comparison,
      isExtracted = r.evidence_level === 'selected_full_text_experimental_unit';
    const pairs = [
      ['Species', t.species, s.species],
      ['Plant part', t.plant_part, s.plant_part],
      ['Preparation', t.preparation, s.preparation],
      ['Use / outcome', t.original_use_description, endpointLabel(s.endpoint)],
      ['Setting', 'Documented traditional account', settingLabel(s.study_setting)],
    ];
    return `<article class="card"><span class="badge">${esc(r.evidence_id)}</span><span class="badge ${isExtracted ? '' : 'warning'}">${isExtracted ? 'Extracted experiment' : 'Literature lead · not fully extracted'}</span><h3>${text(endpointLabel(r.title))}</h3><p class="small">${r.case_id ? `${esc(r.case_id)} · ${r.human_comparison_reviews} human comparison review(s) · ${r.extraction_verifications} reported extraction verifications` : 'Outside the 20-case review set · unreviewed'}</p>${r.human_judgments?.length ? `<p class="small">Recorded human pair judgment: ${r.human_judgments.map((j) => `Reviewer ${esc(j.reviewer.toUpperCase())}: ${human(j.label)} (${human(j.provenance?.method)})`).join('; ')}. Dimension cells remain automated.</p>` : ''}<table><thead><tr><th>Field</th><th>Traditional account</th><th>Experimental study</th></tr></thead><tbody>${pairs.map(([key, a, b]) => `<tr><td>${key}</td><td>${text(a)}</td><td>${text(b)}</td></tr>`).join('')}</tbody></table><div class="outputs"><section class="output"><h4>Experimental finding</h4><strong>${isExtracted ? human(c.experimental_result_direction) : 'Not extracted'}</strong><p>${isExtracted ? text(s.reported_use_or_outcome) : 'This entry is a literature lead. Consult the original paper before assigning an experimental finding.'}</p><p class="small">Model: ${text(s.model)}</p></section><section class="output compare"><h4>Claim comparability · baseline</h4><strong>${human(c.status)}</strong><ul>${c.reasons.map((reason) => `<li>${esc(reason)}</li>`).join('')}</ul></section></div><details><summary>Experimental source, passage & limitations</summary>${source(r.source)}<p>${text(s.notes)}</p><p class="small">Lexical baseline score: ${r.score.total.toFixed(3)} · species ${r.score.taxon}, part ${r.score.parts}, solvent ${r.score.solvent}, text overlap ${r.score.lexical.toFixed(3)}. This is not a confidence score.</p>${selected.rankings ? `<p class="small">Semantic cosine: ${selected.rankings.cosine[r.evidence_id].toFixed(3)} · Hybrid rank-fusion score: ${selected.rankings.rrf[r.evidence_id].toFixed(5)}. These scores only order candidates.</p>` : ''}</details></article>`;
  };
  const experiments = shown.filter((r) => r.evidence_level === 'selected_full_text_experimental_unit');
  const leads = shown.filter((r) => r.evidence_level !== 'selected_full_text_experimental_unit');
  $('results').innerHTML =
    (experiments.length
      ? `<section aria-label="Extracted experiments"><h3>Extracted experiments · ${experiments.length}</h3>${experiments.map(renderCard).join('')}</section>`
      : '<p class="empty">No indexed extracted experiments in this view. This does not establish that no research exists.</p>') +
    (leads.length
      ? `<section aria-label="Literature leads"><h3>Literature leads · ${leads.length}</h3><p class="hint">Candidates for further source extraction. Grouping reflects record completeness, not scientific quality. The selected ranking is preserved within each group.</p>${leads.map(renderCard).join('')}</section>`
      : '');
}

const dimensionNames = {
  species: 'Species',
  part: 'Plant part',
  preparation: 'Preparation',
  outcome: 'Outcome',
  setting: 'Study setting',
  finding: 'Experimental finding',
};
// Explain missing record fields without asserting that the source omits them.
function bucketLabel(account, dimension, key, fallback) {
  if (dimension === 'preparation' && key === 'not_established')
    return account.claim.preparation
      ? 'Preparation equivalence unresolved'
      : 'Traditional preparation not recorded';
  if (dimension === 'outcome' && key === 'not_established') return 'Use–outcome relationship unresolved';
  return fallback;
}
function reviewSummary(account) {
  const counts = {};
  for (const r of account.results) {
    if (r.evidence_level === 'selected_full_text_experimental_unit' && r.human_comparison_reviews > 0)
      counts[r.human_comparison_reviews] = (counts[r.human_comparison_reviews] || 0) + 1;
  }
  return (
    Object.entries(counts)
      .map(([n, total]) => `${n} human ${n === '1' ? 'review' : 'reviews'}`)
      .join(' · ') || 'No human comparison reviews recorded'
  );
}
function resetDrilldown() {
  activeEvidenceIds = null;
  activeGapDimension = null;
  $('drilldown').hidden = true;
}
function renderAtlas() {
  const query = $('atlas-search').value.toLowerCase(),
    setting = $('atlas-setting').value;
  const accounts = data.claims.filter(
    (c) =>
      `${c.id} ${c.name} ${c.claim.community_or_nation || ''} ${c.claim.original_use_description || ''}`
        .toLowerCase()
        .includes(query) &&
      (!$('atlas-missing').checked || !c.claim.preparation) &&
      (!setting || c.atlas.dimensions.setting[setting]),
  );
  $('atlas-count').textContent =
    `${accounts.length} of ${data.claims.length} documented accounts · filters select accounts; cells retain all evidence for each account`;
  $('atlas-body').innerHTML =
    accounts
      .map((c) => {
        const a = c.atlas;
        const cells = Object.keys(dimensionNames)
          .map((d) => {
            const buckets = Object.entries(a.dimensions[d]);
            return `<td>${buckets.length ? buckets.map(([key, b]) => `<button class="atlas-cell" data-account="${esc(c.id)}" data-dimension="${d}" data-bucket="${esc(key)}">${esc(bucketLabel(c, d, key, b.label))} <strong>${b.evidence_ids.length}</strong></button>`).join('') : `<span class="small">${c.retrieval_status === 'unresolved_species' ? 'Species unresolved' : 'No indexed extracted experiment'}</span>`}</td>`;
          })
          .join('');
        return `<tr><td><button class="account-link" data-account="${esc(c.id)}">${esc(c.name)} · ${esc(c.id)}</button><p class="small">${text(c.claim.original_use_description)}</p><p class="small">${text(c.claim.community_or_nation)}</p><span class="small">${a.experimental_units} units · ${a.unique_publications} ${a.unique_publications === 1 ? 'paper' : 'papers'} · ${a.literature_leads} leads<br>${esc(reviewSummary(c))}</span></td>${cells}</tr>`;
      })
      .join('') || '<tr><td colspan="7">No accounts match these filters.</td></tr>';
}
$('atlas-body').addEventListener('click', (event) => {
  const button = event.target.closest('button[data-account]');
  if (!button) return;
  const c = data.claims.find((c) => c.id === button.dataset.account);
  $('claim').value = c.id;
  resetDrilldown();
  if (button.dataset.dimension) {
    activeGapDimension = button.dataset.dimension;
    const d = button.dataset.dimension,
      b = c.atlas.dimensions[d][button.dataset.bucket];
    activeEvidenceIds = b.evidence_ids;
    $('extracted').checked = true;
    $('drilldown-label').textContent =
      `${c.name} · ${dimensionNames[d]}: ${bucketLabel(c, d, button.dataset.bucket, b.label)} · ${b.evidence_ids.length} experimental units`;
    $('drilldown').hidden = false;
  } else {
    $('extracted').checked = c.atlas.experimental_units > 0;
  }
  render();
  $('explorer').scrollIntoView({ behavior: 'smooth', block: 'start' });
  $('claim').focus({ preventScroll: true });
});
$('clear-drilldown').addEventListener('click', () => {
  resetDrilldown();
  render();
});
for (const id of ['atlas-search', 'atlas-setting', 'atlas-missing'])
  $(id).addEventListener(id === 'atlas-search' ? 'input' : 'change', renderAtlas);
$('ranking').addEventListener('change', render);
$('claim').addEventListener('change', () => {
  resetDrilldown();
  render();
});
$('extracted').addEventListener('change', render);
render();
renderAtlas();

function renderSupplementary(account) {
  const notes = account.supplemental_missing_field_evidence || [];
  if (!notes.length) return '';
  return `<h3>Supplementary source evidence</h3><p class="small">Related source context, not a replacement for the original account or experiment. Automated comparisons and rankings use the original records.</p>${notes.map((n) => `<details class="supplementary-source"><summary>${esc(n.record_id)} · ${human(n.field)} · ${n.source_supported_value ? text(n.source_supported_value) : 'Account-specific value unresolved'}</summary><p><strong>Original recorded value:</strong> ${text(n.original_record_value)}</p><p><strong>Value supported in the related source:</strong> ${text(n.source_supported_value)}</p><p><strong>Source context:</strong> ${human(n.source_context_status)}</p><p>${text(n.evidence_basis)}</p>${n.other_source_context ? `<p><strong>Other context:</strong> ${text(n.other_source_context.related_value)} · ${human(n.other_source_context.status)}</p><p>${text(n.other_source_context.reason)}</p>` : ''}<p class="small">${n.assisted_research_not_independent_human_verification ? 'Assisted source research; not independent human verification.' : ''}</p>${(n.source_urls || []).map((s) => `<p>${link(s.url, 'Open supporting source ↗')}<br><strong>Locator:</strong> ${text(s.locator)}</p>`).join('') || '<p>No supporting URL recorded for this audit entry.</p>'}</details>`).join('')}`;
}
function renderGaps(account) {
  const notes = account.targeted_extractions || [];
  $('gaps').innerHTML =
    `<h3>Research gaps & next steps</h3><p class="small">Based on this indexed collection. Missing record fields do not establish missing information in the original source.</p>${(
      account.gaps || []
    )
      .map(
        (g) =>
          `<details ${({ preparation: ['traditional_preparation', 'experimental_preparation'], outcome: ['outcome_unresolved', 'outcome_difference', 'endpoint_coverage', 'source_access'], part: ['part_difference'], setting: ['setting'], species: ['identity'] }[activeGapDimension] || []).includes(g.kind) ? 'open' : ''}><summary>${esc(g.title)}</summary><p>${esc(g.reason)}</p><p><strong>Next step:</strong> ${esc(g.next_step)}</p><p><strong>Record when checked:</strong> ${esc(g.completion_criterion)}</p><p class="small">Traditional account: ${esc(account.id)} · ${link(account.claim.source_url, 'Traditional source')}</p>${g.evidence_ids
            .map((id) => {
              const r = account.results.find((r) => r.evidence_id === id);
              return `<p class="small">${esc(id)}: ${link(r.source.url, r.source.citation)}</p>`;
            })
            .join('')}</details>`,
      )
      .join(
        '',
      )}${notes.length ? `<h3>Targeted source extractions</h3><p class="small">Source extractions with recorded review status. Context notes are separate from the atlas experiment counts.</p>${notes.map((n) => `<details><summary>${esc(n.extraction_id)} · ${n.extraction_depth === 'partial_indexed_sections' ? 'Partial extraction' : 'Methods and table inspected'} · ${esc(n.endpoint)}</summary><p><strong>Verification:</strong> ${n.human_verified ? 'Human confirmation recorded' : 'No completed human verification recorded'} · ${text(n.human_review?.reviewer_id)} · ${human(n.human_review?.status)}</p><p class="small">${human(n.human_review?.verification_provenance?.method)}. ${n.human_review?.verification_provenance?.independent_blinded_annotation === false ? 'Assisted confirmation; not independent blinded review.' : ''}</p><p><strong>Sections checked:</strong> ${text(n.human_review?.source_and_sections_checked)}</p><p>${esc(n.gap_relevance)}</p><p>${esc(n.reported_use_or_outcome)}</p><p><strong>Preparation:</strong> ${text(n.preparation)}</p><p><strong>Setting:</strong> ${human(n.study_setting)}</p>${source({ citation: n.citation, url: n.source_url, supporting_passage: n.supporting_passage, locator: n.passage_locator, licence: n.licence })}<p><strong>Limitations:</strong> ${esc(n.limitations)}</p></details>`).join('')}` : ''}`;
  $('gaps').innerHTML += renderSupplementary(account);
}

$('export-report').addEventListener('click', () => {
  const selected = data.claims.find((c) => c.id === $('claim').value);
  const url = URL.createObjectURL(
    new Blob([evidenceReport(selected, data, $('ranking').value)], { type: 'text/markdown;charset=utf-8' }),
  );
  const anchor = document.createElement('a');
  anchor.href = url;
  anchor.download = `ethnotrace-${selected.id}-evidence.md`;
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});
