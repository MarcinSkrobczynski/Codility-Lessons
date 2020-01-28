# Solution to Codility Lesson #3: PermMissingElem
# Copyright (c) MarcinSkrobczynski


def solution(a: list) -> int:
    return sum(x for x in range(1, len(a) + 2)) - sum(a)
