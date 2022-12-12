# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. 
# What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
require 'pry-byebug'

class Monkey
  attr_accessor :id, :items, :op_type, :op_amount, :test_num, :true_monkey, :false_monkey, :inspection_count

  def initialize(id)
    @id = id
    @inspection_count = 0
  end
end

monkeys = {}

# initialize the monkeys / starting state
file = File.open("input-11")
file_data = file.readlines

current_monkey = nil
file_data.each_with_index do |line, index|
  puts line
  if index == 0 || index % 7 == 0
    #puts "Start new monkey"
    id = line[/Monkey ([^:]*)/,1]
    monkeys[id.to_s] = Monkey.new(id)
    current_monkey = id.to_s
  elsif index == 1 || index % 7 == 1
    #puts "Set items"
    items = line[/\s\sStarting items: (.*)/,1].split(', ')
    monkeys[current_monkey].items = items
  elsif index == 2 || index % 7 == 2
    #puts "Set operation"
    # Operation: new = old * 19
    monkeys[current_monkey].op_type = line[/\s\sOperation: new = old (.) (.*)/,1]
    monkeys[current_monkey].op_amount = line[/\s\sOperation: new = old (.) (.*)/,2]
  elsif index == 3 || index % 7 == 3
    # Test: divisible by 23
    monkeys[current_monkey].test_num = line[/\s\sTest: divisible by (\d*)/,1]
  elsif index == 4 || index % 7 == 4
    # If true: throw to monkey 2
    monkeys[current_monkey].true_monkey = line[/\s\s\s\sIf true: throw to monkey (\d*)/,1]
  elsif index == 5 || index % 7 == 5
    # If false: throw to monkey 3
    monkeys[current_monkey].false_monkey = line[/\s\s\s\sIf false: throw to monkey (\d*)/,1]
  end
end

puts monkeys

# And now for rounds
def do_round(monkeys)
  monkeys.each do |id, monkey|
    puts "Monkey #{id}:"
      # inspect an item
      while !monkey.items.empty?
        item = monkey.items.delete_at(0)
        monkey.inspection_count += 1
        puts "\s\sMonkey inspects an item with a worry level of #{item}."
        old = item.dup.to_i
        worry_level_string = "#{old}#{monkey.op_type}#{monkey.op_amount}"
        worry_level = eval(worry_level_string)
        puts "Worry level is #{monkey.op_type} by #{monkey.op_amount} to #{worry_level}."
        worry_level = (worry_level / 3).to_i
        puts "Monkey gets bored with item. Worry level is divided by 3 to #{worry_level}."
        if worry_level % monkey.test_num.to_i == 0
          puts "Current worry level is divisible by #{monkey.test_num}."
          puts "Item with worry level #{worry_level} is thrown to monkey #{monkey.true_monkey}."
          monkeys[monkey.true_monkey].items << worry_level
        else
          puts "Current worry level not is divisible by #{monkey.test_num}."
          puts "Item with worry level #{worry_level} is thrown to monkey #{monkey.false_monkey}."
          monkeys[monkey.false_monkey].items << worry_level
        end
      end
    end
end

20.times do
  do_round(monkeys)
end

puts monkeys

monkeys.each do |id, monkey|
  puts "Monkey #{id} inspected items #{monkey.inspection_count} times"
end