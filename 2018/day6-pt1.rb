#!/usr/bin/env ruby
require 'pry'

def manhattan_distance(p,q)
  p.zip(q).map{|u,v| (u-v).abs}.inject(:+) 
end

coordinates = File.read('input6.txt').chomp.split("\n")

# coordinates = [
#   '1, 1',
#   '1, 6',
#   '8, 3',
#   '3, 4',
#   '5, 5',
#   '8, 9'
# ]

alphabet = ("a".."z").to_a

height = 0
width = 0
coordinates.each_with_index do |coordinate, idx|
  coords = coordinate.split(',')
  height = coords[0].to_i if coords[0].to_i > height
  width = coords[1].to_i if coords[1].to_i > width
end

puts "Heigh is #{height}"
puts "Width is #{width}"

grid = Array.new(height) { Array.new(width, 10000) }
grid_id = Array.new(height) { Array.new(width, '') }
grid_counts = Array.new(height) { Array.new(width, 1) }

x_index = 0
while x_index < height
  y_index = 0
  while y_index < width
    coordinates.each_with_index do |coordinate, idx|
      coords = coordinate.split(',').map(&:to_i)
      closest = grid[x_index][y_index]
      distance = manhattan_distance(coords, [x_index, y_index])
      # puts "Distance between (#{x_index}, #{y_index}) and #{coordinate} is #{distance} and the closest is #{closest}"
      if closest == distance
        grid_counts[x_index][y_index] = 2
        grid_id[x_index][y_index] = '.'
      end  
      if distance < closest
        grid[x_index][y_index] = distance 
        grid_counts[x_index][y_index] = 1
        grid_id[x_index][y_index] = alphabet[idx]
      end
    end
    y_index += 1
  end
  x_index += 1 
end

final_counts = {}

x_index = 0
while x_index < height
  y_index = 0
  while y_index < width
    letter = grid_id[x_index][y_index]
    final_counts[letter] = final_counts.fetch(letter, 0) + 1
    y_index += 1
  end
  x_index += 1 
end

puts final_counts.sort_by { |key, value| value }


#we'll need to find the 4 closest to "corners" to exclude them for being infinite
# top-left coord with smallest overall numbers
# top-right smallest X, biggest Y
# bottom-left biggest X, smallest Y
# bottom-right biggest of both

