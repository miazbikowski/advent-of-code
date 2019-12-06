print("Advent of Code - Day 5")
import copy

f = open("input5", "r").read()
original_program_codes = [ int(x) for x in f.split(',')]
program_codes = copy.deepcopy(original_program_codes)

class OpCodesManager:
    def __init__(self, program_codes):
        self.program_codes = program_codes
        self.outputs = []
        self.input_var = 1

    def get_param(self, mode, increment, index):
        if mode == 0:
            return self.program_codes[self.program_codes[index + increment]]
        return self.program_codes[index + increment]

    def get_params(self, mode1, mode2, index):
        return self.get_param(mode1, 1, index), self.get_param(mode2, 2, index)    

    def add(self, mode1, mode2, idx):
        print("Opcode 1 being added to %d" % self.program_codes[idx + 3])
        param1, param2 = self.get_params(mode1, mode2, idx)
        self.program_codes[self.program_codes[idx + 3]] = param1 + param2

    def multiply(self, mode1, mode2, idx):
        param1, param2 = self.get_params(mode1, mode2, idx)
        self.program_codes[self.program_codes[idx + 3]] = param1 * param2

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
            elif opcode == 99:
                break
            else:
                print("OpCode was bad:", self.program_codes[index])
            # print(self.program_codes)
        return self.outputs[-1]

test_program_code = [3,0,4,0,99]
manager = OpCodesManager(test_program_code)
assert manager.process_opcodes() == 1

test_program_code = [1,2,3,0,99]
test_modes = [0,0]
manager = OpCodesManager(test_program_code)
manager.add(test_modes[0], test_modes[1], 0)
assert manager.program_codes == [3, 2, 3, 0, 99]

test_program_code = [1,2,3,0,99]
test_modes = [1,1]
manager = OpCodesManager(test_program_code)
manager.add(test_modes[0], test_modes[1], 0)
assert manager.program_codes == [5, 2, 3, 0, 99]

test_program_code = [1,2,3,0,99]
test_modes = [0,0,0]
manager = OpCodesManager(test_program_code)
manager.multiply(test_modes[0], test_modes[1], 0)
assert manager.program_codes == [0, 2, 3, 0, 99]

test_program_code = [1,2,3,0,99]
test_modes = [1,1,1]
manager = OpCodesManager(test_program_code)
manager.multiply(test_modes[0], test_modes[1], 0)
assert manager.program_codes == [6, 2, 3, 0, 99]

test_program_code = [1002,4,3,4,33]
manager = OpCodesManager(test_program_code)
manager.process_opcodes
print(manager.program_codes)

op_codes_manager = OpCodesManager(program_codes)
print(op_codes_manager.process_opcodes())