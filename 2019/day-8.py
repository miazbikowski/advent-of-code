print("Welcome to Day 8!")

f = open("input8", "r").read()
digits = [ int(x) for x in str(f)]
width = 25
height = 6

def multiply_digits(layer):
    ones_count = 0
    twos_count = 0
    for row in range(0, len(layer)):
        for col in range(0, len(layer[row])):
            if layer[row][col] == 1:
                ones_count +=1
            elif layer[row][col] == 2:
                twos_count +=1

    return ones_count * twos_count

def verify(digits, width, height):
    all_layers = []
    column_counter = 0
    row_counter = 0
    zeros_count = 0
    lowest_zeros_counted = 9999
    least_zeros_layer = 0
    new_layer = [[0 for x in range(width)] for y in range(height)]

    for digit in digits:
        if column_counter == width:
            row_counter +=1
            column_counter = 0
        if row_counter == height:
            row_counter = 0
            all_layers.append(new_layer)
            if zeros_count <= lowest_zeros_counted:
                lowest_zeros_counted = zeros_count
                layer_index = (len(all_layers)-1)
                least_zeros_layer = layer_index  # this means the layer we're on now's index should have the highest zeros counted
            new_layer = [[0 for x in range(width)] for y in range(height)]
            zeros_count = 0
            
        new_layer[row_counter][column_counter] = digit
        if digit == 0:
            zeros_count += 1
        column_counter +=1

    all_layers.append(new_layer)
    return all_layers[least_zeros_layer]

# test_digits = [1,1,2,0,0, 1,1,2,2,1, 1,0,1,1,2, 2,2,2,2,2, 0,0,0,0,0, 1,1,1,2,2]
# least_zeros_layer = verify(test_digits, 5, 2)
# print(multiply_digits(least_zeros_layer))

least_zeros_layer = verify(digits, width, height)
print(multiply_digits(least_zeros_layer))