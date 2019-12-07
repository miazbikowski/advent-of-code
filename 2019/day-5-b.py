print("Advent of Code - Day 5")
import copy

f = open("input5", "r").read()
original_program_codes = [ int(x) for x in f.split(',')]
program_codes = copy.deepcopy(original_program_codes)

class OpCodesManager:
    def __init__(self, program_codes):
        self.program_codes = program_codes
        self.outputs = []
        self.input_var = 5

    def get_param(self, mode, increment, index):
        if mode == 0:
            return self.program_codes[self.program_codes[index + increment]]
        return self.program_codes[index + increment]

    def get_params(self, mode1, mode2, index):
        return self.get_param(mode1, 1, index), self.get_param(mode2, 2, index)    

    def add(self, mode1, mode2, idx):
        param1, param2 = self.get_params(mode1, mode2, idx)
        self.program_codes[self.program_codes[idx + 3]] = param1 + param2

    def multiply(self, mode1, mode2, idx):
        param1, param2 = self.get_params(mode1, mode2, idx)
        self.program_codes[self.program_codes[idx + 3]] = param1 * param2

    def less_than(self, mode1, mode2, idx):
        param1, param2 = self.get_params(mode1, mode2, idx)
        self.program_codes[self.program_codes[idx + 3]] = 1 if param1 < param2 else 0

    def equal(self, mode1, mode2, idx):
        param1, param2 = self.get_params(mode1, mode2, idx)
        self.program_codes[self.program_codes[idx + 3]] = 1 if param1 == param2 else 0

    def jump_if_true(self, mode1, mode2, idx):
        param1, param2 = self.get_params(mode1, mode2, idx)
        return param2 if param1 != 0 else idx + 3

    def jump_if_false(self, mode1, mode2, idx):
        param1, param2 = self.get_params(mode1, mode2, idx)
        return param2 if param1 == 0 else idx + 3

    @staticmethod
    def get_modes(modes):
        return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]

    def process_opcodes(self,):
        index = 0
        while self.program_codes[index] != 99:
            mode1, mode2, mode3, opcode = self.get_modes(f"{self.program_codes[index]:05}")
            if opcode == 1:
                self.add(mode1, mode2, index)
                index += 4
            elif opcode == 2:
                self.multiply(mode1, mode2, index)
                index += 4
            elif opcode == 3:
                self.program_codes[self.program_codes[index+1]] = self.input_var
                index += 2
            elif opcode == 4:
                self.outputs.append(self.program_codes[self.program_codes[index + 1]])
                index += 2
            elif opcode == 5:
                index = self.jump_if_true(mode1, mode2, index)
            elif opcode == 6:
                index = self.jump_if_false(mode1, mode2, index)
            elif opcode == 7:
                self.less_than(mode1, mode2, index)
                index += 4
            elif opcode == 8:
                self.equal(mode1, mode2, index)
                index += 4    
            elif opcode == 99:
                break
            else:
                print("OpCode was bad:", self.program_codes[index])
            # print(self.program_codes)
        return self.outputs[-1]

op_codes_manager = OpCodesManager(program_codes)
print(op_codes_manager.process_opcodes())