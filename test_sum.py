import unittest
from sum import sum
class TestMath(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(4,5),9)
        self.assertEqual(sum("4",5),9)
        self.assertEqual(sum(4,"5"),9)
        self.assertEqual(sum("4","5"),9)
        self.assertEqual(sum(),0)
        