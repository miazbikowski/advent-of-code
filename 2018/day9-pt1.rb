# 458 players; last marble is worth 71307 points

players = 458
player_scores = {}
(1..players).to_a.each { |key| player_scores[key] = 0 }

marbles = (2..7130700).to_a
board = [0, 1]
current_marble = 1

player_index = 3

marbles.each do |marble|
  if marble % 23 == 0
    # going counter-clockwise
    # handle going over left edge
    marble_to_be_removed = current_marble - 7

    # puts "marble_to_be_removed #{marble_to_be_removed} and board size is #{board.size}"
    if marble_to_be_removed < 0
      remove_at = board.size + (marble_to_be_removed) # ie board size 20 - marble_to_be_removed (-3) then you remove then marble at 17?
    else
      remove_at = marble_to_be_removed
    end    

    # puts "remove_at is #{remove_at} and board size is #{board.size}"
    player_scores[player_index] += (marble + board.slice!(remove_at))
    current_marble = remove_at
  else
    # going clock-wise
    # if current marble is on the edge, you start back at the beginning
    if current_marble == board.size - 1
      position = 1
    else
      position = current_marble + 2
    end  

    board.insert(position, marble)
    current_marble = position
  end

  # change player 
  if player_index < players
    player_index +=1
  else
    player_index = 1  
  end

  if marble < 100
    print_board = board.map(&:to_s)
    print_board[current_marble] += '*'
    puts "#{marble}: " + print_board.join(" ")
  end
end

puts player_scores.sort_by { |key, value| value }