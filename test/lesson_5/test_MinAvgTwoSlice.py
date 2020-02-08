import unittest

from solutions.lesson_5.MinAvgTwoSlice import solution


class TestMinAvgTwoSlice(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution([4, 2, 2, 5, 1, 5, 8]), 1)

    def test_simple_cases(self):
        self.assertEqual(solution([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 0)
        self.assertEqual(solution([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 8)

    def test_long_array_small_value(self):
        array = [1] * 100000
        self.assertEqual(solution(array), 0)

    def test_long_array_big_value(self):
        array = [10000] * 100000
        self.assertEqual(solution(array), 0)

    def test_long_array_different_values_incrementing(self):
        array = [x for x in range(-10000, 10000)]
        self.assertEqual(solution(array), 0)

    def test_long_array_different_values_decrementing(self):
        array = [x for x in range(10000, -10000, -1)]
        self.assertEqual(solution(array), len(array) - 2)  # -1 because last index, -2 because last pair

    def test_long_array_alternated_array(self):
        array = [4, 2, 2, 5, 1, 5, 8] * 100
        self.assertEqual(solution(array), 1)


if __name__ == '__main__':
    unittest.main()
