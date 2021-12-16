import pdb;
from termcolor import colored, cprint

file = open('input-9.txt', 'r')
file_lines = file.readlines()

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

board = []
for file_line in file_lines:
	file_line = file_line.strip()
	line = []
	for item in file_line:
		line.append(int(item))
	board.append(line)

def print_neighbours(x, y, board):
	if x > 0:
		print(board[x-1][y])
	if x+1 < len(board):
		print(board[x+1][y])
	if y > 0:
		print(board[x][y-1])
	if y+1 < len(board[0]):
		print(board[x][y+1])


lowest_values = []
def check_neighbour(x, y, board):
	item_value = board[x][y]
	# print("Value: {}".format(item_value))
	lowest_value = True
	if x > 0:
		if board[x-1][y] <= item_value:
			lowest_value = False
	if x+1 < len(board):
		if board[x+1][y] <= item_value:
			lowest_value = False
	if y > 0:
		if board[x][y-1] <= item_value:
			lowest_value = False
	if y+1 < len(board[0]):
		if board[x][y+1] <= item_value:
			lowest_value = False
	# for dec in [-1, 0, 1]:
	# 	x_value = x + dec
	# 	if x_value >= 0 and x_value < len(board):
	# 		for y_dec in [-1, 0, 1]:
	# 			y_value = y + y_dec
	# 			if not (dec == 0 and y_dec == 0):
	# 				if y_value >= 0 and y_value < len(board[0]):
	# 					#print("Checking against: {}".format(board[x_value][y_value]))
	# 					if board[x_value][y_value] <= item_value:		
	# 						lowest_value = False
	if lowest_value == True:
		lowest_values.append(item_value)
		# print("Value: {}".format(item_value))
		# print_neighbours(x, y, board)
		# print("{} was the lowest!".format(item_value))
	# else:
	# 	print("Was not the lowest")

for x, row in enumerate(board):
	for y, col in enumerate(row):
		check_neighbour(x, y, board)

#print(lowest_values)
def calc_final_output():
	sum = 0
	for value in lowest_values:
		sum += (value+1)
	return sum

#print(calc_final_output())

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.basin = None

	def __eq__(self, other_point):
		return self.x == other_point.x and self.y == other_point.y

	def __repr__(self):
		return "{}, {}".format(self.x, self.y)

class Basin:
	def __init__(self):
		self.points = []

	def add_point(self, point):
		self.points.append(point)
		point.basin = self

	def has_neighbours_in_basin(self, point):
		x = point.x
		y = point.y
		# returns True/False if point is neighbours w/ another point in this basin
		# for dec in [-1, 0, 1]:
		# for dec in [-1, 0, 1]:
		# 	x_value = x + dec
		# 	if x_value >= 0 and x_value < len(board):
		# 		for y_dec in [-1, 0, 1]:
		# 			y_value = y + y_dec
		# 			if not (dec == 0 and y_dec == 0): # not if it's x,y itself
		# 				if y_value >= 0 and y_value < len(board[0]):
		# 					if Point(x_value, y_value) in self.points:
		# 						return True
		if x > 0:
			if Point(x-1, y) in self.points:
				return True
		if x+1 < len(board):
			if Point(x+1, y) in self.points:
				return True
		if y > 0:
			if Point(x, y-1) in self.points:
				return True
		if y+1 < len(board[0]):
			if Point(x, y+1) in self.points:
				return True
		return False
		# Missing a merge basins if 2 neighbours belong to different basins

	def size(self):
		return len(self.points)

	def __repr__(self):
		return str(self.size())

# let's test...
# basin = Basin()
# basin.add_point(Point(0,0))
# neighbour_point = Point(0, 1)
# assert(basin.point_part_of_basin(neighbour_point))
# not_neighbour_point = Point(2, 2)
# refute(basin.point_part_of_basin(not_neighbour_point))

basins = []

def merge_basins(basins_to_merge):
	points = []
	for basin in basins_to_merge:
		points.extend(basin.points)
		basins.remove(basin)
	new_basin = Basin()
	new_basin.points = points
	basins.append(new_basin)

# for x, row in enumerate(board):
# 	for y, col in enumerate(row):
for x in range(0, 20):
	for y in range(0, 20):
		# print(board[x][y])
		if board[x][y] != 9:
			point = Point(x, y)
			#Either I'm already part of a basin (based on having a neighbour who is)
			part_of_basin = False
			neighbour_basins = []
			for basin in basins:
				# if board[x][y] == 2:
				# 	pdb.set_trace()
				if basin.has_neighbours_in_basin(point):
					# print("Belongs to existing basin!")
					if len(neighbour_basins) == 0: # should only add to 1 basin
						basin.add_point(point)
					if basin not in neighbour_basins: # only add unique basins
						neighbour_basins.append(basin)
					part_of_basin = True
			# Merge basins if the point we were checking was a point touching 2 basins
			if part_of_basin == True and len(neighbour_basins) > 1:
				# print("Merging basins!")
				merge_basins(neighbour_basins)
			# If I'm not part of a basin but I'm not a 9, then I'm a new basin
			if part_of_basin == False:
				# print("New Basin found!")
				new_basin = Basin()
				new_basin.add_point(point)
				basins.append(new_basin)

print(basins)
print(len(basins))

def calculate_final_result():
	top_3_basins = [basins[0], basins[1], basins[2]]
	print(top_3_basins)
	for idx, basin in enumerate(basins):
		if idx == 0 or idx == 1 or idx == 2:
			continue
		for index, top_basin in enumerate(top_3_basins):
			if len(basin.points) > len(top_basin.points): # dunno why comparing .size doesn't work
				print("{} is bigger than {}".format(basin, top_basin))
				del top_3_basins[index]
				top_3_basins.append(basin)
				break


	print(top_3_basins)
	sum = 1
	for basin in top_3_basins:
		sum = sum * len(basin.points)
	return sum
	# after the above loop we should have the top 3 largest basins

print(calculate_final_result())

# 891000
# That's not the right answer; your answer is too low. - sounds like perhaps improperly merged basins?