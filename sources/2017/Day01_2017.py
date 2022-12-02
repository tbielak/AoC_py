import AoC


class Main(AoC.Solution):
    def count(input, add=1):
        sum = 0
        for i in range(len(input)):
            if input[i] == input[(i + add) % len(input)]:
                sum += ord(input[i]) - ord("0")
        return sum

    def part_one(self, input):
        return Main.count(input)

    def part_two(self, input):
        return Main.count(input, len(input) // 2)
