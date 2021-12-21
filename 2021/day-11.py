# Disclaimer: This is Marc N's refactoring of my broken code
# I don't wanna take credit for the fact it's working
# I still don't know what change he made that changed the behaviour at all

def flash(x, y, octopi):
    global flash_counts
    flash_counts += 1
    for x_value in [-1, 0, 1]:
        for y_value in [-1, 0, 1]:
            new_x = x + x_value
            new_y = y + y_value
            if not (0 <= new_x < len(octopi)):
                continue
            elif not (0 <= new_y < len(octopi[0])):
                continue
            elif (x, y) == (new_x, new_y):
                octopi[x][y] = 0
            elif 0 < octopi[new_x][new_y] < 10:
                octopi[new_x][new_y] = octopi[new_x][new_y] + 1
                if octopi[new_x][new_y] >= 10:
                    flash(new_x, new_y, octopi)


def run_step(octopi):
    for x, line_of_octopus in enumerate(octopi):
        for y in range(len(line_of_octopus)):
            octopi[x][y] = octopi[x][y] + 1


def run_flashes(octopi):
    for x, line_of_octopus in enumerate(octopi):
        for y, octopus in enumerate(line_of_octopus):
            if octopus == 10:
                flash(x, y, octopi)


def state(octopi, x, y):
    # print(f"Checking {x}, {y}")
    for line in octopi:
        print(''.join(str(val) for val in line))
    print('\n')

def check_if_synchronized(octopi):
	for line in octopi:
		for octopus in line:
			if octopus != 0:
				return False
	return True


def resolve(file_as_txt, steps):
    octopi = [[int(char) for char in line] for line in file_as_txt.split('\n')]
    for step in range(0, steps):
        run_step(octopi)
        run_flashes(octopi)
        if check_if_synchronized(octopi) == True:
        	print("They octopi have synchronized at step {}".format(step+1))
        	return
    print(octopi)
    return flash_counts


TEST = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

INPUT_MIA = """8548335644
6576521782
1223677762
1284713113
6125654778
6435726842
5664175556
1445736556
2248473568
6451473526"""

INPUT_MARC = """4738615556
6744423741
2812868827
8844365624
4546674266
4518674278
7457237431
4524873247
3153341314
3721414667"""

# Have to reset flash_counts since it's a global var
# flash_counts = 0
# assert resolve(TEST, 10) == 204
# flash_counts = 0
# assert resolve(TEST, 100) == 1656
# flash_counts = 0
# assert resolve(INPUT_MARC, 100) == 1615

flash_counts = 0
resolve(INPUT_MIA, 10000)
print(flash_counts)
