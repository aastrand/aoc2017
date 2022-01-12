#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.grid import OFFSETS_STRAIGHT, print_grid

LINES = set(["|", "-"])


def solve(filename):
    lines = [l.replace("\n", "") for l in open(filename, "r")]

    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid[(x, y)] = char

            if char == "|" and y == 0:
                pos = (x, y)

    heading = (0, 1)
    letters = []
    old = pos
    steps = 0
    while True:
        pos = (pos[0] + heading[0], pos[1] + heading[1])
        char = grid.get(pos)

        if char == "+":
            for o in OFFSETS_STRAIGHT:
                n = (pos[0] + o[0], pos[1] + o[1])
                nc = grid.get(n)

                if nc != " ":
                    new_heading = (n[0] - pos[0], n[1] - pos[1])

                    if (pos[0] + new_heading[0], pos[1] + new_heading[1]) != old:
                        heading = new_heading
                        break
        elif char == " ":
            break
        elif char is None:
            raise "out of bounds at %s" % pos
        elif char not in LINES:
            letters.append(char)

        old = pos
        steps += 1

    return "".join(letters), steps + 1


def main():
    test = solve("example.txt")
    assert test[0] == "ABCDEF"
    assert test[1] == 38

    r = solve("input.txt")
    print(r[0])
    print(r[1])


if __name__ == "__main__":
    sys.exit(main())
