"""Deterministic gap explanations over the indexed records, not worldwide evidence."""


def explain(claim, results, retrieval_status):
    extracted = [
        r
        for r in results
        if r["evidence_level"] == "selected_full_text_experimental_unit"
    ]
    leads = [r for r in results if r not in extracted]
    gaps = []

    def add(kind, title, reason, next_step, evidence, missingness=None):
        gaps.append(
            dict(
                kind=kind,
                title=title,
                reason=reason,
                next_step=next_step,
                evidence_ids=[r["evidence_id"] for r in evidence],
                missingness=missingness,
            )
        )

    if retrieval_status == "unresolved_species":
        add(
            "identity",
            "Plant identity unresolved",
            "Our record has no resolved scientific species. Common names alone cannot establish identity.",
            "Inspect the cited traditional source and taxonomic context before linking experiments.",
            [],
            "unresolved_identity",
        )
    elif not extracted:
        add(
            "coverage",
            "No extracted experiment indexed",
            "This collection has no extracted experimental unit for this account. This is not evidence that the use has never been studied.",
            (
                "Inspect the indexed literature leads and extract relevant methods and outcomes."
                if leads
                else "Search for evidence using the verified species and documented use; record the search scope."
            ),
            leads,
            "not_yet_extracted" if leads else "no_indexed_candidate",
        )
    if not claim.get("preparation"):
        add(
            "traditional_preparation",
            "Traditional preparation missing from record",
            "The preparation field is empty. We have not established whether the original source omits it or it has not yet been extracted.",
            "Check the traditional source and record the recipe, locator and attribution if documented. Otherwise record which source sections were checked.",
            extracted,
            "not_recorded_source_status_unresolved",
        )
    unknown = [r for r in extracted if not r["study"].get("preparation")]
    if unknown:
        add(
            "experimental_preparation",
            "Experimental preparation missing from record",
            "Some experimental records lack preparation details.",
            "Inspect the cited methods before drawing preparation comparisons.",
            unknown,
            "not_recorded_source_status_unresolved",
        )
    unresolved = [
        r for r in extracted if r["comparison"]["outcome"] == "not_established"
    ]
    if unresolved:
        add(
            "outcome_unresolved",
            "Use–outcome relationship unresolved",
            "The measured endpoint has not been established as testing the original documented use. A related glucose endpoint is not automatically the same symptom.",
            "Compare the exact traditional wording with the measured endpoint; record the interpretation and any disagreement.",
            unresolved,
            "relationship_not_established",
        )
    different = [
        r for r in extracted if r["comparison"]["outcome"] == "different_endpoint"
    ]
    if different:
        add(
            "outcome_difference",
            "A different outcome was tested",
            "The comparator identifies an endpoint different from the documented use. This can be informative without testing that claim.",
            "Inspect the cited endpoint and look for indexed studies that directly measure the documented use.",
            different,
        )
    parts = [r for r in extracted if r["comparison"]["plant_part"] == "different_parts"]
    if parts:
        add(
            "part_difference",
            "Different plant parts",
            "The mapped plant parts do not overlap.",
            "Keep these results separate; check for evidence using the documented plant part.",
            parts,
        )
    if extracted and all(
        r["study"].get("study_setting") in ("in_vitro", "animal_in_vivo")
        for r in extracted
    ):
        add(
            "setting",
            "Indexed extracted evidence is preclinical",
            "The extracted units shown here use cells or animals. This statement does not cover unextracted papers or all published research.",
            "Check existing leads for human evidence before expanding the search. Do not infer clinical effects from these experiments.",
            extracted,
        )
    if leads:
        add(
            "extraction_backlog",
            "Literature leads awaiting extraction",
            "Bibliographic or abstract records have not been converted into source-checked experimental units.",
            "Review relevance first, then extract the part, preparation, model, endpoint and limitations from accessible full text.",
            leads,
            "not_yet_extracted",
        )
    return gaps
