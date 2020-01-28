import unittest

from solutions.lesson_2_CyclicRotation import solution


class TestCyclicRotation(unittest.TestCase):
    def test_codility(self):
        self.assertListEqual(solution([3, 8, 9, 7, 6], 1), [6, 3, 8, 9, 7])
        self.assertListEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertListEqual(solution([0, 0, 0], 1), [0, 0, 0])
        self.assertListEqual(solution([1, 2, 3, 4], 4), [1, 2, 3, 4])

    def test_long_list_many_times(self):
        array = [x for x in range(100)]
        self.assertListEqual(solution(array, 100), array)

    def test_long_list_0_times(self):
        array = [x for x in range(100)]
        self.assertListEqual(solution(array, 0), array)

    def test_short_list_many_times(self):
        self.assertListEqual(solution([1], 100), [1])

    def test_empty_array(self):
        self.assertListEqual(solution([], 100), [])


if __name__ == '__main__':
    unittest.main()
