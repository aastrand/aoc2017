#!/bin/bash

mkdir day$1
cp -R template.py "day${1}/day${1}.py"

# Download input
# Put this in .cookie.txt
#  # Netscape HTTP Cookie File
#  .adventofcode.com	TRUE	/	FALSE	0	session	<token-copied-from-browser-devtools>
curl -o day$1/input.txt --cookie .cookie.txt https://adventofcode.com/2017/day/$1/input
