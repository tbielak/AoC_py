import AoC


class Wire:
    def __init__(self, input):
        self.points = {}
        self.path = []
        for s in input.split(","):
            self.path.append((s[0], int(s[1:])))

    def twists_and_turns(self):
        step = x = y = 0
        turns = {"R": (1, 0), "U": (0, -1), "L": (-1, 0), "D": (0, 1)}
        for (direction, distance) in self.path:
            for i in range(distance):
                step += 1
                x += turns[direction][0]
                y += turns[direction][1]
                self.points[(x, y)] = step

    def distance_to_closest(self, other):
        distance = 2**30
        for p in self.points:
            if p in other.points:
                distance = min(distance, abs(p[0]) + abs(p[1]))
        return distance

    def fewest_steps(self, other):
        steps = 2**30
        for p, s in self.points.items():
            if p in other.points:
                steps = min(steps, s + other.points[p])
        return steps


class Main(AoC.Solution):
    def both_parts(self, input):
        w1 = Wire(input[0])
        w2 = Wire(input[1])
        w1.twists_and_turns()
        w2.twists_and_turns()
        return [w1.distance_to_closest(w2), w1.fewest_steps(w2)]
