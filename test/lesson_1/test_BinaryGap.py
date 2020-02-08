import unittest

from solutions.lesson_1.BinaryGap import solution


class TestBinaryGap(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(529), 4)
        self.assertEqual(solution(20), 1)
        self.assertEqual(solution(15), 0)
        self.assertEqual(solution(32), 0)
        self.assertEqual(solution(1041), 5)

    def test_max(self):
        self.assertEqual(solution(2147483647), 0)

    def test_max_with_all_successive_zeros(self):
        self.assertEqual(solution(1073741824), 0)

    def test_max_length_of_binary_gap(self):
        self.assertEqual(solution(1073741825), 29)

    def test_few_gaps(self):
        self.assertEqual(solution(1082392577), 17)

    def test_value_right_side_open(self):
        self.assertEqual(solution(1082392576), 6)


if __name__ == '__main__':
    unittest.main()
