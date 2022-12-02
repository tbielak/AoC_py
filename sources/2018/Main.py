import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)  # to access AoC module (one dir up)

import AoC
import Day01_2018
import Day02_2018
import Day03_2018

names = {
    1: "--- Day 1: Chronal Calibration ---",
    2: "--- Day 2: Inventory Management System ---",
    3: "--- Day 3: No Matter How You Slice It ---",
}

repo = {
    1: (2, [("", Day01_2018.Main())]),
    2: (2, [("", Day02_2018.Main())]),
    3: (2, [("", Day03_2018.Main())]),
}

AoC.Engine(2018, names, repo).run(sys.argv)
