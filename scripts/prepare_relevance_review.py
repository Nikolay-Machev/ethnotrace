"""Enrich the existing relevance queue; preserve human answers on every rerun."""

import json
from retrieve import Baseline, ROOT, rows


def prepare():
    b = Baseline()
    p = ROOT / "data/review/retrieval_relevance.jsonl"
    queue = rows(p)
    notes = {
        r["paper_id"]: r for r in rows(ROOT / "data/curated/targeted_extractions.jsonl")
    }
    packet = [
        "<!-- Generated, do not edit. Run python3 scripts/rebuild.py. -->\n",
        "# Retrieval relevance review\n",
        "Decide whether each candidate helps assess the documented account, including "
        "methodological differences or null findings. Relevance is not claim support. "
        "Inspect the linked sources; if evidence is insufficient, leave the decision null "
        "and status pending.\n",
        "Enter decisions in `data/review/retrieval_relevance.jsonl`: "
        "`human_retrieval_relevant` (true/false), `human_rationale`, `human_reviewer_id`, "
        "`source_checked` (true), and `human_review_status` (completed). Do not copy "
        "assistant decisions without checking. The packets below omit assistant relevance "
        "labels.\n",
    ]
    for q in queue:
        c = b.cited_account(q["claim_id"])
        r = b.present(b.claims[q["claim_id"]], b.documents[q["evidence_id"]])
        q["traditional_context"] = {
            k: c.get(k)
            for k in (
                "species",
                "plant_part",
                "preparation",
                "original_use_description",
                "community_or_nation",
                "citation",
                "source_url",
                "supporting_passage",
                "passage_locator",
            )
        }
        q["experimental_context"] = r["study"]
        q.setdefault("human_reviewer_id", None)
        q.setdefault("source_checked", False)
        if q["evidence_id"] in notes:
            note = notes[q["evidence_id"]]
            q["provisional_retrieval_relevant"] = True
            q["rationale"] = (
                note["gap_relevance"]
                + " Relevance does not establish support for the traditional use."
            )
            q["annotation_method"] = (
                "assistant_targeted_source_inspection_not_human_review"
            )
            q["targeted_extraction_id"] = note["extraction_id"]
        packet += [
            f"## {q['claim_id']} / {q['evidence_id']}\n",
            f"**Documented use:** {c.get('original_use_description')}\n",
            f"**Attribution:** {c.get('community_or_nation')}\n",
            f"**Traditional source:** {c.get('citation')} — {c.get('source_url')}\n",
            f"**Traditional locator:** {c.get('passage_locator')}\n",
            f"**Traditional passage:** {c.get('supporting_passage')}\n",
            f"**Candidate:** {r['source']['citation']} — {r['source']['url']}\n",
            f"**Candidate locator:** {r['source']['locator']}\n",
            f"**Available passage:** {r['source']['supporting_passage']}\n",
            f"**Recorded endpoint:** {r['study'].get('endpoint') or 'Not extracted'}\n",
            "Record useful / not useful / unresolved and a source-based reason.\n",
        ]
    p.write_text("".join(json.dumps(q, ensure_ascii=False) + "\n" for q in queue))
    (ROOT / "docs/retrieval_review_packet.md").write_text("\n".join(packet))
    return len(queue)


if __name__ == "__main__":
    print(f"Prepared {prepare()} candidates; existing human decisions preserved.")
