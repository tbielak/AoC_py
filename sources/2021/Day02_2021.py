import AoC


class Main(AoC.Solution):
    def load(input):
        course = []
        for line in input:
            s = line.split(" ")
            course.append((s[0][0], int(s[1])))
        return course

    def part_one(self, input):
        course = Main.load(input)
        position = depth = 0
        for (command, units) in course:
            if command == "d":
                depth += units
            elif command == "u":
                depth -= units
            else:
                position += units
        return position * depth

    def part_two(self, input):
        course = Main.load(input)
        position = depth = aim = 0
        for (command, units) in course:
            if command == "d":
                aim += units
            elif command == "u":
                aim -= units
            else:
                position += units
                depth += aim * units
        return position * depth
