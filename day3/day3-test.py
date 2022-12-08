import unittest
from day3 import shared_item, priority

class TestDay3(unittest.TestCase):
    def test_shared_element_1(self):
        result = shared_item(test_row_1)
        self.assertEqual(result, 'p', f'for {test_row_1} result should be "p"')

    def test_shared_element_2(self):
        result = shared_item(test_row_2)
        self.assertEqual(result, 'P', f'for {test_row_2} result should be "P"')

    def test_shared_element_3(self):
        result = shared_item(test_row_3)
        self.assertEqual(result, 't', f'for {test_row_3} result should be "t"')

    def test_priority(self):
        self.assertEqual(priority('p'), 16)

test_row_1 = "vJrwpWtwJgWrhcsFMMfFFhFp"
test_row_2 = "PmmdzqPrVvPwwTWBwg"
test_row_3 = "ttgJtRGJQctTZtZT"

if __name__ == '__main__':
    unittest.main()
