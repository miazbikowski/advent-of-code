file = File.open("input-3")
file_data = file.readlines

def get_middle_index(array)
  # may cause a bug, need to check if we need to round up
	(array.length / 2).to_i
end

def split_line(line)
  middle_index = get_middle_index(line)
  bag1 = line[0..middle_index-1]
  bag2 = line[middle_index..-1]

  [bag1, bag2]
end

def find_common_item(bag1, bag2)
  bag1.chars & bag2.chars
end

common_items = []
file_data.each do |line|
  bags = split_line(line)
  common_items << find_common_item(bags[0], bags[1])[0]
end

def get_priority(letter)
  lowercase = ("a".."z").to_a
  uppercase = ("A".."Z").to_a

  priority = lowercase.index(letter)

  if priority == nil
    priority = uppercase.index(letter) + 26
  end

  priority + 1
end

total_priority = 0
common_items.each do |item|
  total_priority += get_priority(item)
end  

puts "Total priority: #{total_priority}"

# part 2
def find_common_item_v2(bag1, bag2, bag3)
  bag1.chars & bag2.chars & bag3.chars
end

common_items = []
index = 0
while(index < file_data.length)
  bag1 = file_data[index]
  bag2 = file_data[index+1]
  bag3 = file_data[index+2]
  common_items << find_common_item_v2(bag1, bag2, bag3)[0]
  index += 3
end

total_priority = 0
common_items.each do |item|
  total_priority += get_priority(item)
end  

puts "Total priority: #{total_priority}"