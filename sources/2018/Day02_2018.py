import AoC


class Main(AoC.Solution):
    def part_one(self, input):
        two = three = 0
        for s in input:
            charcount = {}
            for c in s:
                charcount[c] = charcount.get(c, 0) + 1
            two += int(2 in charcount.values())
            three += int(3 in charcount.values())
        return two * three

    def diff(s1, s2):
        x = ""
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                x += s1[i]
        return x

    def part_two(self, input):
        for i in range(len(input)):
            for j in range(i + 1, len(input)):
                x = Main.diff(input[i], input[j])
                if len(x) == len(input[i]) - 1:
                    return x
