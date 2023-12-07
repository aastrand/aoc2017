#!/usr/bin/env python3

import os
import sys

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def translate_to_np(s):
    return np.array([[1 if c == "#" else 0 for c in l] for l in s.split("/")])


def iterate2(grid, rules):
    size = len(grid)
    by = 2 if size % 2 == 0 else 3
    new_size = size * (by + 1) // by
    new_grid = np.empty((new_size, new_size), dtype=int)
    squares = [i for i in range(0, size, by)]
    new_squares = [i for i in range(0, new_size, by + 1)]

    for y in range(len(squares)):
        for x in range(len(squares)):
            i = squares[y]
            ni = new_squares[y]
            j = squares[x]
            nj = new_squares[x]
            square = grid[i : i + by, j : j + by]
            new_grid[ni : ni + by + 1, nj : nj + by + 1] = rules[square.tobytes()]

    return new_grid


def solve(filename, iterations):
    lines = io.get_lines(filename)
    rules = {}
    grid = translate_to_np(".#./..#/###")

    for line in lines:
        k, v = map(translate_to_np, line.strip().split(" => "))
        for a in (k, np.fliplr(k)):
            for r in range(4):
                rules[np.rot90(a, r).tobytes()] = v

    for _ in range(iterations):
        grid = iterate2(grid, rules)

    return grid.sum()


def main():
    assert solve("example.txt", 2) == 12
    print(solve("../input/2017/day21.txt", 5))
    print(solve("../input/2017/day21.txt", 18))


if __name__ == "__main__":
    sys.exit(main())
