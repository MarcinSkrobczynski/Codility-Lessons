# Solution to Codility Lesson #2: CyclicRotation
# Copyright (c) MarcinSkrobczynski


def solution(a: list, k: int) -> list:

    if not a:
        return []

    for _ in range(k):
        a.insert(0, a.pop(-1))

    return a
