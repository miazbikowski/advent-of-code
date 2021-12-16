from collections import Counter

# Using readlines()
file = open('input-3.txt', 'r')
lines = file.readlines()

string_1 = ""
string_2 = ""
string_3 = ""
string_4 = ""
string_5 = ""
string_6 = ""
string_7 = ""
string_8 = ""
string_9 = ""
string_10 = ""
string_11 = ""
string_12 = ""

for line in lines:
	string_1 += line[0]
	string_2 += line[1]
	string_3 += line[2]
	string_4 += line[3]
	string_5 += line[4]
	string_6 += line[5]
	string_7 += line[6]
	string_8 += line[7]
	string_9 += line[8]
	string_10 += line[9]
	string_11 += line[10]
	string_12 += line[11]

strings = [string_1, string_2, string_3, string_4, string_5, string_6, string_7, string_8, string_9, string_10, string_11, string_12]

gamma = ""

for string in strings:
	res = Counter(string)
	gamma += max(res, key = res.get)
	
print(gamma)

def bit_flip(string):
	flipped_string = ""
	for char in string:
		if char == "0":
			flipped_string += "1"
		else:
		    flipped_string += "0"
	return flipped_string
			
epsilon = bit_flip(gamma)

final_result = int(gamma, 2) * int(epsilon, 2)
print(final_result)

# part 2 
matching_lines = [ line.strip() for line in lines]


for index in range(0,12):
	bit_1 = []
	bit_0 = []
	print("Initiating loop at index {}".format(index))
	print(len(matching_lines))
	for line in matching_lines:
		if line[index] == "1":
			bit_1.append(line)
		else:
			bit_0.append(line)
	if len(bit_1) >= len(bit_0):
		print("bit 1 wins")
		matching_lines = bit_1
	else:
		print("bit 0 wins")
		matching_lines = bit_0
	print(matching_lines)
	print("--------")
	if len(matching_lines) <= 1:
		break

print("Oxygen")
oxygen = int(matching_lines[0], 2)
print(matching_lines[0])
print(oxygen)


matching_lines = [ line.strip() for line in lines]
for index in range(12):
	bit_1 = []
	bit_0 = []
	print("Initiating loop at index {}".format(index))
	print(len(matching_lines))
	for line in matching_lines:
		if line[index] == "1":
			bit_1.append(line)
		else:
			bit_0.append(line)
	if len(bit_0) <= len(bit_1):
		print("bit 0 wins")
		matching_lines = bit_0
	else:
		print("bit 1 wins")
		matching_lines = bit_1
	print(matching_lines)
	print("--------")
	if len(matching_lines) <= 1:
		break

print("O2")
o2 = int(matching_lines[0],2)
print(matching_lines[0])
print(o2)

print("And the grand finale result is...")
print(oxygen * o2)

