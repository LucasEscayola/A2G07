import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_multiply_numbers(self):
        self.assertEqual(utils.multiply_numbers(3, 6), 18)
        self.assertEqual(utils.multiply_numbers(-3, -6), 18)
        self.assertEqual(utils.multiply_numbers(3, -6), -18)
        self.assertNotEqual(utils.multiply_numbers(3, 6), 15)

