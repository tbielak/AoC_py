import AoC


class Main(AoC.Solution):
    def load(input):
        fabrics = []
        for line in input:
            parts = line.split(" ")
            point = parts[2].replace(":", "").split(",")
            size = parts[3].split("x")
            fabrics.append(
                (
                    int(parts[0][1:]),
                    int(point[0]),
                    int(point[1]),
                    int(size[0]),
                    int(size[1]),
                )
            )
        return fabrics

    def part_one(self, input):
        points = {}
        for (_, px, py, width, height) in Main.load(input):
            for x in range(px, px + width):
                for y in range(py, py + height):
                    points[(x, y)] = points.get((x, y), 0) + 1
        return sum(1 for v in points.values() if v > 1)

    def part_two(self, input):
        ids = set()
        points = {}
        for (id, px, py, width, height) in Main.load(input):
            ids.add(id)
            for x in range(px, px + width):
                for y in range(py, py + height):
                    if not (x, y) in points:
                        points[(x, y)] = set()
                    points[(x, y)].add(id)

        for point_ids in points.values():
            if len(point_ids) > 1:
                ids.difference_update(point_ids)

        return ids.pop()
