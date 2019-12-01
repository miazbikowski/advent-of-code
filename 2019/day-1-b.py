print("Advent of Code - Day 1")

f = open("input1", "r")

masses = []
for x in f:
    masses.append(int(x))


TEST_CASES = {
  14: 2,
  1969: 966,
  100756: 50346  
}


def calculate_fuel(mass):
    return (int(mass / 3 ) - 2)

def calculate_total_fuel(mass):
    fuel = calculate_fuel(mass)
    if fuel < 0:
        return 0
    else:
        return fuel + calculate_total_fuel(fuel)      

# TESTING
def test_calculate_fuel():
  for test_key, test_value in TEST_CASES.items():
    assert calculate_total_fuel(test_key) == test_value
  print("looks like it worked!")  

test_calculate_fuel()
# END TESTING

total_fuel = 0
for mass in masses:
    total_fuel += calculate_total_fuel(mass)

print("The total fuel needed for everything:", total_fuel)