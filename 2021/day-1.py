# Using readlines()
file = open('input-1.txt', 'r')
Lines = file.readlines()
 
count = 0
decrease_count = 0
previous_number = 0

last_index = len(Lines) - 4
print(last_index)

# Part 1
for index, line in enumerate(Lines):
    if index == 0:
        continue
    else:
        if line > previous_number:
            count += 1
        else:
            decrease_count += 1
    previous_number = line

print("count of increases: {}".format(count))
print("count of decreases: {}".format(decrease_count))
# print("Line{}: {}".format(count, line.strip()))

count = 0

for index in range(0, last_index+1):
    window1 = int(Lines[index]) + int(Lines[index+1]) + int(Lines[index+2])
    window2 = int(Lines[index+1]) + int(Lines[index+2]) + int(Lines[index+3])

    if window2 > window1:
        count += 1

    if index == last_index:
        print("Last count: {} {}".format(window1, window2))

print("count of increases: {}".format(count))