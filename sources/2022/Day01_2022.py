import AoC


class Main(AoC.Solution):
    def total_calories(input, top_count=1):
        elfs = []
        calories = 0
        for line in input:
            if not line:
                elfs.append(calories)
                calories = 0
            else:
                calories += int(line)
        elfs.append(calories)
        elfs.sort(reverse=True)
        calories = 0
        for i in range(top_count):
            calories += elfs[i]
        return calories

    def part_one(self, input):
        return Main.total_calories(input)

    def part_two(self, input):
        return Main.total_calories(input, 3)
