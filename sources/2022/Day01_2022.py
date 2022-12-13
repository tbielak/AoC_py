import AoC


class Main(AoC.Solution):
    def total_calories(input, top_count=1):
        return sum(
            sorted(
                [
                    sum([int(v) for v in x.split(":")])
                    for x in ":".join(input).split("::")
                ]
            )[-top_count:]
        )

    def part_one(self, input):
        return Main.total_calories(input)

    def part_two(self, input):
        return Main.total_calories(input, 3)
