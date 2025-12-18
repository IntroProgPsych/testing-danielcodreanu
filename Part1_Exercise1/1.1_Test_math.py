
import unittest
from mathexercise import add

class TestAddFunction(unittest.TestCase):
    # TODO:
    # - Write tests for:
    #   * adding two positive numbers
    #   * adding two negative numbers
    #   * adding a positive and a negative number
    # - Use assertEqual to check the results.
    # - Use clear method names, e.g. test_add_positive_numbers, etc.

    # write your tests here:
    def testnumbers(self):
        self.assertEqual(add(8,7), 15)
        self.assertEqual(add(-5,-9), -14)
        self.assertEqual(add(4,6),10)
        






if __name__ == "__main__":
    unittest.main()
