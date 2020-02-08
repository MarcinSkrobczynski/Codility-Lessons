import unittest

from solutions.lesson_6.Distinct import solution


class TestDistinct(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution([2, 1, 1, 2, 3, 1]), 3)

    def test_empty_list(self):
        self.assertEqual(solution([]), 0)

    def test_long_array_the_same_value(self):
        array = [1] * 100000
        self.assertEqual(solution(array), 1)

    def test_long_array_different_values(self):
        array = [x for x in range(0, 100000)]
        self.assertEqual(solution(array), 100000)


if __name__ == '__main__':
    unittest.main()
