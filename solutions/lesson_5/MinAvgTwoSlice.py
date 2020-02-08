# Solution to Codility Lesson #5: MinAvgTwoSlice
# Copyright (c) MarcinSkrobczynski


def solution(a: list) -> int:
    minimal_average = 100000
    n = len(a)
    index = 0

    for i in range(0, n - 1):
        slice_sum = a[i]
        slice_cnt = 1

        for j in [1, 2]:
            if i + j >= n:
                continue

            slice_sum += a[i+j]
            slice_cnt += 1
            average = slice_sum / slice_cnt

            if average < minimal_average:
                index, minimal_average = i, average

    return index
