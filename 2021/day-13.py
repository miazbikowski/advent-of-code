#fold along y=7
#fold along x=5
import copy

TEST_INSTRUCTIONS = [
	'y=7',
	'x=5'
]

MY_INSTRUCTIONS = [
	'x=655',
	'y=447',
	'x=327',
	'y=223',
	'x=163',
	'y=111',
	'x=81',
	'y=55',
	'x=40',
	'y=27',
	'y=13',
	'y=6'
]

file = open('input-13.txt', 'r')
file_lines = file.readlines()

line = [ '.' for item in range(0,1500) ]
grid = [ copy.deepcopy(line) for item in range(0,1500)]

for coords in file_lines:
	x, y = coords.split(',')
	grid[int(y)][int(x)] = '#'


# for line in grid:
# 	print(line)

def fold(grid, axis, position):
	# so what happens when we fold at line 7
	# line 8 (7+1) overlaps with line 6 (7-1)
	# line 9 (7+2) overlaps with line 5 (7-2)
	# and so on and so forth, while the other axis remains constant
	if axis == 'y':
		# so we will start at line 8 and work our way down...
		idx = 1
		for y_index, line in enumerate(grid):
			if y_index < position+1: 
				continue
			for x_index, point in enumerate(line):
				if point == '#':
					grid[position-idx][x_index] = '#'
					grid[y_index][x_index] = '.'
			idx += 1
		grid = grid[:position] #weird that this wasn't setting the grid back outside this func
		return grid
	else:
		for y_index, line in enumerate(grid):
			idx = 1
			for x_index, point in enumerate(line):
				if x_index < position+1: 
					continue
				if point == '#':
					grid[y_index][position-idx] = '#'
					grid[y_index][x_index] = '.'
				idx += 1
			line = line[:position]
			grid[y_index] = line
		return grid


# grid = fold(grid, 'x', 655)
# print("------------")
# for line in grid:
# 	print(line)

# grid = fold(grid, 'x', 5)
# print("------------")
# for line in grid:
# 	print(line)

for instructions in MY_INSTRUCTIONS:
	alignment, position = instructions.split('=')
	grid = fold(grid, alignment, int(position))

print("------------")
for line in grid:
	print(line)

count = 0
for line in grid:
	for point in line:
		if point == '#':
			count +=1

print(count)

# for part 2, 87 is not the right answer