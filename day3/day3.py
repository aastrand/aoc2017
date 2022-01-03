#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.grid import *


def get_neighbours(grid, pos):
    r = set()

    for o in OFFSETS:
        if grid.get((pos[0] + o[0], pos[1] + o[1])) is not None:
            r.add(o)

    return r


# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ... 26
#                       49
def solve(number):
    grid = {}
    inverse = {}
    sums = {}

    n = 1
    grid[(0, 0)] = n
    inverse[n] = (0, 0)
    sums[(0, 0)] = 1
    n += 1

    grid[(1, 0)] = n
    inverse[n] = (1, 0)
    sums[(1, 0)] = 1
    n += 1

    grid[(1, -1)] = n
    inverse[n] = (1, -1)
    sums[(1, -1)] = 2
    n += 1

    pos = (1, -1)
    part2 = None
    while n < number + 1:
        neighbours = get_neighbours(grid, pos)

        if neighbours == set([BOTTOM_LEFT, BOTTOM]):  # top right, go left
            pos = (pos[0] - 1, pos[1])
        elif neighbours == set([TOP, TOP_RIGHT]):  # bottom left, go right
            pos = (pos[0] + 1, pos[1])
        elif neighbours == set([TOP_LEFT, LEFT]):  # bottom right, go up
            pos = (pos[0], pos[1] - 1)
        elif neighbours == set([RIGHT, BOTTOM_RIGHT]):  # top left, go down
            pos = (pos[0], pos[1] + 1)
        elif neighbours >= set([BOTTOM, BOTTOM_RIGHT, RIGHT]):  # top, go left
            pos = (pos[0] - 1, pos[1])
        elif neighbours >= set([TOP, TOP_RIGHT, RIGHT]):  # left, go down
            pos = (pos[0], pos[1] + 1)
        elif neighbours >= set([LEFT, TOP_LEFT, TOP]):  # bottom, go right
            pos = (pos[0] + 1, pos[1])
        elif neighbours >= set([BOTTOM, BOTTOM_LEFT, LEFT]):  # right, go up
            pos = (pos[0], pos[1] - 1)

        grid[pos] = n
        inverse[n] = pos

        if part2 is None:
            neighbours = get_neighbours(grid, pos)
            sum = 0
            for o in neighbours:
                sum += sums[(pos[0] + o[0], pos[1] + o[1])]

            sums[pos] = sum

            if sum > number:
                part2 = sum

        n += 1

    return (abs(inverse[number][0]) + abs(inverse[number][1]), part2)


def main():

    # Data from square 1 is carried 0 steps, since it's at the access port.
    # Data from square 12 is carried 3 steps, such as: down, left, left.
    # ata from square 23 is carried only 2 steps: up twice.
    # Data from square 1024 must be carried 31 steps.
    assert solve(1)[0] == 0
    assert solve(12)[0] == 3
    assert solve(23)[0] == 2
    assert solve(1024)[0] == 31

    res = solve(325489)
    print(res[0])
    print(res[1])


if __name__ == "__main__":
    sys.exit(main())
