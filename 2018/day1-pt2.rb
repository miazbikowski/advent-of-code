input = File.read('input1.txt')

frequency = 0
previous_frequencies = [0]
instructions = input.chomp.split("\n")

@cursor = 0

while @cursor < instructions.size
  frequency += instructions[@cursor].to_i

  break if previous_frequencies.include?(frequency)

  previous_frequencies << frequency
  @cursor += 1
end

puts frequency