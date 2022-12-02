import AoC


class Main(AoC.Solution):
    def part_one(self, input):
        return sum(int(x) for x in input)

    def part_two(self, input):
        freq = 0
        known = set()
        while True:
            for line in input:
                freq += int(line)
                if freq in known:
                    return freq
                known.add(freq)
