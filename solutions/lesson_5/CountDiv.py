# Solution to Codility Lesson #5: CountDiv
# Copyright (c) MarcinSkrobczynski


def solution(a: int, b: int, k: int) -> int:
    x = a // k
    y = b // k
    return y - x if a % k != 0 else y - x + 1
