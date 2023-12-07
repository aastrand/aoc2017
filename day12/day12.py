#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io
from utils.graph import bfs


def build_graph(lines):
    graph = {}
    for line in lines:
        parts = line.split(" <-> ")
        graph[int(parts[0])] = [int(n) for n in parts[1].split(", ")]

    return graph


def part1(filename):
    return len(bfs(0, build_graph(io.get_lines(filename))))


def part2(filename):
    graph = build_graph(io.get_lines(filename))

    nodes = set([n for n in graph.keys()])
    groups = set()
    while len(nodes) > 0:
        n = nodes.pop()
        v = bfs(n, graph)
        groups.add(tuple(sorted(list(v))))
        for n in v:
            try:
                nodes.remove(n)
            except KeyError:
                pass

    return len(groups)


def main():
    assert part1("example.txt") == 6
    print(part1("../input/2017/day12.txt"))

    assert part2("example.txt") == 2
    print(part2("../input/2017/day12.txt"))


if __name__ == "__main__":
    sys.exit(main())
