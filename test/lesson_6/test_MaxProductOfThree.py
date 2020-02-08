import random
import unittest

from solutions.lesson_6.MaxProductOfThree import solution


class TestMaxProductOfThree(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution([-3, 1, 2, -2, 5, 6]), 60)

    def test_simple_cases(self):
        self.assertEqual(solution([10, 9, 8, 10, 7, 6, 5, 10, 4, 3, 2, 1]), 1000)
        self.assertEqual(solution([x for x in range(0, 1000)]), 999 * 998 * 997)
        self.assertEqual(solution([-10, -10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1000)
        self.assertEqual(solution([-10, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10 * 9 * 8)

    def test_not_enough_values(self):
        self.assertEqual(solution([10, 10]), 0)

    def test_long_array_different_values(self):
        array = [x for x in range(-1000, 1001)]
        random.shuffle(array)
        self.assertEqual(solution(array), 1000 * 1000 * 999)

    def test_long_array(self):
        array = [x for x in range(0, 1000)] * 100
        random.shuffle(array)
        self.assertEqual(solution(array), 999 * 999 * 999)


if __name__ == '__main__':
    unittest.main()
