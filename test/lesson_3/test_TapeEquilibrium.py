import unittest

from solutions.lesson_3.TapeEquilibrium import solution


class TestTapeEquilibrium(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution([3, 1, 2, 4, 3]), 1)

    def test_long_array_with_the_same_value(self):
        array = [1] * 100000
        self.assertEqual(solution(array), 0)

    def test_long_array_with_different_values(self):
        array = [x for x in range(-1000, 1000)]
        self.assertEqual(solution(array), 1000)


if __name__ == '__main__':
    unittest.main()
