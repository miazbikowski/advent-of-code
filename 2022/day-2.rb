# Day 2 and I am definitely not golfing

file = File.open("input-2")
file_data = file.readlines

$SELECTION_POINTS = {
	'X': 1,
	'Y': 2,
	'Z': 3
}

TIE_POINTS = 3
WIN_POINTS = 6

ENEMY_ROCK = 'A'
ENEMY_PAPER = 'B'
ENEMY_SCISSOR = 'C'

MY_ROCK = 'X'
MY_PAPER = 'Y'
MY_SCISSOR = 'Z'

$MATCHES = {
  'A': 'X',
  'B': 'Y',
  'C': 'Z'
}

$total_points = 0

def single_round(enemy_choice, my_choice)
	if $MATCHES[enemy_choice.to_sym] == my_choice
		$total_points += TIE_POINTS
  elsif (enemy_choice == ENEMY_ROCK && my_choice == MY_PAPER) || (enemy_choice == ENEMY_PAPER && my_choice == MY_SCISSOR) || (enemy_choice == ENEMY_SCISSOR && my_choice == MY_ROCK)
    $total_points += WIN_POINTS
  end

  $total_points += $SELECTION_POINTS[my_choice.to_sym]
end

file_data.each do |line|
  inputs = line.split(' ')
  single_round(inputs[0], inputs[1])
end

puts $total_points

# part 2 - could definitely use refactor but meh

$total_points = 0

def single_round_2(enemy_choice, round_result)
  if round_result == 'X' # LOSE
    case enemy_choice
    when ENEMY_PAPER
      my_choice = MY_ROCK
    when ENEMY_ROCK
      my_choice = MY_SCISSOR
    when ENEMY_SCISSOR
      my_choice = MY_PAPER
    end
  elsif round_result == 'Y' # DRAW
    my_choice = $MATCHES[enemy_choice.to_sym]
    $total_points += TIE_POINTS
  else # WIN
    case enemy_choice
    when ENEMY_PAPER
      my_choice = MY_SCISSOR
    when ENEMY_ROCK
      my_choice = MY_PAPER
    when ENEMY_SCISSOR
      my_choice = MY_ROCK
    end
    $total_points += WIN_POINTS
  end

  $total_points += $SELECTION_POINTS[my_choice.to_sym]
end

file_data.each do |line|
  inputs = line.split(' ')
  single_round_2(inputs[0], inputs[1])
end

puts $total_points

