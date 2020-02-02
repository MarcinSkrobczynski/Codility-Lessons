# Solution to Codility Lesson #4: MissingInteger
# Copyright (c) MarcinSkrobczynski


def solution(a: list) -> int:
    x = len(a)
    numbers = [1] + [0] * x
    x += 1

    for i, value in enumerate(a):
        if 0 < value < x:
            numbers[value] = 1

    for i, value in enumerate(numbers):
        if value == 0:
            return i

    return x
