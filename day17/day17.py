#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def part1(steps):
    max = 2018
    buf = []
    cur = 0
    for i in range(max):
        buf.insert(cur, i)
        cur = (cur + steps) % len(buf) + 1

    return buf[buf.index(2017) + 1]


def part2(steps):
    max = 50000000
    length = 0
    cur = 0
    for i in range(max):
        length += 1
        if cur == 1:
            last = i
        cur = (cur + steps) % length + 1

    return last


def main():
    assert part1(3) == 638
    print(part1(377))

    print(part2(377))


if __name__ == "__main__":
    sys.exit(main())
