#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def part1(filename):
    lines = io.get_lines(filename)

    sum = 0
    for line in lines:
        nums = [int(n) for n in line.split("\t")]
        sum += max(nums) - min(nums)

    return sum


def part2(filename):
    lines = io.get_lines(filename)

    sum = 0
    for line in lines:
        nums = [int(n) for n in line.split("\t")]
        for n1 in nums:
            for n2 in nums:
                if n1 != n2 and n1 % n2 == 0:
                    sum += n1 // n2

    return sum


def main():
    assert part1("example.txt") == 18
    print(part1("input.txt"))

    assert part2("example2.txt") == 9
    print(part2("input.txt"))


if __name__ == "__main__":
    sys.exit(main())
