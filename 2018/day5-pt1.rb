#!/usr/bin/env ruby
require 'pry'

original_polymers = File.read('input5.txt').chomp.split('')

def opposing_polarity?(poly1, poly2)
  return true if (poly1 == poly1.downcase) && poly1.upcase == poly2
  return true if (poly2 == poly2.downcase) && poly2.upcase == poly1
  return true if (poly1 == poly1.upcase) && poly1.downcase == poly2
  return true if (poly2 == poly2.upcase) && poly2.downcase == poly1

  false
end  

check = 0
while check < polymers.size - 1
  if opposing_polarity?(polymers[check], polymers[check+1])
    # puts "Found opposing: #{polymers[check]} #{polymers[check+1]}"
    polymers.delete_at(check+1)
    polymers.delete_at(check)
    check -=1 unless check == 0
  else
    check +=1
  end
end

puts polymers.join('')
puts polymers.size    