import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_review_links import validate


class ReviewLinkValidationTests(unittest.TestCase):
    def test_checked_in_review_data_links_to_the_correct_records(self):
        report = validate(ROOT)
        self.assertEqual(report['review_cases'], 20)
        self.assertEqual(report['extracted_links'], 12)
        self.assertEqual(report['constructed_species_mismatches'], 8)
        self.assertEqual(report['adjudications'], 20)

    def copied_data(self):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        shutil.copytree(ROOT / 'data', root / 'data')
        return temporary, root

    def test_rejects_case_packet_that_points_to_a_different_record(self):
        temporary, root = self.copied_data()
        with temporary:
            path = root / 'data/review/review_cases.jsonl'
            records = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
            records[0]['experiment']['record_id'] = 'E002'
            path.write_text(''.join(json.dumps(record) + '\n' for record in records), encoding='utf-8', newline='\n')
            with self.assertRaisesRegex(ValueError, 'experimental packet does not match'):
                validate(root)

    def test_rejects_expectation_attached_to_the_wrong_pair(self):
        temporary, root = self.copied_data()
        with temporary:
            path = root / 'data/evaluation/development_expectations.jsonl'
            records = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
            records[0]['evidence_id'] = 'E002'
            path.write_text(''.join(json.dumps(record) + '\n' for record in records), encoding='utf-8', newline='\n')
            with self.assertRaisesRegex(ValueError, 'expectation points to a different record pair'):
                validate(root)

    def test_rejects_duplicate_reviewer_case_mapping(self):
        temporary, root = self.copied_data()
        with temporary:
            path = root / 'data/review/reviewer_b.jsonl'
            records = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
            records[1]['case_id'] = records[0]['case_id']
            path.write_text(''.join(json.dumps(record) + '\n' for record in records), encoding='utf-8', newline='\n')
            with self.assertRaisesRegex(ValueError, 'Duplicate reviewer b case_id'):
                validate(root)


if __name__ == '__main__':
    unittest.main()
