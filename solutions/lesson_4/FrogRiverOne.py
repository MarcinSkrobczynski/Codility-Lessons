# Solution to Codility Lesson #4: FrogRiverOne
# Copyright (c) MarcinSkrobczynski


def solution(x: int, a: list) -> int:
    leaves = [1] + [0] * x
    count = 0

    for i, value in enumerate(a):
        if value <= x and leaves[value] == 0:
            leaves[value] = 1
            count += 1

            if count == x:
                return i

    return -1
