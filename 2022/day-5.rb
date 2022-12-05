"""
        [H]     [W] [B]            
    [D] [B]     [L] [G] [N]        
[P] [J] [T]     [M] [R] [D]        
[V] [F] [V]     [F] [Z] [B]     [C]
[Z] [V] [S]     [G] [H] [C] [Q] [R]
[W] [W] [L] [J] [B] [V] [P] [B] [Z]
[D] [S] [M] [S] [Z] [W] [J] [T] [G]
[T] [L] [Z] [R] [C] [Q] [V] [P] [H]
 1   2   3   4   5   6   7   8   9 
"""

stacks = {
  '1' => ['T', 'D', 'W', 'Z', 'V', 'P'],
  '2' => ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
  '3' => ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
  '4' => ['R', 'S', 'J'],
  '5' => ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
  '6' => ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
  '7' => ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
  '8' => ['P', 'T', 'B', 'Q'],
  '9' => ['H', 'G', 'Z', 'R', 'C']
}

Instruction = Struct.new(:quantity, :from, :to)
LOG_FORMAT = /move (\d+) from (\d+) to (\d+)/

def analyze_instruction(line)
  line.match(LOG_FORMAT) { |m| Instruction.new(*m.captures) }
end

file = File.open("input-5")
file_data = file.readlines

file_data.each do |line|
  instruction = analyze_instruction(line)
  instruction.quantity.to_i.times do
    stacks[instruction.to] << stacks[instruction.from].pop
  end
end

final = ''
stacks.each do |key, value|
  final << value.last
end

puts final

# part 2

stacks = {
  '1' => ['T', 'D', 'W', 'Z', 'V', 'P'],
  '2' => ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
  '3' => ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
  '4' => ['R', 'S', 'J'],
  '5' => ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
  '6' => ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
  '7' => ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
  '8' => ['P', 'T', 'B', 'Q'],
  '9' => ['H', 'G', 'Z', 'R', 'C']
}

file = File.open("input-5")
file_data = file.readlines

file_data.each do |line|
  instruction = analyze_instruction(line)
  stacks[instruction.to] << stacks[instruction.from].pop(instruction.quantity.to_i)
  stacks[instruction.to].flatten!
end

final = ''
stacks.each do |key, value|
  final << value.last
end

puts final

