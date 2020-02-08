import unittest

from solutions.lesson_5.GenomicRangeQuery import solution


class TestGenomicRangeQuery(unittest.TestCase):
    def test_codility(self):
        self.assertListEqual(solution("CAGCCTA", [2, 5, 0], [4, 5, 6]), [2, 4, 1])

    def test_simple_cases(self):
        self.assertListEqual(solution("CCAAGGTT", [0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 4, 5, 6, 7]),
                             [2, 2, 1, 1, 1, 1, 1, 1])
        self.assertListEqual(solution("TTGGCCAA", [0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 3, 4, 5, 6, 7]),
                             [4, 4, 3, 3, 2, 2, 1, 1])
        self.assertListEqual(solution("TTGGCCAA", [0, 0, 2, 2, 4, 4, 6, 6], [0, 1, 2, 3, 4, 5, 6, 7]),
                             [4, 4, 3, 3, 2, 2, 1, 1])

    def test_short_string_short_pq(self):
        self.assertListEqual(solution("A", [0], [0]), [1])

    def test_short_string_long_pq(self):
        array = [0] * 50000
        result = [4] * 50000
        self.assertListEqual(solution("T", array, array), result)

    def test_long_string_short_pq(self):
        string = "C" * 100000
        self.assertListEqual(solution(string, [0], [0]), [2])

    def test_long_string_long_pq_small_range(self):
        string = "G" * 100000
        array = [x for x in range(0, 50000)]
        result = [3] * 50000
        self.assertListEqual(solution(string, array, array), result)

    def test_long_string_long_pq_max_range(self):
        string = "G" * 100000
        start = [0] * 50000
        stop = [99999] * 50000
        result = [3] * 50000
        self.assertListEqual(solution(string, start, stop), result)


if __name__ == '__main__':
    unittest.main()
