#! /usr/bin/ruby

require 'pry'

class Point
  attr_accessor :x, :y

  def initialize(a, b)
    @x = a
    @y = b
  end

  def move(direction)
    # we only ever move one spot at a time to allow the chases to happen
    case direction
    when 'R'
      @x += 1
    when 'L'
      @x -= 1
    when 'U'
      @y += 1
    when 'D'
      @y -= 1
    end
  end

  def chase(head)
    if ! cover?(head) && ! adjacent?(head)
      # find the distance to the head, negative numbers are left and down, positve up and right
      a, b = distance_to(head)

      # find the movement to make, can be directly added to current position for new position
      a, b = find_planck_movement(a,b)
      @x += a
      @y += b
    end
  end

  def find_planck_movement(a,b)
    # if the value is 0, nothing happens.
    # if the value is 1, nothing happens.
    # if the value is 2, we divide by 2 to get to 1 and preserve the sign
    a = a/2 if a.abs == 2
    b = b/2 if b.abs == 2
    return a,b
  end

  def distance_to(point)
    return point.x - x, point.y - y
  end

  def cover?(point)
    # are the two points in the same spot?
    x == point.x && y == point.y
  end

  def adjacent?(point)
    # are the two points touching?
    (x - point.x).abs <= 1 && (y - point.y).abs <= 1 && ! cover?(point)
  end

  def to_s
    "#{x}:#{y}"
  end
end

input = <<-INPUT
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
INPUT

input = <<-INPUT
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
INPUT

input = File.read('input-9')

def solve_bridge(knots: 2, moves: [])
  positions = {}

  knots = Array.new(knots) { Point.new(0,0) }

  moves.split("\n").each do |move|
    direction, distance = move.match(/(\w) (\d+)/).captures
    distance.to_i.times do |_|
      knots.first.move(direction)
      knots.each_cons(2) do |segment|
        segment.last.chase(segment.first)
      end
      positions[knots.last.to_s] = 1
    end
  end
  return positions.size
end

p "Part 1 number of positions: #{solve_bridge(knots: 2, moves: input)}"
p "Part 2 number of positions: #{solve_bridge(knots: 10, moves: input)}"