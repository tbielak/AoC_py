# AoC Engine
# This file is shared by all projects: 2015, 2016, ...

import sys
from os import cpu_count
from time import perf_counter

# if missing -> run "pip install colorama" from command line
import colorama


# script arguments


class Options:
    def __init__(self, argv):
        self.colors = True
        self.help = False
        self.available = False
        self.speed = 0
        self.day = -1
        self.solution = -1
        self.input_filename = ""

        for i in range(1, len(argv)):
            x = argv[i]

            if x == "-c":
                self.colors = False

            if x == "-h":
                self.help = True

            if x == "-a":
                self.available = True

            if x == "-s":
                self.speed = 10
                if len(argv) > i + 1:
                    i = i + 1
                    if argv[i].isnumeric():
                        self.speed = int(argv[i])
                    else:
                        i = i - 1

            if x == "-p" and len(argv) > i + 1:
                i = i + 1
                subs = argv[i].split(":")
                if subs[0].isnumeric():
                    self.day = int(subs[0])
                if len(subs) > 1 and subs[1].isnumeric():
                    self.solution = int(subs[1]) - 1

            if x == "-i" and len(argv) > i + 1:
                i = i + 1
                self.input_filename = argv[i]


# solution base class


class Solution:
    def both_parts(self, input):
        pass

    def part_one(self, input):
        pass

    def part_two(self, input):
        pass

    def run(self, input):
        output = []
        exec_times = []

        t0 = perf_counter()
        bp = self.both_parts(input) if len(input) > 1 else self.both_parts(input[0])
        t1 = perf_counter()
        if not bp is None:
            if isinstance(bp, list):
                output.extend(bp)
            else:
                output.append(bp)
            exec_times.append((t1 - t0) * 1000)
            return (output, exec_times)

        t0 = perf_counter()
        p1 = self.part_one(input) if len(input) > 1 else self.part_one(input[0])
        t1 = perf_counter()
        if isinstance(p1, list):
            output.extend(p1)
        else:
            output.append(p1)
        exec_times.append((t1 - t0) * 1000)

        t0 = perf_counter()
        p2 = self.part_two(input) if len(input) > 1 else self.part_two(input[0])
        t1 = perf_counter()
        if not p2 is None:
            if isinstance(p2, list):
                output.extend(p2)
            else:
                output.append(p2)
            exec_times.append((t1 - t0) * 1000)

        return (output, exec_times)


# colorful console: works when script is run with <Ctrl+F5> under MS Visual Studio


class Console:
    def write_line(self, s=""):
        colors = ["{d}", "{y}", "{w}", "{g}", "{r}"]
        escapes = ["\x1B[0m", "\x1B[93m", "\x1B[97m", "\x1B[92m", "\x1B[91m"]

        s = str(s)
        for i in range(len(colors)):
            while True:
                position = s.find(colors[i])
                if position == -1:
                    break
                esc = escapes[i] if self.colors_enabled else ""
                s = s[:position] + esc + s[position + len(colors[i]) :]
        print(s)

    def setup(self, colors_enabled):
        self.colors_enabled = colors_enabled
        if colors_enabled:
            colorama.init()


# execution engine


