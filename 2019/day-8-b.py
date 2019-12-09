print("Welcome to Day 8!")

f = open("input8", "r").read()
digits = [ int(x) for x in str(f)]
width = 25
height = 6

def get_layers(digits, width, height):
    all_layers = []
    column_counter = 0
    row_counter = 0
    new_layer = [[0 for x in range(width)] for y in range(height)]

    for digit in digits:
        if column_counter == width:
            row_counter +=1
            column_counter = 0
        if row_counter == height:
            row_counter = 0
            all_layers.append(new_layer)
            new_layer = [[0 for x in range(width)] for y in range(height)]
            
        new_layer[row_counter][column_counter] = digit
        column_counter +=1

    all_layers.append(new_layer)
    return all_layers

# test_digits = [1,1,2,0,0, 1,1,2,2,1, 1,0,1,1,2, 2,2,2,2,2, 0,0,0,0,0, 1,1,1,2,2]
# least_zeros_layer = verify(test_digits, 5, 2)
# print(multiply_digits(least_zeros_layer))

def process_image(layers, width, height):
    final_image = [[0 for x in range(width)] for y in range(height)]
    for row in range(0, height):
        for column in range(0, width):
            for layer in layers:
                digit = layer[row][column]
                if digit == 2:
                    continue
                else:
                    final_image[row][column] = digit
                    break

    return final_image                    


# digits = [0,2,2,2,1,1,2,2,2,2,1,2,0,0,0,0]
# width = 2
# height = 2

layers = get_layers(digits, width, height)
image = process_image(layers, width, height)

for row in image:
    string = ""
    for x in [str(y) for y in row]:
        string += x
    print(string)