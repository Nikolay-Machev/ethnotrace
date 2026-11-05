import subprocess
import sys
import unittest
from pathlib import Path


class GeneratedFilesTests(unittest.TestCase):
    def test_committed_outputs_match_clean_rebuild(self):
        root = Path(__file__).resolve().parents[1]
        result = subprocess.run([sys.executable, "scripts/rebuild.py", "--check"],
                                cwd=root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
