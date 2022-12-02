import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)  # to access AoC module (one dir up)

import AoC
import Day01_2021
import Day02_2021
import Day03_2021

names = {
    1: "--- Day 1: Sonar Sweep ---",
    2: "--- Day 2: Dive! ---",
    3: "--- Day 3: Binary Diagnostic ---",
}

repo = {
    1: (2, [("", Day01_2021.Main())]),
    2: (2, [("", Day02_2021.Main())]),
    3: (2, [("", Day03_2021.Main())]),
}

AoC.Engine(2021, names, repo).run(sys.argv)
