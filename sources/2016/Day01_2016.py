import AoC


class Main(AoC.Solution):
    def load(input):
        route = []
        for s in input.replace(" ", "").split(","):
            route.append((1 if s[0] == "R" else -1, int(s[1:])))
        return route

    def walk(pos, face, steps=1):
        update = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # [ north, east, south, west ]
        return (pos[0] + update[face][0] * steps, pos[1] + update[face][1] * steps)

    def distance(pos):
        return abs(pos[0]) + abs(pos[1])

    def part_one(self, input):
        face = 0
        pos = (0, 0)
        for (direction, steps) in Main.load(input):
            face = (face + direction) & 3
            pos = Main.walk(pos, face, steps)
        return Main.distance(pos)

    def part_two(self, input):
        face = 0
        pos = (0, 0)
        visited = {pos}
        for (direction, steps) in Main.load(input):
            face = (face + direction) & 3
            for i in range(steps):
                pos = Main.walk(pos, face)
                if pos in visited:
                    return Main.distance(pos)
                visited.add(pos)
