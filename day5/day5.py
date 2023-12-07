#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def solve(filename, part2=False):
    ops = [int(o) for o in io.get_lines(filename)]

    pos = 0
    steps = 0
    while pos < len(ops):
        op = ops[pos]

        if part2 and op >= 3:
            ops[pos] -= 1
        else:
            ops[pos] += 1

        pos += op
        steps += 1

    return steps


def main():
    assert solve("example.txt") == 5
    print(solve("../input/2017/day5.txt"))

    assert solve("example.txt", True) == 10
    print(solve("../input/2017/day5.txt", True))


if __name__ == "__main__":
    sys.exit(main())
