import copy

all_fish = [3,4,3,1,2]

file = open('input-6.txt', 'r')
file_lines = file.readlines()
all_fish = [ int(value) for value in file_lines[0].split(',')]

# print(all_fish)

# for day in range(1,19):
# 	for index in range(0, len(all_fish)):
# 		fish = all_fish[index]
# 		if fish == 0:
# 			all_fish[index] = 6
# 			all_fish.append(8)
# 		else:
# 			all_fish[index] -= 1
	# print("Day: {}".format(day))
	# print(all_fish)

# print(len(all_fish))

# For part 2, we won't maintain a list of fish but a list of counters for 0 to 8 that will increment as time goes
counters = [0, 0, 0, 0, 0, 0, 0, 0, 0] # index 0 to 8
temp_counters = copy.deepcopy(counters)
# instantiate based on input
for fish in all_fish:
	counters[fish] += 1

# print(counters)

# loop through the days
for day in range(1,257):
	for index, counter in enumerate(counters):
		if index == 0:
			temp_counters[6] = counter
			temp_counters[8] = counter
		elif index == 7:
			temp_counters[6] += counter # there are 2 ways you might reach 6, either from 0 or from 7 - need to account for this
		else:
			temp_counters[index-1] = counter 
	counters = copy.deepcopy(temp_counters)

sum = 0
for counter in counters:
	sum += counter


print(sum)