# Solution to Codility Lesson #3: TapeEquilibrium
# Copyright (c) MarcinSkrobczynski


def solution(a: list) -> int:
    left = sum(a[:1])
    right = sum(a[1:])
    min_diff = abs(right - left)

    for i in range(1, len(a) - 1):
        left += a[i]
        right -= a[i]
        min_diff = min(abs(right - left), min_diff)

    return min_diff
