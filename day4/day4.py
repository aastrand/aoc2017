#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def solve(filename):
    lines = io.get_lines(filename)

    count = len(lines)
    count2 = len(lines)
    for line in lines:
        words = set()
        words2 = set()
        valid = True
        valid2 = True

        for word in line.split(" "):
            if word in words:
                valid = False

            if tuple(sorted(set(word))) in words2:
                valid2 = False

            words.add(word)
            words2.add(tuple(sorted(set(word))))

        if not valid:
            count -= 1

        if not valid2:
            count2 -= 1

    return count, count2


def main():
    assert solve("example.txt")[0] == 2

    res = solve("input.txt")
    print(res[0])
    print(res[1])


if __name__ == "__main__":
    sys.exit(main())
