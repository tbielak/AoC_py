import AoC


class Main(AoC.Solution):
    def load(input):
        data = []
        for line in input:
            data.append([int(s) for s in line.split("\t")])
        return data

    def part_one(self, input):
        return sum(max(row) - min(row) for row in Main.load(input))

    def part_two(self, input):
        sum = 0
        for row in Main.load(input):
            for i in range(len(row)):
                for j in range(i + 1, len(row)):
                    a, b = row[i], row[j]
                    if a < b:
                        a, b = b, a

                    if a % b == 0:
                        sum += a // b
                        break
        return sum
