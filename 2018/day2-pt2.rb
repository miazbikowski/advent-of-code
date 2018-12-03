class Counter
  @counts_of_2s = []
  @counts_of_3s = []

  def self.count_for_twos(counts, line)
    counts.each do |key, count|
      if count == 2
        @counts_of_2s << line
        return
      end
    end
  end         

  def self.count_for_threes(counts, line)
    counts.each do |key, count|
      if count == 3
        @counts_of_3s << line
        return
      end
    end
  end

  def self.get_final_checksum
    @counts_of_2s.size * @counts_of_3s.size
  end

  def self.get_ids_seperated_by_one
    all_ids = @counts_of_2s.concat @counts_of_3s

    all_ids.each_with_index do |id, index|
      compare_index = index + 1
      while compare_index < all_ids.size
        count = count_same_characters(id, all_ids[compare_index])
        return puts id, all_ids[compare_index] if count == 1
        compare_index +=1
      end  
    end
  end

  def self.count_same_characters(s1, s2)
    count = 0
    # puts "comparing #{s1} and #{s2}"
    s1.split('').each_with_index do |char, index|
      count +=1 if s2.split('')[index] != char
      return count if count > 1
    end

    # puts "count: #{count}"
    count
  end
end

input = File.read('input2.txt')

lines = input.chomp.split("\n")

@cursor = 0

while @cursor < lines.size
  counts = {}
  line = lines[@cursor]

  line.split('').each do |character|
  	if counts.key?(character)
  	  counts[character] += 1
  	else
  	  counts[character] = 1
  	end
  end

  Counter.count_for_twos(counts, line)
  Counter.count_for_threes(counts, line)
  	
  @cursor += 1
end

puts Counter.get_final_checksum

puts Counter.get_ids_seperated_by_one


# class File
#   def self.read
#   	...
#   	return File.new(stuff_it_read)
#   end
  
#   def chomp
#     # read all the things from the instance
#     return "any kind of thing \nyou wanna balbalba" --> ["any kind of thing", "you wanna blablabla"]
#   end	
# end

