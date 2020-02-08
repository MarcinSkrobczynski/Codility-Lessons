# Solution to Codility Lesson #5: GenomicRangeQuery
# Copyright (c) MarcinSkrobczynski

VAL = {
    'A': 1,
    'C': 2,
    'G': 3,
    'T': 4,
}


def solution(s: str, p: list, q: list) -> list:
    result = []

    for i, pair in enumerate(zip(p, q)):
        start, stop = pair

        substring = s[start:stop+1]

        for key in VAL.keys():
            if key in substring:
                result.append(VAL[key])
                break

    return result
