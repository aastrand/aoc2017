#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io
from utils.hex import *


def walk(input):
    pos = (0, 0, 0)
    steps = [pos]
    for step in input.split(","):
        pos = (
            pos[0] + HEX_OFFSETS[step][0],
            pos[1] + HEX_OFFSETS[step][1],
            pos[2] + HEX_OFFSETS[step][2],
        )
        steps.append(pos)

    return pos, steps


def solve(input):
    start = (0, 0, 0)
    pos, path = walk(input)

    return hex_cube_dist(start, pos), max([hex_cube_dist(start, p) for p in path])


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
