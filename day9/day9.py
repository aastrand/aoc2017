#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def solve(string):
    stack = []
    garbage = False
    ignore = False
    score = 0
    total_garbage = 0

    for i in range(len(string)):
        c = string[i]

        if garbage and not ignore and c != "!" and c != ">":
            total_garbage += 1

        if ignore:
            ignore = False
        elif c == "!":
            ignore = True
        elif c == "<":
            garbage = True
        elif garbage:
            if c == ">":
                garbage = False
        elif c == "{":
            stack.append("{")
            score += len(stack)
        elif c == "}":
            stack.pop()

    return score, total_garbage


def main():
    assert solve("{}")[0] == 1
    assert solve("{{{}}}")[0] == 6
    assert solve("{{},{}}")[0] == 5
    assert solve("{{{},{},{{}}}}")[0] == 16
    assert solve("{<a>,<a>,<a>,<a>}")[0] == 1
    assert solve("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9
    assert solve("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0] == 9
    assert solve("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3

    assert solve("<>")[1] == 0
    assert solve("<random characters>")[1] == 17
    assert solve("<<<<>")[1] == 3
    assert solve("<{!>}>")[1] == 2
    assert solve("<!!>")[1] == 0
    assert solve("<!!!>")[1] == 0
    assert solve('<{o"i!a,<{i<a>')[1] == 10

    r = solve(io.get_input("input.txt"))
    print(r[0])
    print(r[1])


if __name__ == "__main__":
    sys.exit(main())
