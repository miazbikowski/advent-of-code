plants = "..##..##....#.#.####........##.#.#####.##..#.#..#.#...##.#####.###.##...#....##....#..###.#...#.#.#.#..".split('')

notes = File.read('input12.txt').chomp.split("\n")

puts plants.size
puts "Gen 0: #{plants.join('')}"

(1..20).to_a.each do |generation|
  will_become_plants = []
  will_become_plantless = []
  notes.each do |note|
    m = note.match /(\S\S\S\S\S) => (\S)/
    pattern = $1
    next_state = $2
    # puts "Match #{pattern}, Next state is #{next_state}"
    (0..plants.size - 5).to_a.each do |plant_index|
      five_plants = plants[plant_index..plant_index+4].join('')
      if five_plants == pattern
        # puts "Plants #{five_plants} at index #{plant_index} matches pattern #{pattern}"
        if next_state == '#'
          will_become_plants << plant_index + 2
        else
          will_become_plantless << plant_index + 2
        end    
      end
    end
  end

  puts "#{will_become_plants.size} spots will become plants: #{will_become_plants.join(', ')}"
  puts "#{will_become_plantless.size} spots will become dirt: #{will_become_plantless.join(', ')}"
  will_become_plants.each do |plant_index|
    plants[plant_index] = '#'
  end
  
  will_become_plantless.each do |plant_index|
    plants[plant_index] = '.'
  end

  puts "Gen #{generation}: #{plants.join('')}"
end

plants = plants[0..plants.size]
puts plants.join('')

sum = 0
plants.each_with_index do |plant, idx|
  sum += idx if plant == '#'
end

puts sum
