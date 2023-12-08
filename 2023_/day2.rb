file_path = 'input2'

possible_games = []
File.open(file_path, "r") do |file|
    file.each_line do |line|
        match = line.match(/Game\s+(\d+):\s*(.+)$/i)

        if match
            game_id = match[1].to_i
            sets = match[2].split(/\s*;\s*/)
            
            puts "Game ID: #{game_id}"
            puts "Values: #{sets}"

            game_possible = true

            sets.each do |set|
                set.split(',').each do |color_pick| 
                    amount, color = color_pick.split(' ')
                    if (color == 'red' && amount.to_i >12) || (color == 'green' && amount.to_i > 13) || (color == 'blue' && amount.to_i > 14)
                        game_possible = false
                    end
                    #puts "There are #{amount} of #{color}"
                end
            end
        end

        possible_games << game_id if game_possible
    end

    puts "Possible games are #{possible_games}" 
    puts possible_games.sum
end

# part 2
game_totals = []
File.open(file_path, "r") do |file|
    file.each_line do |line|
        match = line.match(/Game\s+(\d+):\s*(.+)$/i)

        if match
            game_id = match[1].to_i
            sets = match[2].split(/\s*;\s*/)
            
            puts "Game ID: #{game_id}"
            puts "Values: #{sets}"
            game_mins = {
                'red' => 0,
                'blue' => 0,
                'green' => 0
            }

            sets.each do |set|
                set.split(',').each do |color_pick| 
                    amount, color = color_pick.split(' ')
                    game_mins[color] = amount.to_i if game_mins[color] < amount.to_i
                end
            end
        end

        game_totals << game_mins.values.reduce(:*)
    end

    puts "All game powers: #{game_totals.sum}"
end