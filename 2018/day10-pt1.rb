require 'pry'

text_lines = File.read('test-input10.txt').chomp.split("\n")

class Point
  attr_accessor :x, :y, :x_vel, :y_vel

  def initialize(line)
    data = line.match /position=<( *-*\d+), ( *-*\d+)> velocity=<( *-*\d+), ( *-*\d+)>/
    @x = data[1].to_i
    @y = data[2].to_i
    @x_vel = data[3].to_i
    @y_vel = data[4].to_i
  end

  def move_one_second
    @x += @x_vel
    @y += @y_vel
  end

  def move_back_one_second
    @x -= @x_vel
    @y -= @y_vel
  end
end

points = []

text_lines.each do |text_line|
  points << Point.new(text_line)
end

min_x = points.min_by(&:x).x
min_y = points.min_by(&:y).y
max_x = points.max_by(&:x).x
max_y = points.max_by(&:y).y

box_size = (max_y - min_y) * (max_x - min_x)
last_box_size = 99999999999999

seconds = 0
while(last_box_size >= box_size)
  points.each(&:move_one_second)
  puts points[0].inspect
  min_x = points.min_by(&:x).x
  min_y = points.min_by(&:y).y
  max_x = points.max_by(&:x).x
  max_y = points.max_by(&:y).y
  last_box_size = box_size
  box_size = (min_y - min_x) * (max_x - max_y)
  seconds += 1
  puts "Box size: #{box_size}"
end

points.each(&:move_back_one_second)

output = Array.new (max_y - min_y + 1) { Array.new((max_x - min_x + 1), ' ') }

points.each do |point|
  output[point.y - min_y][point.x - min_x] = "#"
end

puts output.map{|v| v.join('') }.join("\n")
