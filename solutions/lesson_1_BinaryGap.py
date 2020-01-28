# Solution to Codility Lesson #1: BinaryGap
# Copyright (c) MarcinSkrobczynski


def solution(n: int) -> int:
    digits = str(bin(n))[2:]

    maxi = 0
    counter = 0

    for d in digits:
        if d == '1':
            if counter > 0 and counter > maxi:
                maxi = counter

            counter = 0
        elif d == '0':
            counter += 1

    return maxi
