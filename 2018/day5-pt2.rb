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

possible_polymers = [*?a..?z]
removal_count = {}

possible_polymers.each do |possible_polymer|
  polymers = original_polymers.dup
  polymers.delete(possible_polymer)
  polymers.delete(possible_polymer.upcase)
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

  removal_count[possible_polymer] = polymers.size
end

puts removal_count.sort_by {| key, value| value }

# puts polymers.join('')
# puts polymers.size    