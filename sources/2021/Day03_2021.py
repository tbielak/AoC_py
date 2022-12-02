import AoC


class Main(AoC.Solution):
    def part_one(self, input):
        gamma_bin = epsilon_bin = ""
        for i in range(len(input[0])):
            zeros = sum(1 if s[i] == "0" else 0 for s in input)
            ones = len(input) - zeros
            gamma_bin += "1" if zeros <= ones else "0"
            epsilon_bin += "1" if zeros > ones else "0"
        return int(gamma_bin, 2) * int(epsilon_bin, 2)

    def find_rating(input, xor_mask):
        consider = [True] * len(input)
        while True:
            for i in range(len(input[0])):
                zeros = ones = 0
                for j in range(len(input)):
                    if consider[j]:
                        if input[j][i] == "1":
                            ones += 1
                        else:
                            zeros += 1
                keep = chr((1 if ones >= zeros else 0) ^ xor_mask + ord("0"))
                for j in range(len(input)):
                    if consider[j] and input[j][i] != keep:
                        consider[j] = False
                if consider.count(True) == 1:
                    for j in range(len(input)):
                        if consider[j]:
                            return int(input[j], 2)

    def part_two(self, input):
        oxygen_rate = Main.find_rating(input, 0)
        co2_rate = Main.find_rating(input, 1)
        return oxygen_rate * co2_rate
