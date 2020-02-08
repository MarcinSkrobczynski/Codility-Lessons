import unittest
import random

from solutions.lesson_6.Triangle import solution


class TestTriangle(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution([10, 2, 5, 1, 8, 20]), 1)
        self.assertEqual(solution([10, 50, 5, 1]), 0)

    def test_not_enough_values(self):
        self.assertEqual(solution([10, 10]), 0)

    def test_only_triplet(self):
        self.assertEqual(solution([10, 10, 10]), 1)
        self.assertEqual(solution([3, 4, 5]), 1)
        self.assertEqual(solution([5, 12, 13]), 1)

    def test_not_triplet(self):
        self.assertEqual(solution([10, 10, 21]), 0)
        self.assertEqual(solution([1, 5, 1]), 0)
        self.assertEqual(solution([50, 24, 24]), 0)

    def test_long_array_with_triplet_at_the_end(self):
        array = [0] * 99997 + [3, 4, 5]
        self.assertEqual(solution(array), 1)

    def test_long_random_array(self):
        array = [x for x in range(0, 100000)]
        random.shuffle(array)
        self.assertEqual(solution(array), 1)


if __name__ == '__main__':
    unittest.main()
