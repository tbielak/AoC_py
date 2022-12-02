import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)  # to access AoC module (one dir up)

import AoC
import Day01_2020
import Day02_2020
import Day03_2020

names = {
    1: "--- Day 1: Report Repair ---",
    2: "--- Day 2: Password Philosophy ---",
    3: "--- Day 3: Toboggan Trajectory ---",
}

repo = {
    1: (2, [("", Day01_2020.Main())]),
    2: (2, [("", Day02_2020.Main())]),
    3: (2, [("", Day03_2020.Main())]),
}

AoC.Engine(2020, names, repo).run(sys.argv)
