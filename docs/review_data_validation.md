# Review-data consistency check

Before evaluating or rebuilding the demo, run the structural review-link check:

```bash
python scripts/validate_review_links.py
python -m unittest discover -s tests -v
```

The check verifies that each review packet's traditional and experimental records, source fields, and evaluation-group IDs match the processed dataset; that extracted-link cases exist in the extracted-pair table; that constructed challenge cases really are species mismatches; and that development expectations, reviewer forms, and adjudications map one-to-one to the same case IDs. It also checks that the structural expectations correspond to the referenced species and current retriever membership.

This is a consistency check, **not** a source audit. It cannot establish that an extraction matches the cited paper, that a traditional-use account is represented faithfully, or that a human comparison judgment is scientifically correct. Those still require checking the cited source passages. Pending or assisted judgments remain pending or assisted; the validator does not create labels or adjudications.
