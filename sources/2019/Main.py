import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)  # to access AoC module (one dir up)

import AoC
import Day01_2019
import Day02_2019
import Day03_2019

names = {
    1: "--- Day 1: The Tyranny of the Rocket Equation ---",
    2: "--- Day 2: 1202 Program Alarm ---",
    3: "--- Day 3: Crossed Wires ---",
}

repo = {
    1: (2, [("", Day01_2019.Main())]),
    2: (2, [("", Day02_2019.Main())]),
    3: (2, [("", Day03_2019.Main())]),
}

AoC.Engine(2019, names, repo).run(sys.argv)
