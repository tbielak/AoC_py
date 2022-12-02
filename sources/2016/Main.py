import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)  # to access AoC module (one dir up)

import AoC
import Day01_2016
import Day02_2016
import Day03_2016

names = {
    1: "--- Day 1: No Time for a Taxicab ---",
    2: "--- Day 2: Bathroom Security ---",
    3: "--- Day 3: Squares With Three Sides ---",
}

repo = {
    1: (2, [("", Day01_2016.Main())]),
    2: (2, [("", Day02_2016.Main())]),
    3: (2, [("", Day03_2016.Main())]),
}

AoC.Engine(2016, names, repo).run(sys.argv)
