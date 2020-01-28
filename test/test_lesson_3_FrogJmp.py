import unittest

from solutions.lesson_3_FrogJmp import solution


class TestFrogJmp(unittest.TestCase):
    def test_codility(self):
        self.assertEqual(solution(10, 85, 30), 3)

    def test_max_jumps(self):
        self.assertEqual(solution(1, 1000000000, 1), 999999999)

    def test_one_big_jump(self):
        self.assertEqual(solution(1, 1000000000, 1000000000), 1)

    def test_jump_equal(self):
        self.assertEqual(solution(1, 101, 1), 100)


if __name__ == '__main__':
    unittest.main()
