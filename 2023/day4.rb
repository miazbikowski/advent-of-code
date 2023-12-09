points = 0
File.open('input4', "r") do |file|
    file.each_line do |line|
        # in part 1 at least, we don't care about the game id, so we should just remove this part
        game_points = 0
        numbers = line.sub(/[^:]+:/, "")
        numbers = numbers.split('|')
        winning_numbers = numbers[0].split(' ')
        player_numbers = numbers[1].split(' ')

        val = (player_numbers & winning_numbers).size
        game_points = 2**(val-1) if val > 0

        points += game_points
    end
end

puts "Solution to part 1: #{points}"

# Part 2
# So when you start a new line, you should already know how many copies of this line you'll have
# since it's a tabulation of previous games
# We'll need to keep a count for each game
# We need to precalculate how many points each card gives
# Sounds like this is NOT round-robin, it ends where the cards end

# Step 1, we initialize our count
all_cards = {}
card_counts = {}
File.open('input4', "r") do |file|
    file.each_line.with_index do |line, index| # to easily have the game #
        card_counts[index] = card_counts.fetch(index, 0) + 1

        game_points = 0
        numbers = line.sub(/[^:]+:/, "")
        numbers = numbers.split('|')
        winning_numbers = numbers[0].split(' ')
        player_numbers = numbers[1].split(' ')

        val = (player_numbers & winning_numbers).size
        game_points = 2**(val-1) if val > 0

        (0..val-1).each do |j|
            # this is the money shot, adding however many copies you have of the current card to the
            # other cards, this is where this is efficient
            card_counts[index+1+j] = card_counts.fetch(index+1+j, 0) + card_counts.fetch(index, 0)
        end
    end
end

print card_counts.values.sum

