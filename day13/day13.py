#!/usr/bin/env python3

import os
import sys
from copy import deepcopy

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def get_layers(lines):
    max = int(lines[-1].split(": ")[0])
    layers = [0] * (max + 1)

    for line in lines:
        parts = line.split(": ")
        layers[int(parts[0])] = int(parts[1])

    return layers


def is_caught(layers, pos, time):
    # "unfold" layer
    offset = time % ((layers[pos] - 1) * 2)
    # where in the layer are we?
    return 2 * (layers[pos] - 1) - offset if offset > layers[pos] - 1 else offset


def part1(filename):
    layers = get_layers(io.get_lines(filename))
    caught = [
        pos * layers[pos] if is_caught(layers, pos, pos) == 0 else 0
        for pos in range(len(layers))
    ]

    return sum(caught)


def part2(filename):
    layers = get_layers(io.get_lines(filename))

    d = 1
    while True:
        done = True
        for pos in range(len(layers)):
            if is_caught(layers, pos, pos + d) == 0:
                done = False
                break

        if done:
            return d

        d += 1

    raise "should not reach"


def main():
    assert part1("example.txt") == 24
    print(part1("input.txt"))

    assert part2("example.txt") == 10
    print(part2("input.txt"))


if __name__ == "__main__":
    sys.exit(main())
