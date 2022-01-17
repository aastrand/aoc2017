#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from collections import defaultdict

from utils import io


def find(path, graph):
    cur = path[-1][1]
    for b in graph[cur]:
        if not ((cur, b) in path or (b, cur) in path):
            new = path + [(cur, b)]
            yield new
            yield from find(new, graph)


def solve(filename):
    lines = io.get_lines(filename)

    graph = defaultdict(set)
    for line in lines:
        a, b = [int(x) for x in line.split("/")]
        graph[a].add(b)
        graph[b].add(a)

    paths = []
    for path in find([(0, 0)], graph):
        paths.append((len(path), sum(a + b for a, b in path)))

    return (sorted(paths, key=lambda x: x[1])[-1][1], sorted(paths)[-1][1])


def main():
    example = solve("example.txt")
    assert example[0] == 31
    assert example[1] == 19

    r = solve("input.txt")
    print(r[0])
    print(r[1])


if __name__ == "__main__":
    sys.exit(main())
