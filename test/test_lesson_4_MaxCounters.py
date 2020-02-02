import unittest

from solutions.lesson_4_MaxCounters import solution


class TestBinaryGap(unittest.TestCase):
    def test_codility(self):
        self.assertListEqual(solution(5, [3, 4, 4, 6, 1, 4, 4]), [3, 2, 2, 4, 2])

    def test_long_array_with_small_value_and_small_N(self):
        array = [1] * 100000
        self.assertListEqual(solution(1, array), [100000])

    def test_long_array_with_small_value_and_big_N(self):
        array = [1] * 100000
        self.assertListEqual(solution(100000, array), [100000] + [0] * 99999)

    def test_long_array_repeating_10_values_and_n_20(self):
        array = [x for x in range(1, 11)] * 10000
        self.assertEqual(solution(20, array), [10000] * 10 + [0] * 10)

    def test_long_array_repeating_10_values_and_n_5(self):
        array = [x for x in range(1, 11)] * 10000
        self.assertEqual(solution(5, array), [10000] * 5)

    def test_long_array_with_one_small_value_and_other_big_and_small_N(self):
        array = [1] + [3] * 99999
        self.assertListEqual(solution(2, array), [1, 1])

    def test_long_array_repeating_4_values_and_one_bigger_than_n_and_n_5(self):
        array = [1, 2, 3, 4, 10] * 10000
        self.assertEqual(solution(5, array), [10000] * 5)

    def test_long_array_repeating_4_the_same_values_and_one_bigger_than_n_and_n_5(self):
        array = [1, 1, 1, 1, 10] * 10000
        self.assertEqual(solution(5, array), [40000] * 5)

    def test_long_array_only_big_values(self):
        array = [10] * 100000
        self.assertListEqual(solution(1, array), [0])


if __name__ == '__main__':
    unittest.main()
