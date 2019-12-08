print("Advent of Code - Day 7")
import copy
import itertools
import threading
import time

f = open("input7", "r").read()
program_codes = [ int(x) for x in f.split(',')]

class OpCodesManager:
    def __init__(self, program_codes, phase_input, input_signal=None):
        self.program_codes = copy.deepcopy(program_codes)
        self.outputs = []
        self.input_var = []
        self.feeds_amp = None
        if input_signal:
            self.input_var = input_signal
        self.input_var.append(phase_input) # phase_input has to come in 2nd

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

    def process_opcodes(self):
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
                while(len(self.input_var) == 0):
                    print("Going to sleep...")
                    time.sleep(1)

                input_var = self.input_var.pop()
                self.program_codes[self.program_codes[index+1]] = input_var
                index += 2
            elif opcode == 4:
                # here instead of appending, we'll use this to add to another Amp's input_vars
                # self.outputs.append(self.program_codes[self.program_codes[index + 1]])
                print("Found an output, feeding it into the next Amp.")
                self.feeds_amp.input_var.append(self.program_codes[self.program_codes[index + 1]])
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
        return self.outputs[-1]

def combinations(items):
    return ( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )


def test1():
    phase_inputs = [9,8,7,6,5]
    program_codes = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    highest_output = 0
    num_amps = 5
    phase_inputs_perms = list(itertools.permutations([5,6,7,8,9], 5))
    for phase_inputs in phase_inputs_perms:
        # instantiate the amps with their phase inputs and in the case of A, the input 0
        amp_a = OpCodesManager(program_codes, phase_inputs[0], 0)
        amp_b = OpCodesManager(program_codes, phase_inputs[1])
        amp_c = OpCodesManager(program_codes, phase_inputs[2])
        amp_d = OpCodesManager(program_codes, phase_inputs[3])
        amp_e = OpCodesManager(program_codes, phase_inputs[4])

        # set up pointers to each other for setting outputs
        amp_a.feeds_amp = amp_b
        amp_b.feeds_amp = amp_c
        amp_c.feeds_amp = amp_d
        amp_d.feeds_amp = amp_d
        amp_e.feeds_amp = amp_a

        t1 = threading.Thread(target=amp_a.process_opcodes)
        t2 = threading.Thread(target=amp_b.process_opcodes)
        t3 = threading.Thread(target=amp_c.process_opcodes)
        t4 = threading.Thread(target=amp_d.process_opcodes)
        t5 = threading.Thread(target=amp_e.process_opcodes)

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

        # next, find a way to know if the threads have all completed, then check
        # the outputs of each one? I expect only one amp will have an output left.

    # assert highest_output == 139629729

test1()
