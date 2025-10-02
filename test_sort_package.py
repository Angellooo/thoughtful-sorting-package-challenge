import unittest
from main import sort

"""
Assumptions:
- Bulky if volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm.
- Heavy if mass ≥ 20 kg bulky nor heavy.
- STANDARD = neither.
- SPECIAL = bulky OR heavy (but not both).
- REJECTED = bulky AND heavy.
- Threshold values (exactly 1,000,000 cm³, 150 cm, or 20 kg) count as bulky/heavy.
"""

class TestPackageSorting(unittest.TestCase):

    # Standard case 
    def test_small_light_package(self):
        # Not bulky (volume < 1,000,000, all dims < 150), not heavy
        self.assertEqual(sort(10, 20, 30, 5), "STANDARD")

    # Bulky only
    def test_bulky_by_volume(self):
        # Volume = 1,000,000 exactly = bulky
        self.assertEqual(sort(200, 200, 25, 10), "SPECIAL")

    def test_bulky_by_dimension(self):
        # One dimension = 150 = bulky
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")

    def test_edge_case_volume_exact(self):
        # Exactly 1,000,000 volume = bulky
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    def test_large_dimension_over_150(self):
        # Dimension > 150 == bulky
        self.assertEqual(sort(151, 10, 10, 5), "SPECIAL")

    # Heavy only
    def test_heavy_package(self):
        # Mass = 20 = heavy
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")

    def test_heavy_above_threshold(self):
        # Mass > 20 = heavy
        self.assertEqual(sort(40, 40, 40, 25), "SPECIAL")

    # Rejected (bulky + heavy)
    def test_rejected_package(self):
        # Both bulky and heavy
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

    def test_rejected_by_dimension_and_mass(self):
        # Dimension ≥ 150 and mass ≥ 20
        self.assertEqual(sort(150, 150, 10, 20), "REJECTED")

    def test_rejected_by_volume_and_mass(self):
        # Volume ≥ 1,000,000 and mass ≥ 20
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")

    # Edge boundaries
    def test_mass_just_below_threshold(self):
        # Mass = 19.9 → not heavy
        self.assertEqual(sort(100, 100, 50, 19.9), "STANDARD")

    def test_dimension_just_below_threshold(self):
        # Dimension = 149 → not bulky
        self.assertEqual(sort(149, 100, 10, 10), "STANDARD")

    def test_volume_just_below_threshold(self):
        # Volume = 999,999 → not bulky
        self.assertEqual(sort(100, 100, 99, 10), "STANDARD")

if __name__ == "__main__":
    unittest.main()