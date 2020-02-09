import unittest

from solutions.lesson_6.NumberOfDiscIntersections import solution


class TestNumberOfDiscIntersections(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution([1, 5, 2, 1, 4, 0]), 11)

    def test_simple_tests(self):
        self.assertEqual(solution([1, 0, 1, 0, 1, 0, 1, 0, 1]), 12)
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]), 36)

    def test_long_array(self):
        array = [1] * 100000
        self.assertEqual(solution(array), 100000 - 2 + 100000 - 1)  # n-2 in contact, n-1 intersect

    def test_long_array_without_intersection(self):
        array = [0] * 100000
        self.assertEqual(solution(array), 0)


if __name__ == '__main__':
    unittest.main()
