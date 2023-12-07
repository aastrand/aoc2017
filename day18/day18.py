#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


class CPU:
    def __init__(self, outp, inp, part2=False):
        self.regs = {}
        self.pc = 0
        self.outp = outp
        self.inp = inp
        self.snd_count = 0
        self.part2 = part2

    def _value(self, v):
        try:
            v = int(v)
        except ValueError:
            pass

        return v if isinstance(v, int) else self.regs.get(v, 0)

    def snd(self, x, *args):
        self.outp.append(self._value(x))
        self.snd_count += 1
        self.pc += 1

    def set(self, x, y):
        self.regs[x] = self._value(y)
        self.pc += 1

    def add(self, x, y):
        self.regs[x] = self.regs.get(x, 0) + self._value(y)
        self.pc += 1

    def mul(self, x, y):
        self.regs[x] = self.regs.get(x, 0) * self._value(y)
        self.pc += 1

    def mod(self, x, y):
        self.regs[x] = self.regs.get(x, 0) % self._value(y)
        self.pc += 1

    def rcv(self, x, *args):
        if self.part2 or self._value(x) != 0:
            if len(self.inp) > 0:
                self.pc += 1
                self.regs[x] = self.inp.pop(0)
                return self.regs[x]

            return None
        else:
            self.pc += 1
            return None

    def jgz(self, x, y):
        if self._value(x) > 0:
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
    pipe = []
    cpu = CPU(pipe, pipe)

    while True:
        instr, x, y = decode(lines[cpu.pc])
        r = getattr(cpu, instr)(x, y)
        if instr == "rcv" and r is not None:
            return r


def part2(filename):
    lines = io.get_lines(filename)

    out1 = []
    out2 = []

    cpu1 = CPU(out1, out2, True)
    cpu1.regs["p"] = 0

    cpu2 = CPU(out2, out1, True)
    cpu2.regs["p"] = 1

    while True:
        instr, x, y = decode(lines[cpu1.pc])
        r = getattr(cpu1, instr)(x, y)

        instr, x, y = decode(lines[cpu2.pc])
        r = getattr(cpu2, instr)(x, y)

        if (
            len(cpu1.inp) == 0
            and decode(lines[cpu1.pc])[0] == "rcv"
            and len(cpu2.inp) == 0
            and decode(lines[cpu2.pc])[0] == "rcv"
        ):
            break

    return cpu2.snd_count


def main():
    assert part1("example.txt") == 4
    print(part1("../input/2017/day18.txt"))

    assert part2("example2.txt") == 3
    print(part2("../input/2017/day18.txt"))


if __name__ == "__main__":
    sys.exit(main())
