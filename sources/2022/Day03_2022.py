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
        sum = 0
        i = 0
        while i < len(input):
            contents = {}
            for j in range(3):
                for c in input[i]:
                    contents[c] = contents.get(c, 0) | (1 << j)
                i = i + 1
            for c, v in contents.items():
                if v == 7:
                    sum += Main.priority(c)
        return sum
