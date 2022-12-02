import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)  # to access AoC module (one dir up)

import AoC
import Day01_2015
import Day02_2015
import Day03_2015

names = {
    1: "--- Day 1: Not Quite Lisp ---",
    2: "--- Day 2: I Was Told There Would Be No Math ---",
    3: "--- Day 3: Perfectly Spherical Houses in a Vacuum ---",
}

repo = {
    1: (2, [("", Day01_2015.Main())]),
    2: (2, [("", Day02_2015.Main())]),
    3: (2, [("", Day03_2015.Main())]),
}

AoC.Engine(2015, names, repo).run(sys.argv)
