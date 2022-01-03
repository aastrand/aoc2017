#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def solve(filename, part2=False):
    banks = [int(v) for v in io.get_lines(filename)[0].split("\t")]

    seen = set()
    steps = 0
    steps2 = 0
    first = None

    while True:
        steps += 1

        max = 0
        chosen = -1
        for i, v in enumerate(banks):
            if v > max:
                max = v
                chosen = i

        val = banks[chosen]
        banks[chosen] = 0
        chosen += 1

        for i in range(0, val):
            banks[chosen % len(banks)] += 1
            chosen += 1

        key = ",".join([str(v) for v in banks])
        if key in seen:
            if part2:
                if not first:
                    first = key
                elif key == first:
                    break

                steps2 += 1
            else:
                break

        seen.add(key)

    return steps, steps2


def main():
    assert solve("example.txt")[0] == 5
    print(solve("input.txt")[0])

    assert solve("example.txt", True)[1] == 4
    print(solve("input.txt", True)[1])


if __name__ == "__main__":
    sys.exit(main())
