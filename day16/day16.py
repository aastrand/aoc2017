#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def dance(programs, moves):
    for move in moves:
        if move[0] == "s":
            offset = int(move[1:])
            programs = (
                programs[len(programs) - offset :]
                + programs[0 : len(programs) - offset]
            )
        elif move[0] == "x":
            parts = move[1:].split("/")
            programs[int(parts[0])], programs[int(parts[1])] = (
                programs[int(parts[1])],
                programs[int(parts[0])],
            )
        elif move[0] == "p":
            parts = move[1:].split("/")
            pos1 = programs.index(parts[0])
            pos2 = programs.index(parts[1])
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
        else:
            raise "unexpected move: %s" % move

    return programs


def part1(input, max=16):
    programs = [chr(i) for i in range(97, 97 + max)]
    programs = dance(programs, input.split(","))

    return "".join(programs)


def part2(input, max=16):
    programs = [chr(i) for i in range(97, 97 + max)]
    start = "".join(programs)
    moves = input.split(",")
    amount = 1000000000

    cycle = 1
    while True:
        programs = dance(programs, moves)

        if "".join(programs) == start:
            break

        cycle += 1

    programs = [chr(i) for i in range(97, 97 + max)]
    for _ in range(amount % cycle):
        programs = dance(programs, moves)

    return "".join(programs)


def main():

    assert part1("s1,x3/4,pe/b", 5) == "baedc"
    print(part1(io.get_input("../input/2017/day16.txt")))

    assert part2("s1,x3/4,pe/b", 5) == "abcde"
    print(part2(io.get_input("../input/2017/day16.txt")))


if __name__ == "__main__":
    sys.exit(main())
