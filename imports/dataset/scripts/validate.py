"""Validate active EthnoTrace files. Archived examples are excluded."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = {"record_id", "dataset_scope", "source_key", "species", "original_plant_name",
        "plant_part", "preparation", "reported_use_or_outcome", "study_setting",
        "source_id", "source_url", "supporting_passage", "passage_locator", "licence",
        "notes", "curation_method", "review_status", "accessed_on", "language"}
TRADITIONAL = {"knowledge_tradition", "community_or_nation", "knowledge_holder",
               "location", "historical_period", "original_use_description",
               "original_use_description_type", "diabetes_relevance",
               "relevance_rationale", "administration_route", "access_or_reuse_conditions"}
EXPERIMENTS = {"animal_in_vivo", "isolated_tissue_ex_vivo", "in_vitro",
               "human_randomized_trial", "human_observational"}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def load_records(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def validate(root=ROOT):
    catalogue = json.loads((root / "data/sources.json").read_text(encoding="utf-8"))
    require(catalogue["scope"] == "canadian_diabetes", "Incorrect catalogue scope")
    entries = catalogue["sources"]
    sources = {s["source_key"]: s for s in entries}
    require(len(sources) == len(entries), "Duplicate source key")
    for s in entries:
        required = {"source_key", "title", "source_url", "source_id", "licence",
                    "licence_url", "original_format", "import_scope", "attribution", "accessed_on"}
        require(required <= s.keys(), "Missing source metadata")
    seen, used, counts = set(), set(), {}
    for filename, prefix in [("traditional_records", "T"), ("experimental_records", "E")]:
        records = load_records(root / f"data/{filename}.jsonl")
        counts[filename] = len(records)
        for r in records:
            rid = r.get("record_id", "<missing>")
            require(BASE <= r.keys(), f"{rid}: missing core fields")
            require(re.fullmatch(prefix + r"[0-9]{3,}", rid) is not None, f"{rid}: invalid ID")
            require(rid not in seen, f"{rid}: duplicate ID")
            seen.add(rid)
            require(r["dataset_scope"] == "canadian_diabetes", f"{rid}: wrong scope")
            require(r["species"] is None or
                    (isinstance(r["species"], list) and len(r["species"]) > 0 and
                     all(isinstance(s, str) and s.strip() for s in r["species"])),
                    f"{rid}: invalid species")
            require(isinstance(r["original_plant_name"], list) and
                    len(r["original_plant_name"]) > 0 and
                    all(isinstance(n, str) and n.strip() for n in r["original_plant_name"]),
                    f"{rid}: missing original names")
            require(r["source_key"] in sources, f"{rid}: unknown source")
            s = sources[r["source_key"]]
            used.add(r["source_key"])
            require(all(r[k] == s[k] for k in ("source_id", "source_url", "licence")),
                    f"{rid}: inconsistent source metadata")
            for k in ("supporting_passage", "passage_locator", "reported_use_or_outcome"):
                require(isinstance(r[k], str) and r[k].strip(), f"{rid}: empty {k}")
            require(re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", r["accessed_on"]) is not None,
                    f"{rid}: invalid access date")
            require(r["review_status"] in {"pending_independent_review", "independently_reviewed"},
                    f"{rid}: invalid review status")
            if prefix == "T":
                require(TRADITIONAL <= r.keys(), f"{rid}: missing traditional-use fields")
                require(r["study_setting"] == "documented_folk_use", f"{rid}: invalid traditional setting")
                require(r["knowledge_tradition"] in
                        {"indigenous", "settler", "documented_exchange", "unspecified"},
                        f"{rid}: invalid tradition")
                require(r["diabetes_relevance"] in {"explicit", "symptom_associated", "unclear"},
                        f"{rid}: invalid relevance")
                require(r["original_use_description_type"] in {"quotation", "paraphrase"},
                        f"{rid}: invalid description type")
                require(bool(r["relevance_rationale"]) and bool(r["access_or_reuse_conditions"]),
                        f"{rid}: missing context")
            else:
                require(r["study_setting"] in EXPERIMENTS, f"{rid}: invalid experimental setting")
    require(used == set(sources), "Unreferenced sources belong in source leads")
    return counts, len(sources)

if __name__ == "__main__":
    counts, sources = validate()
    print(f"PASS: {counts['traditional_records']} traditional records, "
          f"{counts['experimental_records']} experimental records, {sources} sources")
