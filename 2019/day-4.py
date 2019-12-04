min = 138307
max = 654504

print("Welcome to Day 4 of AoC!")

def get_integer_as_array(integer):
    return [int(digit) for digit in str(integer)]

def contains_doubles(iterable):
    pairs = [iterable[i:i + 2] for i in range(len(iterable) - 1)]
    for index, pair in enumerate(pairs):
        if pair[0] == pair[1]: 
            return True
    return False

assert contains_doubles(get_integer_as_array(112)) == True
assert contains_doubles(get_integer_as_array(123)) == False

def is_monotic(iterable):
    for i in range(len(iterable) - 1):
        if iterable[i] > iterable[i + 1]: 
            return False
    return True

assert is_monotic(get_integer_as_array(1234)) == True
assert is_monotic(get_integer_as_array(4321)) == False

passwords = []
for x in range(min, max):
    iterable_x = get_integer_as_array(x)
    if contains_doubles(iterable_x) and is_monotic(iterable_x):
        passwords.append(x)

print(len(passwords))