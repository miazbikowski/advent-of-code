file = open('input-11-test.txt', 'r')
file_lines = file.readlines()

# let's just transform them all to ints
file_lines = [ line.strip() for line in file_lines]
octopi = [ [int(char) for char in line ] for line in file_lines]
#print(octopi)

# You can only reach 10 once
flash_counts = 0
def flash(x, y):
	global flash_counts
	flash_counts += 1
	for x_value in [-1, 0, 1]:
		new_x = x+x_value
		if new_x >= 0 and new_x < len(octopi):
			for y_value in [-1, 0, 1]:
				new_y = y + y_value
				if new_y >= 0 and new_y < len(octopi[0]):
					if x == new_x and y == new_y:
						# print("Set current octopus to 0 because it flashed")
						octopi[x][y] = 0
					else:	
						if octopi[new_x][new_y] == 0:
							pass
						else:
							# print("Add 1 to neighbour at {},{}".format(new_x, new_y))
							octopi[new_x][new_y] = octopi[new_x][new_y] +1
							if octopi[new_x][new_y] == 10:
								flash(new_x, new_y)

def run_step():
	for x, line_of_octopus in enumerate(octopi):
		for y, octopus in enumerate(line_of_octopus):
			octopi[x][y] = octopi[x][y] +1

def run_flashes():
	for x, line_of_octopus in enumerate(octopi):
		for y, octopus in enumerate(line_of_octopus):
			if octopus == 10:
				flash(x, y)

steps = 2
for step in range(0, steps):
	run_step()
	run_flashes()

print(octopi)
print(flash_counts)