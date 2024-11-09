import unittest
import utils

class TestUtils(unittest.TestCase):
    
    def test_division_valid(self):
        self.assertEqual(utils.division(10, 2), 5)
        self.assertEqual(utils.division(-6, 2), -3)
    
   
    def test_division_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            utils.division(10, 0)

    def test_division_invalid_input(self):
        with self.assertRaises(TypeError):
            utils.division("10", 2)
        with self.assertRaises(TypeError):
            utils.division(10, "2")
        with self.assertRaises(TypeError):
            utils.division("10", "2")
        with self.assertRaises(TypeError):
            utils.division([], "2")
        with self.assertRaises(TypeError):
            utils.division("10", {})

