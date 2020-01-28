import random
import unittest

from solutions.lesson_3_PermMissingElem import solution


class TestPermMissingElem(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution([2, 3, 1, 5]), 4)

    def test_long_array(self):
        array = [x for x in range(1, 100000)]
        random.shuffle(array)
        self.assertEqual(solution(array), 100000)

    def test_empty_array(self):
        self.assertEqual(solution([]), 1)

    def test_simple_array(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]), 10)


if __name__ == '__main__':
    unittest.main()
