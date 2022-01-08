#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


def part1(ast, bst):
    af = 16807
    bf = 48271
    m = 2147483647
    sum = 0

    a = ast
    b = bst

    for i in range(40000000):
        a = (a * af) % m
        b = (b * bf) % m
        if (a & 0xFFFF) == (b & 0xFFFF):
            sum += 1

    return sum


def part2(ast, bst):
    af = 16807
    bf = 48271
    m = 2147483647
    sum = 0

    a = ast
    b = bst

    for i in range(5000000):
        while True:
            a = (a * af) % m
            if a % 4 == 0:
                break

        while True:
            b = (b * bf) % m
            if b % 8 == 0:
                break

        if (a & 0xFFFF) == (b & 0xFFFF):
            sum += 1

    return sum


def main():
    # assert part1(65, 8921) == 588
    print(part1(873, 583))

    # assert part2(65, 8921) == 309
    print(part2(873, 583))


if __name__ == "__main__":
    sys.exit(main())
