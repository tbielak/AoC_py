import AoC


class IntcodeVM:
    def parse(input):
        memory = {}
        code = [int(x) for x in input.split(",")]
        for i in range(len(code)):
            memory[i] = code[i]
        return memory

    def __init__(self, memory):
        self.ip = 0
        self.memory = memory.copy()

    def patch(self, address, value):
        self.memory[address] = value

    def peek(self, address):
        return self.memory[address]

    def fetch(self):
        self.ip += 1
        return self.memory[self.memory[self.ip - 1]]

    def store(self, value):
        self.ip += 1
        self.memory[self.memory[self.ip - 1]] = value

    def run(self):
        while True:
            op = self.memory[self.ip]
            self.ip += 1
            if op == 1:
                self.store(self.fetch() + self.fetch())
            elif op == 2:
                self.store(self.fetch() * self.fetch())
            elif op == 99:
                return
            else:
                raise RuntimeError("unsupported operation")


class Main(AoC.Solution):
    def part_one(self, input):
        vm = IntcodeVM(IntcodeVM.parse(input))
        vm.patch(1, 12)
        vm.patch(2, 2)
        vm.run()
        return vm.peek(0)

    def part_two(self, input):
        program = IntcodeVM.parse(input)
        for noun in range(101):
            for verb in range(101):
                vm = IntcodeVM(program)
                vm.patch(1, noun)
                vm.patch(2, verb)
                vm.run()
                if 19690720 == vm.peek(0):
                    return 100 * noun + verb
