from collections import defaultdict, Counter
import math
import re
import copy
import pdb

# polymer = "NNCB"
polymer = "KHSNHFKVVSVPSCVHBHNP"

file = open('input-14.txt', 'r')
file_lines = file.readlines()

# this is a problem about merging multiple changes
# maybe we can find all the applicable rules and the index at which they apply
# and for each rule applied, bump the index of the others by 1

def step(polymer):
    insertions = []
    for rule in file_lines:
        to_match, to_insert = rule.split(' -> ')
        #index = polymer.find(to_match)
        finds = [m.start() for m in re.finditer(f'(?={to_match})', polymer)] #all the indexes where found
        for index in finds:
            # print(f'{to_match} found at {index} in {polymer}')
            insertions.append([to_insert.strip(), index+1])

    # need to sort the insertions or the next part won't work
    sorted_insertions = [[k, v] for k, v in sorted(insertions, key=lambda item: item[1])]

    for item in sorted_insertions:
        to_insert = item[0]
        index_value = item[1]
        # print(f'inserting {to_insert} at {index_value} in {polymer}')
        polymer = polymer[:index_value] + to_insert + polymer[index_value:]
        for index, i in enumerate(sorted_insertions):
            key = i[0]
            idx_v = i[1]
            sorted_insertions[index][1] += 1 

    return polymer

# for idx in range(0, 1):
#     polymer = step(polymer)
#     # print(polymer)
#     #print(len(polymer))

#     counts = Counter(polymer)
#     print(counts)
class Polymer:
# Part TWO! Let's count pairs instead.
# 1. starting pair counts
    def __init__(self, polymer):
        self.polymer = polymer
        self.pair_counts = defaultdict(lambda: 0)
        for index, char in enumerate(self.polymer):
            if index+1 < len(self.polymer):
                pair = char + self.polymer[index+1]
                self.pair_counts[pair] += 1

    # print(pair_counts)

    # 2. func for counting characters
    # the starting and ending characters are the only single-counted
    def count_characters(self):
        starting_char = self.polymer[0]
        ending_char = self.polymer[-1]
        char_counts = defaultdict(lambda: 0)
        for char, count in self.pair_counts.items():
            char_counts[char[0]] += count
            char_counts[char[1]] += count
        for char, count in char_counts.items():
            char_counts[char] = math.ceil(count/2)

        print(char_counts)
        return char_counts

    # count_characters(pair_counts, polymer)

    # 3. Cool, now we need to do the steps by updating pair counts as we go
    # If you have rule NN -> B, then you decrement NN's count and increment NB and BN's
    def do_step(self):
        temp_pair_counts = copy.deepcopy(self.pair_counts)
        for rule in file_lines:
            to_match, to_insert = rule.strip().split(' -> ')
            finds = self.pair_counts[to_match]
            # if finds != 0: print(f"Found {finds} of {to_match} will insert {to_insert}")
            # for find in range(0, finds):
                # TODO: check this, why is temp_pair_counts not updated?
            new_pair1 = to_match[0] + to_insert
            new_pair2 = to_insert + to_match[1]
            temp_pair_counts[to_match] -= finds
            # if temp_pair_counts[to_match] == 0: # to clean (optional)
            #     del temp_pair_counts[to_match]
            temp_pair_counts[new_pair1] += finds
            temp_pair_counts[new_pair2] += finds
                # pdb.set_trace()
        # print(f"Updated pair counts: {temp_pair_counts}")
        self.pair_counts = copy.deepcopy(temp_pair_counts)
        return self.pair_counts

pol = Polymer(polymer)
counts = {}
for step in range(0, 40):
    print(f'Step: {step}')
    pol.do_step()
    print(pol.pair_counts)
    counts = pol.count_characters()

print({k: v for k, v in sorted(counts.items(), key=lambda item: item[1])})