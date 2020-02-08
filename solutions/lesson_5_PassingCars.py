# Solution to Codility Lesson #5: PassingCars
# Copyright (c) MarcinSkrobczynski


def solution(a: list) -> int:
    result = 0
    counter = 0

    for i in a:
        if i == 0:
            counter += 1
            continue
        else:
            result += counter

    return result if result <= 1e9 else -1
