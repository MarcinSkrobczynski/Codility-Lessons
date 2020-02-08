# Solution to Codility Lesson #4: MaxCounters
# Copyright (c) MarcinSkrobczynski


def solution(n: int, a: list) -> list:
    result = [1] + [0] * n

    max_counter = 0
    global_max = 0

    for i in a:
        if 1 <= i <= n:
            if result[i] < global_max:
                result[i] = global_max

            result[i] += 1

            if max_counter < result[i]:
                max_counter = result[i]

        else:
            global_max = max_counter

    for j in range(1, n + 1):
        if result[j] < global_max:
            result[j] = global_max

    return result[1:]
