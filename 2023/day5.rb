class RangedDestinations
    attr_accessor :source, :destination, :range
    def initialize(source, destination, range)
        @source = source.to_i
        @destination = destination.to_i
        @range = range.to_i
    end

    def in_range?(source)
        (@source..@source+@range).include?(source)
    end

    def get_destination(source) #use if in range
        @destination + source-@source
    end
end

class Map
    def initialize(title)
        @title = title
        @range_destinations = []
    end

    def add_range_destinations(source, destination, target)
        @range_destinations << RangedDestinations.new(source, destination, target)
    end

    def get_destination(source)
        @range_destinations.each do |range_dest|
            if range_dest.in_range?(source)
                return range_dest.get_destination(source)
            end
        end

        source
    end
end

#This should just set up all our maps
maps = []
seeds = []
File.open('input5', "r") do |file|
    current_map = nil
    file.each_line do |line|
        if line.include?('seeds:')
            seeds = line.scan(/\d+/).map(&:to_i)
        elsif line == "\n"
            maps << current_map unless current_map.nil?
        elsif line.include?('map') #title of map line
            map_title = line.split(' ')[0]
            current_map = Map.new(map_title)
        else # this should be a line with numbers
            dest, source, range = line.split(' ')
            current_map.add_range_destinations(source, dest, range)
        end
    end

    maps << current_map
end

# print "Seeds: #{seeds}"
# print maps

locations = []
seeds.each do |seed|
    current_num = seed
    maps.each do |map|
        current_num = map.get_destination(current_num)
    end
    locations << current_num
end

puts "Solution to part 1: #{locations.min}"

locations = []
pairs = seeds.each_slice(2).to_a

print pairs

pairs.each do |pair|
    start = pair[0]
    ends = start+pair[1]

    (start..ends).each do |seed|
        current_num = seed
        maps.each do |map|
            current_num = map.get_destination(current_num)
        end
        locations << current_num
    end
end

puts "Solution to part 2: #{locations.min}"