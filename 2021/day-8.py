file = open('input-8.txt', 'r')
file_lines = file.readlines()

output_values = ""
unique_signal_patterns = ""
for file_line in file_lines:
	unique_signal_patterns_for_line = file_line.split('|')[0]
	output_values_for_line = file_line.split('|')[1]
	unique_signal_patterns = output_values_for_line.replace('\n', '')
	output_values += output_values_for_line.replace('\n', '')
output_values = output_values.split(' ')
unique_signal_patterns = unique_signal_patterns.split(' ')

# print(unique_signal_patterns)
# print(output_values)

count = 0
for val in output_values:
	if len(val) in [2, 3, 4, 7]:
		count +=1

print(count)

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

output_values = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
unique_signal_patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']

dict_possibilities = {
	'a': [],
	'b': [],
	'c': [],
	'd': [],
	'e': [],
	'f': [],
	'g': []
}

unique_value_lengths = {
	2: 1,
	4: 4,
	3: 7,
	# 7: 8
}

segment_mappings = {
	0: ['a', 'b', 'c', 'e', 'f', 'g'],
	1: ['c', 'f'],
	2: ['a', 'c', 'd', 'e', 'g'],
	3: ['a', 'c', 'd', 'f', 'g'],
	4: ['b', 'c', 'd', 'f'],
	5: ['a', 'b', 'd', 'f', 'g'],
	6: ['a', 'b', 'd', 'e', 'f', 'g'],
	7: ['a', 'c', 'f'],
	8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
}

for val in unique_signal_patterns:
	if len(val) in unique_value_lengths.keys():
		possibilities = segment_mappings[unique_value_lengths[len(val)]]
		for letter in val:
			# add possibilities
			dict_possibilities[letter].append(possibilities)

print(dict_possibilities)