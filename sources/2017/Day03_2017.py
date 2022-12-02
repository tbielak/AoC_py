import AoC


class Main(AoC.Solution):

    update_x = [1, 0, -1, 0]
    update_y = [0, -1, 0, 1]
    count_update = [0, 1, 0, 1]

    def part_one(self, input):
        x = y = 0
        value = count = 1
        target = int(input)
        while True:
            for j in range(4):
                for i in range(count):
                    if value == target:
                        return abs(x) + abs(y)
                    x += Main.update_x[j]
                    y += Main.update_y[j]
                    value += 1
                count += Main.count_update[j]

    def part_two(self, input):
        target = int(input)
        p = (0, 0)
        spiral = {p: 1}
        count = 1
        while True:
            for j in range(4):
                for i in range(count):
                    value = sum(
                        spiral.get((p[0] + x, p[1] + y), 0)
                        for x in range(-1, 2)
                        for y in range(-1, 2)
                    )
                    if value > target:
                        return value
                    spiral[p] = value
                    p = (p[0] + Main.update_x[j], p[1] + Main.update_y[j])
                count += Main.count_update[j]
