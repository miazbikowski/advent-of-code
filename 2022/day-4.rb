require 'pry-byebug'

file = File.open("input-4")
file_data = file.readlines

overlaps_count = 0
file_data.each do |line|
	assignments = line.strip!.split(",")
	assignment1 = assignments[0].split("-").map(&:to_i)
	assignment2 = assignments[1].split("-").map(&:to_i)
	range1 = (assignment1[0]..assignment1[1])
	range2 = (assignment2[0]..assignment2[1])
	if range1.cover?(range2) || range2.cover?(range1)
		overlaps_count +=1 
	end
end

puts overlaps_count

# Part 2: any overlap at all
def ranges_overlap?(range_a, range_b)
  range_b.begin <= range_a.end && range_a.begin <= range_b.end 
end 

file = File.open("input-4")
file_data = file.readlines

overlaps_count = 0
file_data.each do |line|
	assignments = line.strip!.split(",")
	assignment1 = assignments[0].split("-").map(&:to_i)
	assignment2 = assignments[1].split("-").map(&:to_i)
	range1 = (assignment1[0]..assignment1[1])
	range2 = (assignment2[0]..assignment2[1])
	if ranges_overlap?(range1, range2)
		overlaps_count +=1 
	end
end

puts overlaps_count