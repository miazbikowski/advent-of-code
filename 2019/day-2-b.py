print("Advent of Code - Day 2")
import copy

f = open("input2", "r").read()

original_program_codes = [ int(x) for x in f.split(',')]
program_codes = copy.deepcopy(original_program_codes)

class OpCodesManager:
    def __init__(self, program_codes):
        self.program_codes = program_codes

    def do_addition(self, index):
        first_index = self.program_codes[index + 1]
        second_index = self.program_codes[index + 2]
        third_index = self.program_codes[index + 3]

        first_num = self.program_codes[first_index]
        second_num = self.program_codes[second_index]

        self.program_codes[third_index] = first_num + second_num

    def do_multiplication(self, index):
        first_index = self.program_codes[index + 1]
        second_index = self.program_codes[index + 2]
        third_index = self.program_codes[index + 3]

        first_num = self.program_codes[first_index]
        second_num = self.program_codes[second_index]

        self.program_codes[third_index] = first_num * second_num

    def process_opcodes(self):
        index = 0
        while index < len(self.program_codes):
            if self.program_codes[index] == 1:
                self.do_addition(index)
            elif self.program_codes[index] == 2:
                self.do_multiplication(index)
            elif self.program_codes[index] == 99:
                return self.program_codes
            else:
                print("OpCode was bad:", self.program_codes[index])
            index += 4
        return self.program_codes    

TEST_CASE1 = [1,1,1,4,99,5,6,0,99]
TEST1_ANSWER  = [30,1,1,4,2,5,6,0,99]

op_codes_manager = OpCodesManager(TEST_CASE1)
op_codes_manager.process_opcodes()

assert op_codes_manager.program_codes == TEST1_ANSWER

def brute_force():
    print("Starting BRUTE FORCE!!!")
    noun = 0
    while noun < 100:
        verb = 0
        while verb < 100:
            program_codes = copy.deepcopy(original_program_codes)
            program_codes[1] = noun
            program_codes[2] = verb
            op_codes_manager = OpCodesManager(program_codes)
            op_codes_manager.process_opcodes()
            if op_codes_manager.program_codes[0] == 19690720:
                print("At index 1: %d, At index 2: %d" % (noun, verb))
                print("So the answer is... %d !!!!" % (100 * noun + verb))
                return
            verb +=1
        noun +=1

brute_force()
