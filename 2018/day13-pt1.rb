require 'pry'
require 'colorize'

file_lines = File.read('input13.txt').chomp.split("\n")

class Cart
  attr_accessor :direction, :x, :y, :id
  DIRECTIONS = ['L', 'S', 'R']

  def initialize(id, direction, x, y)
    @id = id
    @direction = direction
    @x = x
    @y = y
    @next_direction = nil
  end

  def get_next_track(tracks)
    if @direction == '^'
      nxt = tracks[@y-1][@x]
    elsif @direction == '>'
      nxt = tracks[@y][@x+1]
    elsif @direction == '<'
      nxt = tracks[@y][@x-1]
    else
      nxt = tracks[@y+1][@x]
    end    
       
    nxt          
  end

  def move_ahead_one
    if @direction == '^'
      @y -= 1
    elsif @direction == '>'
      # puts "moving > from #{@x},#{@y} to #{@x+1},#{@y}"
      @x += 1
    elsif @direction == '<'
      @x -=1
    else
      @y += 1
    end
  end

  def change_direction_at_intersection
    # if your next direction was R, then it will become L, etc
    if @next_direction.nil? || @next_direction == 'R'
      @next_direction = 'L'
    elsif @next_direction == 'L'
      @next_direction = 'S'
    elsif @next_direction == 'S'
      @next_direction = 'R'
    end    
    # If you were going up and your next direction is left, then you'll start going left, etc
    if @direction == '^'
      if @next_direction == 'L'
        @direction = '<'
      elsif @next_direction == 'R'
        @direction = '>'
      end  
    elsif @direction == '>'
      if @next_direction == 'L'
        @direction = '^'
      elsif @next_direction == 'R'
        @direction = 'v'
      end  
    elsif @direction == 'v'
      if @next_direction == 'L'
        @direction = '>'
      elsif @next_direction == 'R'
        @direction = '<'
      end  
    else # '<'
      if @next_direction == 'L'
        @direction = 'v'
      elsif @next_direction == 'R'
        @direction = '^'
      end  
    end
  end

  def change_direction_at_turn(turn)
    # puts "#{@direction} encountered a turn #{turn}"
    if @direction == '^'
      if turn == '\\'
        @direction = '<'
      elsif turn == '/'
        @direction = '>'
      end  
    elsif @direction == '>'
      if turn == '\\'
        @direction = 'v'
      elsif turn == '/'
        @direction = '^'
      end  
    elsif @direction == 'v'
      if turn == '\\'
        @direction = '>'
      elsif turn == '/'
        @direction = '<'
      end  
    elsif @direction == '<'
      if turn == '\\'
        @direction = '^'
      elsif turn == '/'
        @direction = 'v'
      end  
    end

    # puts "has become #{@direction}"
  end  

  def self.crashes?(carts)
    carts.each do |cart1|
      carts.each do |cart2|
        if cart1.x == cart2.x && cart1.y == cart2.y && cart1.id != cart2.id
          puts "THERE IS A COLLISION AT #{cart1.x}, #{cart1.y} between #{cart1.id} and #{cart2.id}"
          return true
        end
      end  
    end

    false
  end      

  def move(tracks, carts)
    next_track = get_next_track(tracks)
    move_ahead_one
    if next_track == '+'
      change_direction_at_intersection
    elsif next_track == "\\" || next_track == "/"
      change_direction_at_turn(next_track)
    end
  end
end

def generate_id
  o = [('a'..'z'), ('A'..'Z')].map(&:to_a).flatten
  (0...50).map { o[rand(o.length)] }.join
end  

carts = []
tracks = Array.new (150) { Array.new(150) }
file_lines.each_with_index do |line, y_index|
  characters = line.split('')
  characters.each_with_index do |character, x_index|
    if character == '<' || character == '>'
      carts << Cart.new(generate_id, character, x_index, y_index)
      character = '-'
    elsif character == '^' || character == 'v'
      carts << Cart.new(generate_id, character, x_index, y_index)
      character = '|'
    end
    tracks[y_index][x_index] = character
  end
end

def print_with_carts(tracks, carts)
  tracks_with_carts = []
  tracks_with_carts = tracks.dup
  carts.each do |cart|
    tracks_with_carts[cart.y][cart.x] = cart.direction
  end
  puts tracks_with_carts.map { |x| x.join('') }
end

def print_around_cart(tracks, carts, cart)
  tracks_with_carts = tracks.dup
  carts.each do |cart|
    tracks_with_carts[cart.y][cart.x] = cart.direction
  end

  x = cart.x - 5
  y = cart.y - 5
  # end_x = x + 10
  # end_y = y + 10

  puts "Map for cart #{cart.id}"
  around_cart = Array.new(10) { Array.new(10) }
  around_cart.each_with_index do |col, y_index|
    col.each_with_index do |row, x_index|
      unless tracks_with_carts[y][x].nil?
        around_cart[y_index][x_index] = tracks_with_carts[y][x]
        x += 1
      else
        around_cart[y_index][x_index] = ' '
      end  
    end
    y += 1
  end    

  puts around_cart.map { |x| x.join('') }
end

# puts tracks.map { |x| x.join('') }
# puts "\n\n\n"
print_with_carts(tracks, carts)

puts "# of carts #{carts.size}"
collision = false

turn = 1
  while !collision
    carts.each do |cart|
      cart.move(tracks, carts)
    end

    collision = Cart.crashes?(carts)

    puts "Turn #{turn}"

    break if collision 
    turn += 1 
  end

