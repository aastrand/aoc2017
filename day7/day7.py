#!/usr/bin/env python3

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io

WEIGHT_RE = r"[a-z]+ \((\d+)\)"


def parse(lines):
    graph = {}
    weights = {}
    parents = {}
    for line in lines:
        parts = line.split("->")
        node = parts[0].strip().split(" ")[0]

        weight = re.match(WEIGHT_RE, parts[0].strip()).groups()[0]
        weights[node] = int(weight)

        if len(parts) > 1:
            children = parts[1].strip().split(", ")
            graph[node] = children
            for child in children:
                parents[child] = node

    return graph, weights, parents


def find_root(graph):
    notroot = set()
    for key, value in graph.items():
        for v in value:
            notroot.add(v)

    for key in graph:
        if key not in notroot:
            return key

    return None


def find_sum(graph, weights, node):
    sum = weights[node]
    for child in graph.get(node, []):
        sum += find_sum(graph, weights, child)

    return sum


def find_unbalanced(graph, root, sums, weights):
    unbalanced = root
    while graph.get(unbalanced) != None:
        counts = {}
        for child in graph[unbalanced]:
            w = sums.get(child, weights[child])
            c, children = counts.get(w, (0, []))
            children.append(child)
            counts[w] = (c + 1, children)

        next_unbalanced = None
        for _, (count, children) in counts.items():
            if count == 1:
                next_unbalanced = children[0]

        if not next_unbalanced:
            break

        unbalanced = next_unbalanced

    return unbalanced


def solve(filename):
    graph, weights, parents = parse(io.get_lines(filename))

    root = find_root(graph)

    sums = {}
    for key in graph:
        sums[key] = find_sum(graph, weights, key)

    unbalanced = find_unbalanced(graph, root, sums, weights)

    for sibling in graph[parents[unbalanced]]:
        if sibling != unbalanced:
            correct = sums[sibling]
            break
    offset = sums[unbalanced] - correct

    return root, weights[unbalanced] - offset


def main():
    assert solve("example.txt")[0] == "tknk"
    assert solve("example.txt")[1] == 60

    r = solve("input.txt")
    print(r[0])
    print(r[1])


if __name__ == "__main__":
    sys.exit(main())
