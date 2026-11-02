"""Reproduce the narrow Canadian diabetes-use filter against the official ZIP.

Download URL and expected SHA-256 are in data/catalogue_imported_source_rows.jsonl.
Usage: python scripts/screen_duke_archive.py /path/to/Duke-Source-CSV.zip
No download, network request or dataset mutation is performed by this script.
"""
import csv
import hashlib
import io
import json
import sys
import zipfile
from pathlib import Path
path = Path(sys.argv[1])
root = Path(__file__).resolve().parents[1]
provenance = json.loads((root / 'data/catalogue_imported_source_rows.jsonl').read_text().splitlines()[0])
if hashlib.sha256(path.read_bytes()).hexdigest() != provenance['archive_sha256']:
    raise ValueError('Archive checksum differs from the inspected snapshot')
with zipfile.ZipFile(path) as z:
    rows = list(csv.DictReader(io.TextIOWrapper(z.open('ETHNOBOT.csv'), encoding='utf-8-sig')))
relevant = [r for r in rows if any(w in r['ACTIVITY'].lower() for w in ('diabet', 'glyc'))]
canadian = [r for r in relevant if 'canad' in r['COUNTRY'].lower()]
print(json.dumps({'all_rows': len(rows), 'diabetes_or_glyc_activity_rows': len(relevant), 'explicit_canadian_rows': canadian}, indent=2))
