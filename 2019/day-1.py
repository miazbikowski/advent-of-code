print("Advent of Code - Day 1")

f = open("input1", "r")

masses = []
for x in f:
    masses.append(int(x))


TEST_CASES = {
  12: 2,
  14: 2,
  1969: 654,
  100756: 33583  
}


def calculate_fuel(mass):
    return (int(mass / 3 ) - 2)

def test_calculate_fuel():
  for test_key, test_value in TEST_CASES.items():
    assert calculate_fuel(test_key) == test_value
  print("looks like it worked!")  

test_calculate_fuel()

total_fuel = 0

for mass in masses:
    total_fuel += calculate_fuel(mass)

print("The total amount of fuel required is:")
print(total_fuel)