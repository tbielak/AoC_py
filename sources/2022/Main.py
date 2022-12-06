import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)  # to access AoC module (one dir up)

import AoC
import Day01_2022
import Day02_2022
import Day03_2022

names = {
    1: "--- Day 1: Calorie Counting ---",
    2: "--- Day 2: Rock Paper Scissors ---",
    3: "--- Day 3: Rucksack Reorganization ---",
}

repo = {
    1: (2, [("", Day01_2022.Main())]),
    2: (2, [("", Day02_2022.Main())]),
    3: (2, [("", Day03_2022.Main())]),
}

AoC.Engine(2022, names, repo).run(sys.argv)
