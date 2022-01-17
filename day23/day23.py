#!/usr/bin/env python3

import os
import sys

import sympy

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


class CPU:
    def __init__(self):
        self.regs = {}
        self.pc = 0
        self.mul_count = 0

    def _value(self, v):
        try:
            v = int(v)
        except ValueError:
            pass

        return v if isinstance(v, int) else self.regs.get(v, 0)

    def set(self, x, y):
        self.regs[x] = self._value(y)
        self.pc += 1

    def sub(self, x, y):
        self.regs[x] = self.regs.get(x, 0) - self._value(y)
        self.pc += 1

    def mul(self, x, y):
        self.regs[x] = self.regs.get(x, 0) * self._value(y)
        self.pc += 1
        self.mul_count += 1

    def jnz(self, x, y):
        if self._value(x) != 0:
            self.pc += self._value(y)
        else:
            self.pc += 1


def decode(line):
    parts = line.split(" ")
    instr = parts[0]
    x = parts[1]
    y = 0
    if len(parts) > 2:
        y = parts[2]

    return (instr, x, y)


def part1(filename):
    lines = io.get_lines(filename)
    cpu = CPU()

    while True:
        if cpu.pc > len(lines) - 1:
            break

        instr, x, y = decode(lines[cpu.pc])
        r = getattr(cpu, instr)(x, y)

    return cpu.mul_count


def part2(filename):
    h = 0
    b = 108400
    c = 125400

    for i in range(b, c + 17, 17):
        if not sympy.isprime(i):
            h += 1

    return h


def main():
    print(part1("input.txt"))
    print(part2("input.txt"))


if __name__ == "__main__":
    sys.exit(main())
