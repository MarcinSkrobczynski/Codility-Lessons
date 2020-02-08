import unittest

from solutions.lesson_4.FrogRiverOne import solution


class TestFrogRiverOne(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]), 6)

    def test_long_array_short_distance(self):
        array = [1] * 99999 + [2]
        self.assertEqual(solution(2, array), 99999)

    def test_long_array_long_distance(self):
        array = [x for x in range(1, 100001)]
        self.assertEqual(solution(100000, array), 99999)

    def test_short_array(self):
        self.assertEqual(solution(1, [1]), 0)

    def test_short_array_wrong_value(self):
        self.assertEqual(solution(1, [2]), -1)

    def test_long_array_never_cross(self):
        array = [1] * 100000
        self.assertEqual(solution(2, array), -1)


if __name__ == '__main__':
    unittest.main()
