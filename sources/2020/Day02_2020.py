import AoC


class Main(AoC.Solution):
    def load(input):
        data = []
        for item in input:
            s = item.split(" ")
            range = s[0].split("-")
            data.append((int(range[0]), int(range[1]), s[1][0], s[2]))
        return data

    def part_one(self, input):
        data = Main.load(input)
        c = 0
        for (lmin, lmax, letter, password) in data:
            if lmin <= password.count(letter) <= lmax:
                c += 1
        return c

    def part_two(self, input):
        data = Main.load(input)
        c = 0
        for (lmin, lmax, letter, password) in data:
            if bool(password[lmin - 1] == letter) ^ bool(password[lmax - 1] == letter):
                c += 1
        return c
