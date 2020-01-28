# Solution to Codility Lesson #3: FrogJmp
# Copyright (c) MarcinSkrobczynski


def solution(x: int, y: int, d: int) -> int:
    diff = y - x
    if diff % d == 0:
        return diff // d
    else:
        return diff // d + 1
