import AoC


class Main(AoC.Solution):
    def part_one(self, input):
        return input.count("(") - input.count(")")

    def part_two(self, input):
        floor = 0
        for i in range(len(input)):
            if "(" == input[i]:
                floor = floor + 1
            if ")" == input[i]:
                floor = floor - 1
            if -1 == floor:
                return i + 1
