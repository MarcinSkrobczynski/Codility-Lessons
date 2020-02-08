import unittest

from solutions.lesson_5.PassingCars import solution


class TestPassingCars(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution([0, 1, 0, 1, 1]), 5)

    def test_100000_east_cars(self):
        array = [0] * 100000
        self.assertEqual(solution(array), 0)

    def test_100000_west_cars(self):
        array = [1] * 100000
        self.assertEqual(solution(array), 0)

    def test_1_east_99999_west_cars(self):
        array = [0] + [1] * 99999
        self.assertEqual(solution(array), 99999)

    def test_alternately_east_west_cars(self):
        array = [0, 1] * 50000
        self.assertEqual(solution(array), -1)


if __name__ == '__main__':
    unittest.main()
