#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


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


def part1(max, lengths):
    input = [i for i in range(max + 1)]
    lengths = [int(l) for l in lengths.split(",")]

    hash = knot(input, lengths)

    return hash[0] * hash[1]


def part2(max, lengths):
    input = [i for i in range(max + 1)]
    # convert to ascii
    lengths = [ord(c) for c in lengths]
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


def main():
    assert part1(4, "3,4,1,5") == 12

    print(part1(255, io.get_input("../input/2017/day10.txt")))

    assert part2(255, "") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert part2(255, "AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert part2(255, "1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert part2(255, "1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

    print(part2(255, io.get_input("../input/2017/day10.txt")))


if __name__ == "__main__":
    sys.exit(main())
