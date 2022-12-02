import AoC


class Main(AoC.Solution):
    def load(input):
        data = []
        for s in input:
            data.append([int(s[0:5]), int(s[5:10]), int(s[10:15])])
        return data

    def is_triangle(x):
        x.sort()
        return 1 if x[0] + x[1] > x[2] else 0

    def part_one(self, input):
        return sum(Main.is_triangle(x) for x in Main.load(input))

    def part_two(self, input):
        data = Main.load(input)
        return sum(
            Main.is_triangle([data[i * 3][j], data[i * 3 + 1][j], data[i * 3 + 2][j]])
            for i in range(len(data) // 3)
            for j in range(3)
        )
