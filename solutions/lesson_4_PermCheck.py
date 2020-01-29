# Solution to Codility Lesson #4: PermCheck
# Copyright (c) MarcinSkrobczynski


def solution(a: list) -> int:
    x = len(a)
    numbers = [1] + [0] * x
    count = 0

    for i, value in enumerate(a):
        if value <= x and numbers[value] == 0:
            numbers[value] = 1
            count += 1

            if count == x:
                return 1

    return 0
