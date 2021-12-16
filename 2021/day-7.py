input = [16,1,2,0,4,2,7,1,2,14]

file = open('input-7.txt', 'r')
file_lines = file.readlines()
input = [ int(value) for value in file_lines[0].split(',')]

# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)

print(Average(input))

from collections import Counter
data = Counter(input)
print(data.most_common)
print(data.most_common(1))  # Returns the highest occurring item

# sum = 0
# # maybe calc the average gap?
# for index, val in enumerate(input):
# 	if index == (len(input) -1):
# 		sum += abs(val - input[0])
# 	else:
# 		sum += abs(val - input[index+1])

# print(sum / len(input))

# 4, 2 and 5 - is the mode the answer?

goal = Average(input) / 2
print(goal)
total_cost = 0
for val in input:
	total_cost += abs(val - goal)

print(total_cost)
# nope it's not mode 65 at a cost of 419893
# it's also not average /2 (236) at a cost of 353059

# Let's brute force it for now
min_val = min(input)
max_val = max(input)

all_costs = []
for val in range(min_val, max_val):
	sum_cost = 0
	for item in input:
		#sum_cost += abs(item-val) # 5 instead becomes 1 + 2 + 3 + 4 + 5
		counter = abs(item-val)
		while(counter > 0):
			sum_cost += counter
			counter -= 1

	all_costs.append(sum_cost)

print(min(all_costs))
#93699985