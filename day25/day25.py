#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io
from utils.parse import ints


class State:
    def __init__(self, name, zo, zd, zs, oo, od, os):
        self.name = name
        self.zo = zo
        self.zd = zd
        self.zs = zs
        self.oo = oo
        self.od = od
        self.os = os

    def __str__(self):
        return "name: %s, zo: %s, zd: %s, zs: %s, oo: %s, od: %s, os: %s" % (
            self.name,
            self.zo,
            self.zd,
            self.zs,
            self.oo,
            self.od,
            self.os,
        )

    def __repr__(self):
        return self.__str__()


class Machine:
    def __init__(self, start):
        self.cur_state = start
        self.cur = 0
        self.tape = {}
        self.states = {}

    def __str__(self):
        return "cur_state: %s,\n cur: %s,\n tape: %s,\n states: %s" % (
            self.cur_state,
            self.cur,
            self.tape,
            self.states,
        )

    def __repr__(self):
        return self.__str__()


def part1(filename):
    input = io.get_input(filename)
    parts = input.split("\n\n")

    start_state = parts[0].split("\n")[0][-2]
    steps = ints(parts[0].split("\n")[1])[0]

    machine = Machine(start_state)

    for part in parts[1:]:
        sub_parts = part.split("\n")

        name = sub_parts[0][-2]

        # if v == 0
        zo = ints(sub_parts[2])[0]
        zd = -1 if "left" in sub_parts[3] else 1
        zs = sub_parts[4][-2]

        # if v == 1
        oo = ints(sub_parts[6])[0]
        od = -1 if "left" in sub_parts[7] else 1
        os = sub_parts[8][-2]

        machine.states[name] = State(name, zo, zd, zs, oo, od, os)

    for _ in range(steps):
        state = machine.states[machine.cur_state]
        val = machine.tape.get(machine.cur, 0)

        if val == 0:
            machine.tape[machine.cur] = state.zo
            machine.cur += state.zd
            machine.cur_state = state.zs
        elif val == 1:
            machine.tape[machine.cur] = state.oo
            machine.cur += state.od
            machine.cur_state = state.os
        else:
            raise "should not happen"

    return sum([v for v in machine.tape.values()])


def main():
    assert part1("example.txt") == 3
    print(part1("../input/2017/day25.txt"))


if __name__ == "__main__":
    sys.exit(main())
