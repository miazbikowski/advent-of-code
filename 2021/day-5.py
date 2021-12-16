import re
import pdb

# Using readlines()
file = open('input-5.txt', 'r')
file_lines = file.readlines()

class Line:
	def __init__(self, start_x, start_y, end_x, end_y):
		self.start_x = start_x
		self.start_y = start_y
		self.end_x = end_x
		self.end_y = end_y

	def within_x_point(self, x):
		# if (x >= self.start_x and x <= self.end_x) or (x >= self.end_x and x <= self.start_x):
		# 	return True
		# return False

		return (min(self.start_x, self.end_x) <= x <= max(self.start_x, self.end_x))

	def within_y_point(self, y):
		# if (y >= self.start_y and y <= self.end_y) or (y >= self.end_y and y <= self.start_y):
		# 	return True
		# return False

		return (min(self.start_y, self.end_y) <= y <= max(self.start_y, self.end_y))

	def intersects_with_point(self, x, y):
		x_calc = (self.end_x - self.start_x)
		if x_calc != 0: 
			slope = (self.end_y - self.start_y) / x_calc
		else:
			slope = 0

		if slope == 0:
			pt3_on = True
		else: 
			pt3_on = (y - self.start_y) == slope * (x - self.start_x)

		# pt3_between = (min(self.start_x, self.end_x) <= x <= max(self.start_x, self.end_x)) and (min(self.start_y, self.end_y) <= y <= max(self.start_y, self.end_y))
		pt3_between = self.within_x_point(x) and self.within_y_point(y)

		return pt3_on and pt3_between


	def __repr__(self):
		return "{},{} -> {},{}".format(self.start_x, self.start_y, self.end_x, self.end_y)

# create our line instances
lines = []
for file_line in file_lines:
	result = re.match(r"(\d*),(\d*)\s->\s(\d*),(\d*)", file_line)
	groups = result.groups()
	x1 = int(groups[0])
	y1 = int(groups[1])
	x2 = int(groups[2])
	y2 = int(groups[3])
	if x1 == x2 or y1 == y2:
		line = Line(x1, y1, x2, y2)
		lines.append(line)

# print(lines)

# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. 
# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

# Go through the grid point by point and count if at least 2
# grid is 000 to 999

total_overlaps_counter = 0
lines_counter = 0

for x in range(0,1000):
	for y in range(0,1000):
		for line in lines:
			if line.within_x_point(x) and line.within_y_point(y):
				lines_counter += 1
		if lines_counter > 1:
			total_overlaps_counter += 1
		lines_counter = 0

# print(total_overlaps_counter)

# part 2 - we need diagonals

lines = []
for file_line in file_lines:
	result = re.match(r"(\d*),(\d*)\s->\s(\d*),(\d*)", file_line)
	groups = result.groups()
	x1 = int(groups[0])
	y1 = int(groups[1])
	x2 = int(groups[2])
	y2 = int(groups[3])
	line = Line(x1, y1, x2, y2)
	lines.append(line)

# print(lines)

total_overlaps_counter = 0
lines_counter = 0

for y in range(0,1000):
	row_string = ""
	for x in range(0,1000):
		for line in lines:
			if line.intersects_with_point(x,y):
				lines_counter += 1
		if lines_counter > 1:
			total_overlaps_counter += 1
		row_string += str(lines_counter)
		lines_counter = 0
	# print(row_string)


print(total_overlaps_counter)