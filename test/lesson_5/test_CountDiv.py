import unittest

from solutions.lesson_5.CountDiv import solution


class TestCountDiv(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution(6, 11, 2), 3)

    def test_simple_tests(self):
        self.assertEqual(solution(0, 10, 2), 6)
        self.assertEqual(solution(1, 10, 2), 5)
        self.assertEqual(solution(1, 10, 1), 10)
        self.assertEqual(solution(1, 99, 100), 0)
        self.assertEqual(solution(100, 149, 150), 0)
        self.assertEqual(solution(101, 104, 5), 0)

    def test_max_range(self):
        self.assertEqual(solution(0, 2000000000, 1), 2000000001)


if __name__ == '__main__':
    unittest.main()
