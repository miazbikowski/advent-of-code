#!/usr/bin/env ruby

require 'pry'

def overlaps?(range, other)
 range.cover?(other.first) || other.cover?(range.first)
end

data = File.read('input3.txt').chomp.split("\n")
data.map! { |d| d.match(/#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/) }
size = 1000
counts = Array.new(size) { Array.new(size, []) }

data.map(&:to_a).map { |arr| arr.map(&:to_i) }.each do |_, id, left, top, width, height|
  w_range = (left..left + width - 1)
  h_range = (top..top + height - 1)

  h_range.each do |row|
    w_range.each do |col|
      counts[row][col] << id
    end
  end
end

data_list = data.map(&:to_a).map { |arr| arr.map(&:to_i) }

data_list.each do |_, id, left, top, width, height|
  w_range = (left..left + width - 1)
  h_range = (top..top + height - 1)

  intersects = false

  next_item_index = 0
  while next_item_index < data_list.size
    next_item = data_list[next_item_index]
    if next_item[1].to_i == id
      next_item_index += 1
      next
    end  
    next_w_range = (next_item[2].to_i..next_item[2].to_i + next_item[4].to_i)
    next_h_range = (next_item[3].to_i..next_item[3].to_i + next_item[5].to_i)

    # binding.pry

    if overlaps?(next_w_range, w_range) && overlaps?(next_h_range, h_range)
      puts "Found intersect between #{id} and #{next_item[1]}"
      intersects = true
      break
    end  

    next_item_index += 1
  end

  if intersects == false
    puts "And the WEENER IS #{id}"
  end  
end
