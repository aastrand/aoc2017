#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io

CMP = {
    "<": lambda a, b: a < b,
    ">": lambda a, b: a > b,
    "<=": lambda a, b: a <= b,
    ">=": lambda a, b: a >= b,
    "!=": lambda a, b: a != b,
    "==": lambda a, b: a == b,
}


def solve(filename):
    lines = io.get_lines(filename)

    regs = {}
    max_during = 0
    for line in lines:
        parts = line.split(" ")
        reg = parts[0]
        op = parts[1]
        value = int(parts[2])
        operand = parts[4]
        cmp = parts[5]
        direct = int(parts[6])

        if CMP[cmp](regs.get(operand, 0), direct):
            regs[reg] = regs.get(reg, 0) + value * (1 if op == "inc" else -1)
            if regs[reg] > max_during:
                max_during = regs[reg]

    max = 0
    for key in regs:
        if regs[key] > max:
            max = regs[key]

    return max, max_during


def main():
    r = solve("example.txt")
    assert r[0] == 1
    assert r[1] == 10

    r = solve("../input/2017/day8.txt")
    print(r[0])
    print(r[1])


if __name__ == "__main__":
    sys.exit(main())
