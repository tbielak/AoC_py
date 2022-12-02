## Projects

Directory | Contents
------------ | -------------
[2015](2015) | Year 2015 puzzle solutions.
[2016](2016) | Year 2016 puzzle solutions.
[2017](2017) | Year 2017 puzzle solutions.
[2018](2018) | Year 2018 puzzle solutions.
[2019](2019) | Year 2019 puzzle solutions.
[2020](2020) | Year 2020 puzzle solutions.
[2021](2021) | Year 2021 puzzle solutions.


## Special files

File | Contents
------------ | -------------
[AoC.py](AoC.py) | Execution environment for the puzzles. It is used in all projects mentioned above. See below to explore solutions running.
[AoC.sln](AoC.sln) | Solution file for Microsoft Visual Studio Community 2022.
[clean.bat](clean.bat) | Batch file used to remove all temporary files generated during work session with Microsoft Visual Studio.


## Running projects

- download the repository
- install *colorama* module if missing (run `pip install colorama` from command line)
- open *AoC.sln* solution file in Microsoft Visual Studio Community 2022
- set an appropriate project as *Startup Project*
- choose solution configuration (*Debug*/*Release*) and... just run it!


## Script arguments

By default all solutions available in selected year are executed. You may also provide script arguments to control the execution:

Script Argument | Description
----------------| -----------
`-h` | Show help = show all available script arguments.
`-a` | Show available solutions.
`-p <day>` | Run solution(s) of selected day only, e.g. `-p 2` runs solution(s) of day two.
`-p <day>:<n>` | Run n-th solution of puzzle from selected day, e.g. `-p 18:2` runs 2nd puzzle solution of day 18.
`-i <filename>` | Run with your input file (file should be copied into *Input* directory), e.g. `-p 2 -i my_2021_02_input.txt`
`-s <x>` | Measure execution time of the solution(s). In this mode each puzzle solution is run at least ten times and at least for specified seconds (ten seconds, if *x* is not provided). It may take some time to obtain all results, so please be patient. 10% of the highest and 10% of the lowest time measurements are dropped, the average time of all remaining executions is printed. Repeatability of results is checked after each execution. These consistency checks and preparing input data for subsequent code executions are outside the measurement scope, thus the execution may last longer than expected. Time of execution does not include input file loading, but includes processing input data (from array of strings to any other structure needed by solution). Example: `-p 2 -s 15` runs 2nd day solution(s) for 15 seconds for precise execution time measurement.
`-c` | Disable colored text in output. Colored output is emited with use of `colorama` module, and it is enabled only in *Release* configuration. Selecting the colors is achieved by emitting escape sequences. This feature in supported by *cmd.exe* and *conhost.exe* console processes starting from Windows 10 TH2 v1511. If you see garbage instead of colors, disable coloring.


## Debugging the solution

Use Microsoft Visual Studio Community 2022 in Windows to debug the solution. Choose *Debug* configuration, and choose the puzzle solution providing *Script Arguments* (*-p* switch) + optionally: your input file (*-i* switch). Place the breakpoint in the appropriate *py* file, e.g. in *part_one* method of *Main* class and run it. Enjoy!


## Cleaning the folder

Run *clean.bat* script to remove any temporary files generated during work session with Microsoft Visual Studio.
