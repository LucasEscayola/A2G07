import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_count_string(self):
        self.assertEqual(utils.count_string("Chicken dinner"), 13)

