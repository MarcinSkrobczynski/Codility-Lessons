# Solution to Codility Lesson #2: OddOccurrencesInArray
# Copyright (c) MarcinSkrobczynski


def solution(a: list) -> int:
    result = 0
    for i in a:
        result ^= i
    return result
