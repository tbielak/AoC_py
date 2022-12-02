import AoC


class Main(AoC.Solution):
    def part_one(self, input):
        x = [int(s) for s in input]
        for a in x:
            for b in x:
                if 2020 == a + b:
                    return a * b

    def part_two(self, input):
        x = [int(s) for s in input]
        for a in x:
            for b in x:
                for c in x:
                    if 2020 == a + b + c:
                        return a * b * c
