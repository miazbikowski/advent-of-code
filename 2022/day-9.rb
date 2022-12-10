# We can represent and track everything as X,Y coordinates
# Any time the Head is not within 1 X or Y, the tail must update its own coordinates
# Note that it would step in the same direction as the H
# We track a set of all tail coordinates

#initial state: H is 0,0 and T is 0,0 -- (X, Y)

require 'pry-byebug'

$tail_movements = []

def touching?(head, tail)
  return true if (head[0]-tail[0]).abs <= 1 && (head[1]-tail[1]).abs <= 1
  false
end

def diagonal?(head, tail)
  return true if head[0] != tail[0] && head[1] != tail[1]
  false
end

def make_tail_follow(tail, direction)
  # if they're diagonal, it will realign
  case direction
  when 'L'
    tail[0] -= 1
  when 'R'
    tail[0] += 1
  when 'U'
    tail[1] += 1
  when 'D'
    tail[1] -= 1
  end
end

head = [0,0]
tail = [0,0]

file = File.open("input-9")
file_data = file.readlines
previous_direction = nil

file_data.each do |instructions|
  tail_moved = false
  puts instructions
  direction, steps = instructions.split(' ')
  steps = steps.to_i

  steps.times do 
    case direction
    when 'L'
      head[0] -= 1
    when 'R'
      head[0] += 1
    when 'U'
      head[1] += 1
    when 'D'
      head[1] -= 1
    end
    puts "Head moved to #{head[0]}, #{head[1]}"

    # if instructions.strip == 'L 3'
    #   binding.pry
    # end

    unless touching?(head, tail)
      if diagonal?(head, tail) 
        puts "Found diagonal"
        make_tail_follow(tail, previous_direction)
      end
      make_tail_follow(tail, direction)
      tail_moved = true
    end
    
    
    if tail_moved
      puts "Tail is now at #{tail[0]}, #{tail[1]}"
      $tail_movements << tail.dup
    end
  end

  previous_direction = direction
end

puts $tail_movements.uniq.count + 1

#6403 is too high
# 6397 is too high
