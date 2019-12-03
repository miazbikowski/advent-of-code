print("Advent of Code - Day 3")

f = open("input3-1", "r").read()
wire1_moves = f.split(',')

f = open("input3-2", "r").read()
wire2_moves = f.split(',')

from math import*
 
def manhattan_distance(x,y):
    # distance += abs(x_value - x_goal) + abs(y_value - y_goal)
    return sum(abs(a-b) for a,b in zip(x,y))

 # Test the manhattan distance function
assert manhattan_distance([15,20],[10,30]) == 15


def step_right(current_coord):
    current_coord = (current_coord[0]+1, current_coord[1])
    return current_coord

# Test step_right
assert step_right((0,0)) == (1,0)

def step_left(current_coord):
    current_coord = (current_coord[0]-1, current_coord[1])
    return current_coord

# Test step_left
assert step_left((0,0)) == (-1,0)


def step_up(current_coord):
    current_coord = (current_coord[0], current_coord[1]+1)
    return current_coord

# Test step_up
assert step_up((0,0)) == (0,1)

def step_down(current_coord):
    current_coord = (current_coord[0], current_coord[1]-1)
    return current_coord

# Test step_down
assert step_down((0,0)) == (0,-1)

def move_line(wire_moves):
    line_coords = []
    current_coord = (0,0)
    for move in wire_moves:
        direction = move[0]
        length = int(move[1:])
        if direction == 'R':
            for x in range(length):
                current_coord = step_right(current_coord)
                line_coords.append(current_coord)
        elif direction == 'L':
            for x in range(length):
                current_coord = step_left(current_coord)
                line_coords.append(current_coord)
        elif direction == 'U':
            for x in range(length):
                current_coord = step_up(current_coord)
                line_coords.append(current_coord)
        elif direction == 'D':
            for x in range(length):
                current_coord = step_down(current_coord)
                line_coords.append(current_coord)
    return line_coords

def overlapping_coords(coords1, coords2):
    overlapping = []
    for x in coords1:
        for y in coords2:
            if x == y:
                overlapping.append(x)
    return overlapping


# TEST_MOVES_1 = ['R8','U5','L5','D3']
coords1 = move_line(wire1_moves)
# print(coords1)
# TEST_MOVES_2 = ['U7','R6','D4','L4']
coords2 = move_line(wire2_moves)
# print(coords2)

overlapping = overlapping_coords(coords1, coords2)

distances = []
for coords in overlapping:
    distances.append(manhattan_distance((0,0), coords))

distances.sort()
print("Smallest distance is:", *distances[:1])

