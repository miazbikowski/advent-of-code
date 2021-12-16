print("Welcome to Day 10!")
from math import atan2, pi

f = open("input10", "r")

points = []
for x in f:
    points.append(x.replace('\n', ''))

class Canditate:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def angle_between(self, x2, y2:
		return atan2(x2 - x, y - y2) % (2 * pi)

	def slope(self, looking_at_x, looking_at_y):
		# m = slope = (y1-y2)/(x1-x2)
		# print(f'slope = ({self.y} - {looking_at_y}) / ({self.x} - {looking_at_x})')
		if (self.x-looking_at_x) == 0:
			return 0
		return (self.y - looking_at_y) / (self.x-looking_at_x) 

	def y_intercept(self, looking_at_x, looking_at_y):
		# b = y-intercept = (x1*y2 - x2*y1)/(x1-x2)
		# print(f'y-intercept = ({self.x} * {looking_at_y}) - ({looking_at_x} * {self.y}) / ({self.x} - {looking_at_x})')
		if (self.x - looking_at_x) == 0:
			return 0
		return ((self.x * looking_at_y) - (looking_at_x * self.y)) / (self.x - looking_at_x)

	def intercepts(self, looking_at_x, looking_at_y, x, y):
		# y = m*x + b
		intercept = (self.slope(looking_at_x, looking_at_y) * x) + self.y_intercept(looking_at_x, looking_at_y)
		print(intercept)
		# print(round(intercept)) ROUND IS TOO AGGRESSIVE
		return(float(y) == intercept)

	def it_me(self, x, y):
		return (self.x == x and self.y == y)

	def generate_limits(self, x, y):
		min_x, max_x, min_y, max_y = 0,0,0,0
		if x < self.x:
			min_x = x
			max_x = self.x
		if x > self.x:
			min_x = self.x
			max_x = x
		if y < self.y:
			min_y = y
			max_y = self.y
		if y > self.y:
			min_y = self.y
			max_y = y

		return min_x, max_x, min_y, max_y

# test1_cand = Canditate(0,0)
# assert test1_cand.intercepts(2, 2, 1,1) == True
# assert test1_cand.intercepts(2, 2, 1, 2) == False

class Grid:
	def __init__(self, points):
		self.grid = self.convert_strings_to_grid(points)
		self.asteroids = self.get_asteroids_list_from_grid()

	def convert_strings_to_grid(self, points):
		coords = [[points[row][col] for col in range(len(points[0]))] for row in range(len(points))]
		return coords

	def get_asteroids_list_from_grid(self):
		asteroids = []
		for row_index, row in enumerate(self.grid):
			for column_index, column in enumerate(row):
				if column != '.':
					asteroids.append(Canditate(row_index, column_index))
		return asteroids

	def get_visible(asteroids, check):
	    visible = set()
	    for asteroid in asteroids:
	        if asteroid == check:
	            continue

	        angle = check.angle_from(asteroid)
	        visible.add(angle)

	    return len(visible)

	def get_most_visible(asteroid_map):
	    most_visible = 0
	    asteroids = None
	    for asteroid in asteroids:
	        visible = get_visible(asteroids, asteroid)
	        most_visible = max(visible, most_visible)

	    return most_visible

	def count_asteroid_los(self, asteroid):
		total_los = 0
		for looking_at_asteroid in self.asteroids:
			asteroid_intercepted = False
			if asteroid.it_me(looking_at_asteroid.x,looking_at_asteroid.y): # don't look at yourself
				continue
			min_x, max_x, min_y, max_y = asteroid.generate_limits(looking_at_asteroid.x, looking_at_asteroid.y)
			for potentially_blocking_asteroid in self.asteroids:
				# For speed, stop if already intercepted by another asteroid
				if asteroid_intercepted:
					continue
				# If this asteroid out of bounds of being between the two others, we know it's not blocking
				if potentially_blocking_asteroid.x > max_x or potentially_blocking_asteroid.x < min_x:
					continue
				if potentially_blocking_asteroid.y > max_y or potentially_blocking_asteroid.y < min_y:
					continue
				 # the looker and the lookee can't be blocked by themselves
				if asteroid.it_me(potentially_blocking_asteroid.x, potentially_blocking_asteroid.y): 
				    continue
				if looking_at_asteroid.it_me(potentially_blocking_asteroid.x, potentially_blocking_asteroid.y):
					continue
				
				intercepts = asteroid.intercepts(looking_at_asteroid.x, looking_at_asteroid.y, potentially_blocking_asteroid.x, potentially_blocking_asteroid.y)
				if intercepts:
					# print(f'Intercept with {potentially_blocking_asteroid.x}, {potentially_blocking_asteroid.y} while checking for LOS on {looking_at_asteroid.x}, {looking_at_asteroid.y}')
					asteroid_intercepted = True
			if not asteroid_intercepted:
			    print(f'Has LOS on {looking_at_asteroid.x}, {looking_at_asteroid.y}')
			    total_los +=1
		return total_los

test_points33 = [
'......#.#.',
'#..#.#....',
'..#######.',
'.#.#.###..',
'.#..#.....',
'..#....#.#',
'#..#....#.',
'.##.#..###',
'##...#..#.',
'.#....####'
]


test_points35 = [
'#.#...#.#.',
'.###....#.',
'.#....#...',
'##.#.#.#.#',
'....#.#.#.',
'.##..###.#',
'..#...##..',
'..##....##',
'......#...',
'.####.###.'
]

test_points41 = [
'.#..#..###',
'####.###.#',
'....###.#.',
'..###.##.#',
'##.##.#.#.',
'....###..#',
'..#.#..#.#',
'#..#.#.###',
'.##...##.#',
'.....#.#..'
]

# test_points = [
# '#.........',
# '...A......',
# '...B..a...',
# '.EDCG....a',
# '..F.c.b...',
# '.....c....',
# '..efd.c.gb',
# '.......c..',
# '....f...c.',
# '...e..d..c',
# ]

grid = Grid(test_points33)
asteroid = Canditate(5, 8)

print(asteroid.intercepts(8, 0, 7, 3))

# print(grid.count_asteroid_los(asteroid))

# # grid = Grid(points)
# for asteroid in grid.asteroids:
# 	print(f'({asteroid.x}, {asteroid.y})')

# highest_count = 0
# print(len(grid.asteroids))
# for asteroid in grid.asteroids:
# 	count = grid.count_asteroid_los(asteroid)
# 	if count > highest_count:
# 		highest_count = count

# print(highest_count)


