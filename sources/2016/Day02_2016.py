import AoC


class Main(AoC.Solution):
    def press(keymap, digit):
        directions = "UDLR"
        curr = "5"
        for d in digit:
            curr = keymap[directions.find(d)][ord(curr) - ord("0")]
        return chr(ord(curr) - ord("0") - 10 + ord("A")) if curr > "9" else curr

    def enter_code(keymap, input):
        code = ""
        for digit in input:
            code += Main.press(keymap, digit)
        return code

    def part_one(self, input):
        return Main.enter_code(
            ["0123123456", "0456789789", "0112445778", "0233566899"], input
        )

    def part_two(self, input):
        return Main.enter_code(
            ["0121452349678;", "036785:;<9:=<=", "0122355678::;=", "0134467899;<<="],
            input,
        )
