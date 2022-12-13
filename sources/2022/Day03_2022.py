import AoC


class Main(AoC.Solution):
    def priority(c):
        return ord(c) - ord("a") + 1 if c >= "a" else ord(c) - ord("A") + 27

    def part_one(self, input):
        return sum(
            Main.priority(
                next(iter(set(s[: len(s) // 2]).intersection(set(s[len(s) // 2 :]))))
            )
            for s in input
        )

    def part_two(self, input):
        return sum(
            Main.priority(
                next(iter(set(r[0]).intersection(set(r[1])).intersection(set(r[2]))))
            )
            for r in [input[i : i + 3] for i in range(0, len(input), 3)]
        )
