import AoC


class Main(AoC.Solution):
    def part_one(self, input):
        area = 0
        for line in input:
            l, w, h = [int(i) for i in line.split("x")]
            x = [l * w, w * h, h * l]
            x.sort()
            area = area + sum(x) * 2 + x[0]
        return area

    def part_two(self, input):
        ribbon = 0
        for line in input:
            x = [int(i) for i in line.split("x")]
            x.sort()
            ribbon = ribbon + 2 * (x[0] + x[1]) + x[0] * x[1] * x[2]
        return ribbon
