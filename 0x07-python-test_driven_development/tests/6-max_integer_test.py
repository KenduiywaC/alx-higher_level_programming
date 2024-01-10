import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_integer_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_float_list(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.8, 4.2]), 4.2)

    def test_mixed_list(self):
        self.assertEqual(max_integer([1, 2.5, -3, 4.2, -1]), 4.2)

    def test_negative_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_elements(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

if __name__ == '__main__':
    unittest.main()
