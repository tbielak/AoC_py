import AoC


class Main(AoC.Solution):
    def part_one(self, input):
        score = 0
        for s in input:
            # 1 = rock, 2 = paper, 3 = scissors
            op = ord(s[0]) - ord("A") + 1
            me = ord(s[2]) - ord("X") + 1
            if op == me:
                score += me + 3
            else:
                score += me + (
                    6
                    if (me == 1 and op == 3)
                    or (me == 3 and op == 2)
                    or (me == 2 and op == 1)
                    else 0
                )
        return score

    def part_two(self, input):
        score = 0
        for s in input:
            # 1 = rock, 2 = paper, 3 = scissors
            op = ord(s[0]) - ord("A") + 1
            me = ord(s[2]) - ord("X") + 1
            if me == 2:
                score += op + 3
            else:
                score += ((op + (me % 3)) % 3) + (me - 1) * 3 + 1
        return score
