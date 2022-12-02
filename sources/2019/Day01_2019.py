import AoC


class Main(AoC.Solution):
    def part_one(self, input):
        return sum(int(v) // 3 - 2 for v in input)

    def full_req(v):
        sum = 0
        while v > 0:
            v = max(v // 3 - 2, 0)
            sum += v
        return sum

    def part_two(self, input):
        return sum(Main.full_req(int(v)) for v in input)
