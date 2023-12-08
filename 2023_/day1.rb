file_path = "input1"
sum = 0
File.open(file_path, "r") do |file|
    file.each_line do |line|
        integers = line.scan(/\d/).map(&:to_i)
        if integers.any?
            puts "#{integers.first}#{integers.last}"
            sum += "#{integers.first}#{integers.last}".to_i
        else
            puts "No integers found in the string."
        end
    end
end

puts "Part 1: #{sum}"

# part 2

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

file_path = "input1"
sum = 0
File.open(file_path, "r") do |file|
    file.each_line do |line|
        integers = line.scan(/(?=([1-9]|one|two|three|four|five|six|seven|eight|nine|\d+))/i).flatten
        if integers.any?
            first =  integers.first.length > 1 ? nums.find_index(integers.first)+1 : integers.first.to_i
            last = integers.last.length > 1 ? nums.find_index(integers.last)+1 : integers.last.to_i
            puts "#{line} is #{first}#{last}"
            sum += "#{first}#{last}".to_i
        end
    end
end

puts "Part 2: #{sum}"
