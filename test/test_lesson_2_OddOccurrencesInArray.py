import random
import unittest

from solutions.lesson_2_OddOccurrencesInArray import solution


class TestOddOccurrencesInArray(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution([9, 3, 9, 3, 9, 7, 9]), 7)

    def test_long_array_with_zeros_and_one_value_in_the_middle(self):
        array = [0] * 999999
        array[500000] = 1
        self.assertEqual(solution(array), 1)

    def test_long_array_with_non_zeros_and_one_value_in_the_middle(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * 100000
        array.pop(-1)
        random.shuffle(array)
        self.assertEqual(solution(array), 9)

    def test_long_array_with_many_different_values(self):
        array = [x for x in range(1000000000, 1000000000-500000, -1)] * 2
        array.pop(0)
        random.shuffle(array)
        self.assertEqual(solution(array), 1000000000)


if __name__ == '__main__':
    unittest.main()
