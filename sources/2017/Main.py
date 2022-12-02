import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)  # to access AoC module (one dir up)

import AoC
import Day01_2017
import Day02_2017
import Day03_2017

names = {
    1: "--- Day 1: Inverse Captcha ---",
    2: "--- Day 2: Corruption Checksum ---",
    3: "--- Day 3: Spiral Memory ---",
}

repo = {
    1: (2, [("", Day01_2017.Main())]),
    2: (2, [("", Day02_2017.Main())]),
    3: (2, [("", Day03_2017.Main())]),
}

AoC.Engine(2017, names, repo).run(sys.argv)
