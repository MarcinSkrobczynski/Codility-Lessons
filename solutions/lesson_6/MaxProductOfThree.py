# Solution to Codility Lesson #6: MaxProductOfThree
# Copyright (c) MarcinSkrobczynski


def solution(a: list) -> int:
    n = len(a)

    if n < 3:
        return 0

    a.sort(reverse=True)

    return max(a[0] * a[1] * a[2], a[0] * a[-1] * a[-2])
