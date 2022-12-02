import AoC


class Main(AoC.Solution):
    def part_one(self, input):
        x = c = 0
        width = len(input[0])
        for s in input:
            if s[x] == "#":
                c += 1
            x = (x + 3) % width
        return c

    def part_two(self, input):
        m = 1
        width = len(input[0])
        height = len(input)
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        for (sx, sy) in slopes:
            x = y = c = 0
            while True:
                if input[y][x] == "#":
                    c += 1
                x += sx
                y += sy
                x %= width
                if y >= height:
                    break
            m *= c
        return m