class Engine:
    def __init__(self, year, names, repo):
        self.year = year
        self.names = names
        self.repo = repo
        self.cc = Console()

    def intro(self):
        self.cc.write_line(
            "{w}AdventOfCode.py: "
            + str(self.year)
            + " Puzzle Solutions{d}, copyright(c) 2022 by {y}TomB{d}"
        )

    def help(self):
        self.cc.write_line("{y}Available options:{d}")
        self.cc.write_line("{g}-h{d} : help (you are exploring it right now)")
        self.cc.write_line(
            "{g}-c{d} : disable colorful output (useful when streaming to file)"
        )
        self.cc.write_line("{g}-a{d} : show available solutions")
        self.cc.write_line(
            "{g}-p <day>{d} : run solution(s) of selected <day> only (by default all available puzzle solutions are executed)"
        )
        self.cc.write_line(
            "{g}-p <day>:<n>{d} : run n-th solution of puzzle from day <day> (if it is not available, first one is executed)"
        )
        self.cc.write_line(
            "{g}-i <filename>{d} : run with <filename> as input (if not specified inputs are loaded from 'input' directory)"
        )
        self.cc.write_line(
            "{g}-s <x>{d} : execution speed testing (at least 10 times, at least <x> seconds to measure reliable execution time)"
        )
        self.cc.write_line()
        self.cc.write_line(
            "{y}Warning:{d} Not all combinations of options are supported. See valid ones in examples below:"
        )
        self.cc.write_line(
            "{g}<no options provided>{d} => run everything once, using as input the appropriate files read from 'input' directory"
        )
        self.cc.write_line("{g}-a{d} => show available solutions")
        self.cc.write_line("{g}-p 2{d} => run only the solution(s) of 2nd day puzzle")
        self.cc.write_line("{g}-p 4:2{d} => run 2nd solution of 4th day puzzle")
        self.cc.write_line(
            "{g}-p 5 -i my_input.txt{d} => run 5th day puzzle solution with the input read from my_input.txt file"
        )
        self.cc.write_line(
            "{g}-s 10{d} => execution speed testing of all puzzles, at least 10 times for 10 seconds (it may take a while!)"
        )
        self.cc.write_line(
            "{g}-p 7 -s 5{d} => execution speed testing 7th puzzle solution(s), at least 10 times for 5 seconds"
        )
        self.cc.write_line()
        self.cc.write_line("Enjoy!")

    def available_solutions(self):
        self.cc.write_line("{y}Solutions matrix:{d}")
        self.cc.write_line("{g}         1111111111222222{d}")
        self.cc.write_line("{g}1234567890123456789012345{d}  <== day")
        solved = ""
        solutions = ""
        for i in range(1, 26):
            solved = solved + str(self.repo.get(i, "-")[0])
            solutions = (
                solutions + str(len(self.repo.get(i)[1]))
                if i in self.repo
                else solutions + "-"
            )
        self.cc.write_line(solved + "  <== parts solved")
        self.cc.write_line(solutions + "  <== number of solutions available")

    def load_input(self, input_filename, day):
        filename = (
            input_filename
            if input_filename != ""
            else "input/{0}_{1}.txt".format(self.year, str(day).zfill(2))
        )
        try:
            x = open(filename).read().split("\n")
            if x[-1] == "":
                x.pop()
            return x
        except IOError:
            self.cc.write_line("{r}ERROR: Cannot load input file!{d}")
            return []

    def print_output(self, output, count=0):
        (results, exec_times) = output
        for s in results:
            self.cc.write_line(s)
        s = "Execution time = {y}" if count == 0 else "Average execution time = {y}"
        s = s + "{:.5f}".format(sum(exec_times)) + " ms{d}"
        if len(exec_times) > 1:
            s += " ("
            for i in range(len(exec_times)):
                s = s + "{y}" + "{:.5f}".format(exec_times[i]) + " ms{d}"
                if i < len(exec_times) - 1:
                    s = s + " / "
            s = s + ")"
        if count > 0:
            s = s + " (results of " + str(count) + " executions)"
        self.cc.write_line(s)

    def execute(self, print_info, input_filename, day, solution):
        if not day in self.repo:
            if print_info:
                self.cc.write_line(
                    "{r}ERROR: Day " + str(day) + " solution(s) are not available.{d}"
                )
                return (False, [])

        one_day = self.repo[day][1]
        if solution >= len(one_day):
            if print_info:
                self.cc.write_line("{r}ERROR: Requested solution is not available.{d}")
                return (False, [])

        if print_info:
            self.cc.write_line("{g}" + self.names[day] + "{d}")

        (description, sol) = one_day[solution]
        if description != "":
            s = ": " + description
            if s.find("{T}") > -1:
                s = s.replace("{T}", ", " + str(cpu_count()) + " concurrent threads")
            if print_info:
                if len(one_day) > 1:
                    self.cc.write_line(
                        "{g}--- Solution #" + str(solution + 1) + s + "{d}"
                    )
                else:
                    self.cc.write_line("{g}--- " + s[2:] + "{d}")

        input = self.load_input(input_filename, day)
        if len(input) == 0:
            return (False, [])

        return (True, sol.run(input))

    def execute_solution(self, speed, input_filename, day, solution):
        if speed > 0:
            count = 0
            ok = True
            first = True
            exec_times = []
            t0 = perf_counter()
            while True:
                count += 1
                output = self.execute(first, input_filename, day, solution)
                if not output[0]:
                    ok = False
                    break
                if first:
                    first = False
                    ref_output = output[1][0]
                    for j in range(len(output[1][1])):
                        exec_times.append([])
                else:
                    if ref_output != output[1][0]:
                        self.cc.write_line(
                            "{r}ERROR: Different results obtained in successive executions{d}"
                        )
                        ok = False
                        break
                for j in range(len(output[1][1])):
                    exec_times[j].append(output[1][1][j])
                t1 = perf_counter()
                time_elapsed = t1 - t0
                if time_elapsed >= speed and count >= 10:
                    min_i = count // 10
                    max_i = count - min_i
                    for j in range(len(exec_times)):
                        exec_times[j].sort()
                        c = 0
                        output[1][1][j] = 0
                        for i in range(min_i, max_i):
                            output[1][1][j] += exec_times[j][i]
                            c += 1
                        output[1][1][j] /= c
                    break
            if ok:
                self.print_output(output[1], count)
            else:
                self.cc.write_line("{r}ERROR: Unable to run speed test{d}")
        else:
            output = self.execute(True, input_filename, day, solution)
            if output[0]:
                self.print_output(output[1])

    def execute_day(self, speed, input_filename, day):
        if not day in self.repo:
            self.cc.write_line(
                "{r}ERROR: Day " + str(day) + " solution(s) are not available.{d}"
            )
            return

        one_day = self.repo[day][1]
        for sol in range(len(one_day)):
            self.execute_solution(speed, input_filename, day, sol)

    def execute_all(self, speed):
        for (day, one_day) in self.repo.items():
            for sol in range(len(one_day[1])):
                self.execute_solution(speed, "", day, sol)

    def run(self, argv):
        opt = Options(argv)
        self.cc.setup(opt.colors)
        self.intro()

        if opt.help:
            self.help()
            return

        if opt.available:
            self.available_solutions()
            return

        if opt.speed > 0:
            repetitions = [
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
                "ten",
            ]
            s = str(opt.speed) if opt.speed > 10 else repetitions[opt.speed - 1]
            s = s + " second"
            if opt.speed > 1:
                s = s + "s"
            self.cc.write_line(
                "{y}Warning:{d} In this mode ({g}-s{d}) each puzzle solution is run at least ten times and at least for "
                + s
                + "."
            )
            self.cc.write_line(
                "It may take some time to obtain all results, please be patient. 10% of the highest and the lowest time measurements"
            )
            self.cc.write_line(
                "are dropped, the average time of all remaining is printed. Repeatability of results is checked after each execution."
            )

        if opt.day > -1:
            if opt.solution > -1:
                self.execute_solution(
                    opt.speed, opt.input_filename, opt.day, opt.solution
                )
            else:
                self.execute_day(opt.speed, opt.input_filename, opt.day)
        else:
            self.execute_all(opt.speed)
