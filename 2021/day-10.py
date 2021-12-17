file = open('input-10.txt', 'r')
file_lines = file.readlines()

INCOMPLETE = "Incomplete"
CORRUPTED = "Corrupted"
VALID = "Valid"

corrupted_points = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
}

points_total = 0

closing_matches = {
	'}': '{',
	']': '[',
	'>': '<',
	')': '(' 
}

def line_valid(line):
	global points_total
	unclosed_opens = []
	for char in line:
		if char in closing_matches.keys():
			# must close the last open
			if len(unclosed_opens) == 0 or unclosed_opens[-1] != closing_matches[char]: #line is invalid!
				# print("Line is invalid at char {}".format(char))
				points_total = points_total + corrupted_points[char]
				return CORRUPTED
			else:
				del unclosed_opens[-1]
		else:
			unclosed_opens.append(char)
	if len(unclosed_opens) != 0:
		# print("Line is incomplete (still has unclosed characters)")
		return INCOMPLETE
	# print("This line is valid!!")
	return VALID

lines_kept = []
for line in file_lines:
	line = line.strip()
	status = line_valid(line)
	if status == INCOMPLETE:
		lines_kept.append(line)

print(points_total)
# print(lines_kept)

# pt 2

autocomplete_points = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4
}

opening_matches = {
	'{': '}',
	'[': ']',
	'<': '>',
	'(': ')'
}

points_total = 0

def line_valid(line):
	global points_total
	unclosed_opens = []
	for char in line:
		if char in closing_matches.keys():
			# must close the last open
			if len(unclosed_opens) == 0 or unclosed_opens[-1] != closing_matches[char]: #line is invalid!
				return (CORRUPTED, [])
			else:
				del unclosed_opens[-1]
		else:
			unclosed_opens.append(char)
	if len(unclosed_opens) != 0:
		# print("Line is incomplete (still has unclosed characters)")
		return (INCOMPLETE, unclosed_opens)
	# print("This line is valid!!")
	return (VALID, [])

incomplete_lines = []
for line in file_lines:
	line = line.strip()
	status, incomplete_line = line_valid(line)
	if status == INCOMPLETE:
		incomplete_lines.append(incomplete_line)

print incomplete_lines

line_completions = []
for line in incomplete_lines:
	line_completion = []
	for char in line:
		line_completion.insert(0, opening_matches[char])
	line_completions.append(line_completion)

print(line_completions)

scores = []
for line in line_completions:
	score = 0
	for char in line:
		score = 5 * score + autocomplete_points[char]
	scores.append(score)

scores.sort()

import math
print(scores[int(math.ceil(len(scores)/2))])