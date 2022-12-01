file = File.open("input-1")
file_data = file.readlines

third_max_calories = 0
second_max_calories = 0
max_calories = 0
single_elf_calories = 0

file_data.each do |line|
  if line == "\n"
    if max_calories < single_elf_calories
      third_max_calories = second_max_calories
      second_max_calories = max_calories
      max_calories = single_elf_calories
    elsif single_elf_calories > second_max_calories
      third_max_calories = second_max_calories
      second_max_calories = single_elf_calories
    elsif single_elf_calories > third_max_calories
      third_max_calories = single_elf_calories
    end

    single_elf_calories = 0
  else
    calories = line.to_i
    single_elf_calories += calories
  end
end

puts third_max_calories
puts second_max_calories
puts max_calories

total = third_max_calories + second_max_calories + max_calories

puts "total: #{total}"
