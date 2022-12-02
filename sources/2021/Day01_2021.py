import AoC


class Main(AoC.Solution):
    def part_one(self, input):
        x = [int(s) for s in input]
        return sum(1 if x[i] > x[i - 1] else 0 for i in range(1, len(x)))

    def part_two(self, input):
        x = [int(s) for s in input]
        return sum(
            1 if x[i] + x[i - 1] + x[i - 2] > x[i - 1] + x[i - 2] + x[i - 3] else 0
            for i in range(1, len(x))
        )
