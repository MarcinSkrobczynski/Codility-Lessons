import unittest

from solutions.lesson_4_MissingInteger import solution


class TestBinaryGap(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution([1, 3, 6, 4, 1, 2]), 5)
        self.assertEqual(solution([1, 2, 3]), 4)
        self.assertEqual(solution([-1, -3]), 1)

    def test_long_array_ones(self):
        array = [1] * 100000
        self.assertEqual(solution(array), 2)

    def test_long_array_not_ones(self):
        array = [1000000] * 100000
        self.assertEqual(solution(array), 1)

    def test_long_array_only_negatives(self):
        array = [x for x in range(-1000000, -1000000+100000)]
        self.assertEqual(solution(array), 1)

    def test_long_array_only_positives_incrementing(self):
        array = [x for x in range(1, 100001)]
        self.assertEqual(solution(array), 100001)

    def test_long_array_only_positives_repeating(self):
        array = [x for x in range(1, 11)] * 10000
        self.assertEqual(solution(array), 11)


if __name__ == '__main__':
    unittest.main()
