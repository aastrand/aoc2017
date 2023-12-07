#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io
from utils.parse import ints


def dist(p):
    return abs(p[1][0]) + abs(p[1][1]) + abs(p[1][2])


def get_particles(lines):
    particles = []
    for i, line in enumerate(lines):
        parts = line.split(", ")
        particles.append([i, ints(parts[0]), ints(parts[1]), ints(parts[2])])

    return particles


def update(p):
    p[2][0] += p[3][0]
    p[2][1] += p[3][1]
    p[2][2] += p[3][2]
    p[1][0] += p[2][0]
    p[1][1] += p[2][1]
    p[1][2] += p[2][2]


def part1(filename):
    particles = get_particles(io.get_lines(filename))

    for i in range(500):
        for p in particles:
            update(p)

    min = None
    minp = None
    for p in particles:
        d = dist(p)
        if min is None or min > d:
            min = d
            minp = p

    return minp[0]


def part2(filename):
    particles = get_particles(io.get_lines(filename))

    for _ in range(500):
        seen = {}
        removes = set()
        for i, p in enumerate(particles):
            p[0] = i

            if tuple(p[1]) in seen:
                removes.add(seen[tuple(p[1])])
                removes.add(p[0])
            else:
                seen[tuple(p[1])] = p[0]

            update(p)

        removes = list(removes)
        removes.sort(reverse=True)

        for r in removes:
            del particles[r]

    return len(particles)


def main():
    print(part1("../input/2017/day20.txt"))
    print(part2("../input/2017/day20.txt"))


if __name__ == "__main__":
    sys.exit(main())
