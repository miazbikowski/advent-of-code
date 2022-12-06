data = File.open("input-6").read

index = 0
length = 4
while index+length < data.length
  four_chars = data[index..index+length-1]
  if four_chars.count(four_chars[0]) == 1 && four_chars.count(four_chars[1]) == 1 && four_chars.count(four_chars[2]) == 1 && four_chars.count(four_chars[3]) == 1
    break
  else
    index += 1
  end
end

puts index + length   

# part 2, we'll need to refine this shit and use detect

index = 0
length = 14
while index+length < data.length
  four_chars = data[index..index+length-1].split('')
  if four_chars.detect{ |e| four_chars.count(e) > 1 }
    index += 1
  else
    break
  end
end

puts index + length   