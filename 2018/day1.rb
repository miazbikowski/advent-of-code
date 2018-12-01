input = File.read('input1.txt')

frequency = 0
instructions = input.chomp.split("\n")

@cursor = 0

while @cursor < instructions.size
  frequency += instructions[@cursor].to_i
  @cursor += 1
end

puts frequency
