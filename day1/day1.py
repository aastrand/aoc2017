#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def part1(line):
    sum = 0
    for i in range(0, len(line)):
        prev = i - 1
        if prev < 0:
            prev = len(line) - 1
        if line[prev] == line[i]:
            sum += int(line[i])

    return sum


def part2(line):
    sum = 0
    for i in range(0, len(line)):
        other = (i + (len(line) // 2)) % len(line)
        if line[other] == line[i]:
            sum += int(line[i])

    return sum


def main():
    assert part1("1122") == 3
    assert part1("1111") == 4
    assert part1("1234") == 0
    assert part1("91212129") == 9

    print(part1(io.get_lines("input.txt")[0]))

    assert part2("1212") == 6
    assert part2("1221") == 0
    assert part2("123425") == 4
    assert part2("123123") == 12
    assert part2("12131415") == 4

    print(part2(io.get_lines("input.txt")[0]))


if __name__ == "__main__":
    sys.exit(main())
