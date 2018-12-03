class Counter
  @counts_of_2s = 0
  @counts_of_3s = 0

  def self.count_for_twos(counts)
    counts.each do |key, count|
      if count == 2
        @counts_of_2s += 1
        return
      end
    end
  end         

  def self.count_for_threes(counts)
    counts.each do |key, count|
      if count == 3
        @counts_of_3s += 1
        return
      end
    end
  end

  def self.get_final_checksum
    @counts_of_2s * @counts_of_3s
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

  Counter.count_for_twos(counts)
  Counter.count_for_threes(counts)
  	
  @cursor += 1
end

puts Counter.get_final_checksum



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

