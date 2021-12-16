# Using readlines()
file = open('input-2.txt', 'r')
lines = file.readlines()

horizontal_pos = 0
depth = 0

for line in lines:
	direction, amount = line.split(" ")
	if direction == "forward":
		horizontal_pos += int(amount)
	elif direction == "up":
		depth -= int(amount)
	elif direction == "down":
		depth += int(amount)

print(horizontal_pos * depth)


horizontal_pos = 0
depth = 0
aim = 0

for line in lines:
	direction, amount = line.split(" ")
	if direction == "forward":
		horizontal_pos += int(amount)
		depth += (aim*int(amount))
	elif direction == "up":
		aim -= int(amount)
	elif direction == "down":
		aim += int(amount)

print(horizontal_pos * depth)