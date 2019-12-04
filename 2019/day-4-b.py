min = 138307
max = 654504

print("Welcome to Day 4 of AoC!")


def get_integer_as_array(integer):
    return [int(digit) for digit in str(integer)]

def pair_followed_by_same_digit(iterable, pair_index, digit):
    if (pair_index + 2) < len(iterable) and iterable[pair_index +2] == digit:
        return True
    if (pair_index - 1) >= 0 and iterable[pair_index -1] == digit:
        return True
    return False

assert pair_followed_by_same_digit([1,1,1,2,3], 0, 1) == True
assert pair_followed_by_same_digit([1,1,2,2,3], 0, 1) == False

def contains_doubles_and_no_triples(iterable):
    pairs = [iterable[i:i + 2] for i in range(len(iterable) - 1)]
    for index, pair in enumerate(pairs):
        if pair[0] == pair[1]: 
            if pair_followed_by_same_digit(iterable, index, pair[0]) == False:
                return True
    return False

assert contains_doubles_and_no_triples(get_integer_as_array(112)) == True
assert contains_doubles_and_no_triples(get_integer_as_array(111122)) == True
assert contains_doubles_and_no_triples(get_integer_as_array(123)) == False
assert contains_doubles_and_no_triples(get_integer_as_array(123444)) == False

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
    if contains_doubles_and_no_triples(iterable_x) and is_monotic(iterable_x):
        passwords.append(x)

print(len(passwords))