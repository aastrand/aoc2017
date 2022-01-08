#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.grid import flood_fill, print_grid


def knot(input, lengths, runs=1):
    cur = 0
    skip = 0
    for r in range(runs):
        for l in lengths:
            from_beg = None
            from_cur = cur + l
            if from_cur > len(input) - 1:
                from_beg = (cur + l) % len(input)
                from_cur = len(input)

            slice = input[cur:from_cur]
            if from_beg:
                slice.extend(input[0:from_beg])

            slice.reverse()

            for i in range(cur, from_cur):
                input[i] = slice[i - cur]

            if from_beg:
                for i in range(0, from_beg):
                    input[i] = slice[i + (from_cur - cur)]

            cur = (cur + l + skip) % len(input)
            skip += 1

    return input


def hash(str):
    input = [i for i in range(255 + 1)]
    # convert to ascii
    lengths = [ord(c) for c in str]
    # add suffix
    lengths.extend([17, 31, 73, 47, 23])

    hash = knot(input, lengths, 64)

    # convert to dense, 16 blocks of 16
    str = []
    for i in range(16):
        base = 0
        for j in range(16):
            base ^= hash[(i * 16) + j]

        digit = hex(base)[2:]
        if len(digit) < 2:
            digit = "0%s" % digit
        str.append(digit)

    return "".join(str)


def get_rows(key):
    rows = []

    for n in range(128):
        row = []
        hashed = hash("%s-%d" % (key, n))
        for d in hashed:
            row.append(bin(int(d, 16))[2:].zfill(4))
        rows.append(row)

    return rows


def part1(rows):
    return sum([d.count("1") for row in rows for d in row])


def part2(rows):
    grid = {}
    y = 0
    for row in rows:
        x = 0
        for d in row:
            for bit in str(d):
                if bit == "1":
                    grid[(x, y)] = "#"
                x += 1

        y += 1

    n = 1
    updated = True
    while updated:
        updated = False
        for key, value in grid.items():
            if value == "#":

                def visitor(g, p):
                    g[p] = n

                flood_fill(grid, key, visitor)
                n += 1
                updated = True
                break

    return n - 1


def main():
    test = get_rows("flqrgnkx")
    input = get_rows("amgozmfv")

    assert part1(test) == 8108
    print(part1(input))

    assert part2(test) == 1242
    print(part2(input))


if __name__ == "__main__":
    sys.exit(main())
