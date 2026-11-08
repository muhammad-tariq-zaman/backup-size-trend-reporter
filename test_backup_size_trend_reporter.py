import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import report

def row(b, d, size):
    return {"backup": b, "date": d, "size_gb": str(size)}

class TestBackupTrend(unittest.TestCase):
    def test_growing(self):
        self.assertEqual(report([row("DB", "2026-10-01", 10), row("DB", "2026-11-01", 15)])[0][4], "GROWING")
    def test_shrinking(self):
        self.assertEqual(report([row("DB", "2026-10-01", 15), row("DB", "2026-11-01", 10)])[0][4], "SHRINKING")
    def test_flat(self):
        self.assertEqual(report([row("DB", "2026-10-01", 10), row("DB", "2026-11-01", 10.05)])[0][4], "FLAT")
    def test_largest_growth_first(self):
        r = report([row("A", "2026-10-01", 10), row("A", "2026-11-01", 11), row("B", "2026-10-01", 10), row("B", "2026-11-01", 20)])
        self.assertEqual(r[0][0], "B")
