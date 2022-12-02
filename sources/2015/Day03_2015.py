import AoC


class Main(AoC.Solution):
    def part_one(self, input):
        x = y = 0
        visited = {(0, 0)}
        for c in input:
            if "^" == c:
                y -= 1
            if "v" == c:
                y += 1
            if ">" == c:
                x -= 1
            if "<" == c:
                x += 1
            visited.add((x, y))
        return len(visited)

    def part_two(self, input):
        x = [0, 0]
        y = [0, 0]
        visited = {(0, 0)}
        i = 0
        for c in input:
            if "^" == c:
                y[i] -= 1
            if "v" == c:
                y[i] += 1
            if ">" == c:
                x[i] -= 1
            if "<" == c:
                x[i] += 1
            visited.add((x[i], y[i]))
            i ^= 1
        return len(visited)
