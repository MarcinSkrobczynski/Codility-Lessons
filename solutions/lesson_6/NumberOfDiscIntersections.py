# Solution to Codility Lesson #6: NumberOfDiscIntersections
# Copyright (c) MarcinSkrobczynski


def solution(a: list) -> int:
    discs = []
    for j, r in enumerate(a):
        discs.extend([(j - r, True), (j + r, False)])

    discs.sort(key=lambda x: (x[0], not x[1]))

    intersections = 0
    num_of_discs = 0

    for _, starts in discs:
        if starts:
            intersections += num_of_discs
            num_of_discs += 1
        else:
            num_of_discs -= 1

    return intersections if intersections <= 10e6 else -1
