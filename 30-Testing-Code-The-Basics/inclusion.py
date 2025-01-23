import unittest

class InclusionTests(unittest.TestCase):
    def test_inclusion(self):
        # self.assertTrue("k" in "king")
        self.assertIn("k", "king")

    def test_non_inclusion(self):
        self.assertNotIn("x", "djiwo")
if __name__ == "__main__":
    unittest.main()