# input = 5719

# Find the fuel cell's rack ID, which is its X coordinate plus 10.
# Begin with a power level of the rack ID times the Y coordinate.
# Increase the power level by the value of the grid serial number (your puzzle input).
# Set the power level to itself multiplied by the rack ID.
# Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
# Subtract 5 from the power level.

grid = Array.new (300) { Array.new(300) }

def get_power_level(x, y, input)
  rack_id = x + 10
  power_level = rack_id * y
  power_level += input
  power_level = power_level * rack_id
  if power_level >= 100
    power_level = power_level.to_s.split('')[-3].to_i
  else
    power_level = 0
  end
  power_level -= 5
end

input = 5719

# set the grid power levels
x_index = 0
while x_index < grid.size
  y_index = 0
  while y_index < grid[0].size
    grid[x_index][y_index] = get_power_level(x_index, y_index, input)
    y_index += 1
  end
  x_index += 1
end

def get_subgrid_total(start_x, start_y, size, grid)
  end_x = start_x
  until (end_x == grid.size - 1) or (end_x == start_x + size)
   end_x += 1
  end

  end_y = start_y
  until (end_y == grid[0].size - 1) or (end_y == start_y + size)
    end_y += 1
  end

  x_index = start_x
  sum = 0

  while x_index < end_x
    y_index = start_y
    while y_index < end_y
      sum += grid[x_index][y_index]
      y_index += 1
    end
    x_index += 1
  end

  sum
end


#part 2
guess_max_size = 20
size = 1

highest_power_level = 0
highest_x = 0
highest_y = 0
highest_grid_size = 0

(size..guess_max_size).to_a.each do |size|
  x_index = 0
  while x_index < grid.size
    y_index = 0
    while y_index < grid[0].size
      power_level = get_subgrid_total(x_index, y_index, size, grid)
      highest_x = x_index if power_level > highest_power_level
      highest_y = y_index if power_level > highest_power_level
      highest_grid_size = size if power_level > highest_power_level
      highest_power_level = power_level if power_level > highest_power_level
      y_index += 1
    end
    x_index += 1
  end
end

puts "Answer is #{highest_x},#{highest_y},#{highest_grid_size}"

