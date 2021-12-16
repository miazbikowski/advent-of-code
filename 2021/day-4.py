import copy
import pdb
import re

# Using readlines()
numbers_file = open('input-4-a.txt', 'r')
numbers_lines = numbers_file.readlines()

# Using readlines()
boards_file = open('input-4-b.txt', 'r')
board_lines = boards_file.readlines()

boards = []
board = []
for index, line in enumerate(board_lines):
    if (index+1) % 6 == 0 and index != 0:
        boards.append(copy.deepcopy(board))
        board = []
    else:
        split_line = re.split(r'\s{1,}', line.strip())
        numbers = [ [int(value), False] for value in split_line]
        board.append(numbers)

    if index == len(board_lines) - 1:
        boards.append(copy.deepcopy(board))

def print_boards(boards):
    for board in boards:
        print_board(board)
        print(" ")

def print_board(board):
    for line in board:
        print(line)

def print_column(board, index):
    for line in board:
        print(line[index])

def update_board(number, board):
    for line in board:
        for value in line:
            if value[0] == int(number):
                value[1] = True

numbers = []
for line in numbers_lines:
    numbers = line.split(",")

def is_winning_board(board):
    for line in board:
        winning = is_winning_line(line)
        if winning == True:
            return True
    for index in range(0, len(board)):
        winning = is_winning_column(index, board)
        if winning == True:
            return True
    return False

def is_winning_line(line):
    for item in line:
        if item[1] == False:
            return False
    return True

def is_winning_column(index, board):
    for line in board:
        if line[index][1] == False:
            return False
    # print("Winning column!!")
    # print_column(board, index)
    return True

# print_boards(boards)

def calculate_result(board, number):
    total_sum = 0
    for line in board:
        for entry in line:
            if entry[1] == False:
                total_sum += entry[0]
    return total_sum * int(number)

def play_game(numbers, boards):
    for number in numbers:
        for board in boards:
            update_board(number, board)
            winning = is_winning_board(board)
            if winning == True:
                print("The winning board is: ")
                print_board(board)
                print("At number {}".format(number))
                print("The final result: {}".format(calculate_result(board, number)))
                return
# print_boards(boards)

# play_game(numbers, boards)

def lose_game(numbers, boards):
    for number in numbers:
        print(number)
        print("len: {}".format(len(boards)))
        i = 0
        boards_to_delete = []
        for board in boards:
            print("index: {}".format(i))
            update_board(number, board)
            print_board(board)
            print("---")
            winning = is_winning_board(board)
            if winning == True:
                last_board_to_win = board
                last_number_to_win = number
                last_calculated_result = calculate_result(board, number)
                boards_to_delete.append(board)
            i += 1
        for board in boards_to_delete:
            boards.remove(board) # can't use indexes
        print_boards(boards)
    print("The last board to win is: ")
    print_board(last_board_to_win)
    print("At number {}".format(last_number_to_win))
    print("The final result: {}".format(last_calculated_result))

lose_game(numbers, boards)
# not 4631
