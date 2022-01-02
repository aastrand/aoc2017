#!/usr/bin/env python3

import sys

from .. import util


def part1(filename):
    line = util.get_lines(filename)[0]

    print(line)

    return 0


def part2(filename):
    lines = util.get_lines(filename)

    return 0


def main():
    print(part1("input.txt"))
    print(part2("input.txt"))


if __name__ == "__main__":
    sys.exit(main())
