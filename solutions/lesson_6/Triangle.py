# Solution to Codility Lesson #6: Triangle
# Copyright (c) MarcinSkrobczynski


def solution(a: list) -> int:
    n = len(a)

    if n < 3:
        return 0

    a.sort()

    for i in range(0, n - 2):
        if a[i] + a[i + 1] > a[i + 2]:
            return 1

    return 0
