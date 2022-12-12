# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. 
# What is the sum of these six signal strengths?
# Maybe we can track where certain ops are at by using a 2d array or a hash
# Any ops in index 0 is ready to be pop'ed off and the registry updated

require 'pry-byebug'

$ongoing_ops = {
  '0' => [],
  '1' => []
}

file = File.open("input-10")
file_data = file.readlines

$register = 1
$cycle = 1
$signal_strengths = []
$crt = []
$current_crt_row = []

def update_ops_by_one_cycle(op=nil)
  puts "Register is at #{$register}"
  #puts "Sprite position: #{'.'*($register-1)}####{'.'*(40-2-$register)}"
  # any ops at index 0 pop off
  $ongoing_ops['0'].each do |op|
    amount = (op.split('')[5..].join('')).to_i
    $register += amount
    puts "finish executing #{op} (Register X is now #{$register})"
  end

  $ongoing_ops['0'] = $ongoing_ops['1']
  $ongoing_ops['1'] = []
  
  $ongoing_ops['1'] << op if op

  # part 1
  puts "Ending state for cycle #{$cycle}: #{$ongoing_ops}"
  if [20, 60, 100, 140, 180, 220].include?($cycle)
    puts "#{$cycle}*#{$register} = #{$cycle * $register}"
    $signal_strengths << $cycle * $register
  end

  # part 2
  if [41, 81, 121, 161, 201, 241].include?($cycle)
    $crt << $current_crt_row.dup.join('')
    $current_crt_row = []
  end

  # the current CRT row, we take from the sprite position at the current cycle index
  if ($cycle % 40)-1 == ($register-1) || ($cycle % 40)-1 == $register || ($cycle % 40)-1 == ($register+1)
    $current_crt_row << '#'
  else
    $current_crt_row << '.'
  end
  puts "Current CRT row: #{$current_crt_row}"
  $cycle +=1
end

file_data.each do |op|
  op.strip!
  puts op
  if op != 'noop'
    update_ops_by_one_cycle(op)
    update_ops_by_one_cycle
  else
    update_ops_by_one_cycle
  end
end

# Do an extra cycles to finish off instructions
update_ops_by_one_cycle
puts "Final register amount: #{$register}"
puts $signal_strengths.sum

puts $crt