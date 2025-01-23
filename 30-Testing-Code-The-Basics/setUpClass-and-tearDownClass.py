import unittest

class TestOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run once before test suite starts")

    def setUp(self):
        print("This will run before")

    def tearDown(self):
        print("This will run after")

    @classmethod
    def tearDownClass(cls):
        print("This will run once after the test suite finishes")

    def test_stuff(self):
        self.assertEqual(1,1)

    def test_more_stuff(self):
        self.assertEqual([], [])

if __name__ == "__main__":
    unittest.main()