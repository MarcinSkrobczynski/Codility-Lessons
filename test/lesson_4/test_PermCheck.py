import unittest
import random

from solutions.lesson_4.PermCheck import solution


class TestPermCheck(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution([4, 1, 3, 2]), 1)
        self.assertEqual(solution([4, 1, 3]), 0)

    def test_short_array_permutation(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)

    def test_long_array_permutation(self):
        array = [x for x in range(1, 100001)]
        random.shuffle(array)
        self.assertEqual(solution(array), 1)

    def test_short_array_not_permutation(self):
        self.assertEqual(solution([4, 5, 3, 2]), 0)

    def test_long_array_not_permutation(self):
        array = [x for x in range(0, 100000)]
        random.shuffle(array)
        self.assertEqual(solution(array), 0)

    def test_long_array_with_big_values_not_permutation(self):
        array = [1000000000] * 100000
        self.assertEqual(solution(array), 0)


if __name__ == '__main__':
    unittest.main()
