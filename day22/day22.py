#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io

DIRECTIONS = [
    (0, -1),  # up
    (-1, 0),  # left
    (0, 1),  # down
    (1, 0),  # right
]


def get_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid[(x, y)] = char

    return grid


def part1(filename, bursts):
    lines = io.get_lines(filename)
    grid = get_grid(lines)

    pos = (len(lines[0]) // 2, len(lines) // 2)
    facing = 0

    sum = 0
    for _ in range(bursts):
        if grid.get(pos) == "#":
            facing = (facing - 1) % len(DIRECTIONS)
            grid[pos] = "."
        else:
            facing = (facing + 1) % len(DIRECTIONS)
            grid[pos] = "#"
            sum += 1

        pos = (pos[0] + DIRECTIONS[facing][0], pos[1] + DIRECTIONS[facing][1])

    return sum


def part2(filename, bursts):
    lines = io.get_lines(filename)
    grid = get_grid(lines)

    pos = (len(lines[0]) // 2, len(lines) // 2)
    facing = 0

    sum = 0
    for _ in range(bursts):
        if pos not in grid or grid.get(pos) == ".":
            facing = (facing + 1) % len(DIRECTIONS)
            grid[pos] = "W"
        elif grid.get(pos) == "W":
            grid[pos] = "#"
            sum += 1
        elif grid.get(pos) == "#":
            facing = (facing - 1) % len(DIRECTIONS)
            grid[pos] = "F"
        elif grid.get(pos) == "F":
            facing = (facing - 2) % len(DIRECTIONS)
            grid[pos] = "."
        else:
            raise "not supposed to happen"

        pos = (pos[0] + DIRECTIONS[facing][0], pos[1] + DIRECTIONS[facing][1])

    return sum


def main():
    assert part1("example.txt", 10000) == 5587
    print(part1("input.txt", 10000))

    assert part2("example.txt", 100) == 26
    assert part2("example.txt", 10000000) == 2511944
    print(part2("input.txt", 10000000))


if __name__ == "__main__":
    sys.exit(main())
