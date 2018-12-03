#!/usr/bin/env ruby

require 'pry'

data = File.read('input3.txt').chomp.split("\n")
data.map! { |d| d.match(/#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/) }
size = 1000
counts = Array.new(size) { Array.new(size, 0) }

data.map(&:to_a).map { |arr| arr.map(&:to_i) }.each do |_, id, left, top, width, height|
  w_range = (left..left + width - 1)
  h_range = (top..top + height - 1)

  h_range.each do |row|
    w_range.each do |col|
      counts[row][col] += 1
    end
  end
end

puts counts.flatten.count { |e| e >= 2}