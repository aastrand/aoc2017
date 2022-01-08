#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io

#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \

# https://www.redblobgames.com/grids/hexagons/#coordinates-cube
OFFSETS = {
    "n": (1, -1, 0),
    "s": (-1, 1, 0),
    "nw": (0, -1, 1),
    "ne": (1, 0, -1),
    "se": (0, 1, -1),
    "sw": (-1, 0, 1),
}


def walk(input):
    pos = (0, 0, 0)
    steps = [pos]
    for step in input.split(","):
        pos = (
            pos[0] + OFFSETS[step][0],
            pos[1] + OFFSETS[step][1],
            pos[2] + OFFSETS[step][2],
        )
        steps.append(pos)

    return pos, steps


def cube_subtract(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


# https://www.redblobgames.com/grids/hexagons/#distances
def cube_dist(a, b):
    diff = cube_subtract(a, b)
    return (abs(diff[0]) + abs(diff[1]) + abs(diff[2])) // 2


def solve(input):
    start = (0, 0, 0)
    pos, path = walk(input)

    return cube_dist(start, pos), max([cube_dist(start, p) for p in path])


def main():
    assert solve("ne,ne,ne")[0] == 3
    assert solve("ne,ne,sw,sw")[0] == 0
    assert solve("ne,ne,s,s")[0] == 2
    assert solve("se,sw,se,sw,sw")[0] == 3

    r = solve(io.get_input("input.txt"))
    print(r[0])
    print(r[1])


if __name__ == "__main__":
    sys.exit(main())
