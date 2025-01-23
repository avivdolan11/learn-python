import unittest

def explicit_return_sum(a, b):
    return a + b

def implixit_return_sum(a, b):
    print(a+b)

class TestNone(unittest.TestCase):
    def test_sum_functions(self):
        self.assertIsNone(implixit_return_sum(2,5))
        self.assertIsNotNone(explicit_return_sum(2,5))


if __name__ == "__main__":
    unittest.main()