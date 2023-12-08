# Strategy: what if, as we go through the 2d array, we create number nodes and give location values we can check against when we encounter a symbol?

class NumberLocation
    attr_accessor :x_start, :x_end, :y

    def initialize(x_start, y)
        @x_start = x_start
        @x_end = x_start
        @y = y
    end
end

class Number
    attr_accessor :value, :location, :touches_symbol
    def initialize(value, location)
        @value = value
        @location = location
        @touches_symbol = false
    end

    def add_to_value(char)
        @value += char
    end

    def get_integer_value
        @value.to_i
    end

    def update_location(x_index)
        @location.x_end = x_index
    end

    def touches_symbol?(symbol_x, symbol_y)
        # if you're within +1 or -1 of y
        # and -1 of x_start to +1 of x_end
        if (symbol_x >= @location.x_start-1 &&  symbol_x <= @location.x_end+1) && (symbol_y >= @location.y-1 && symbol_y <= @location.y+1)
            true
        else
            false
        end
    end
end

# We can go through the 2d array once to initialize all our Numbers, then go through again to check for symbol touching
file_path = 'input3'

numbers = []
File.open(file_path, "r") do |file|
    file.each_line.with_index do |line, y_index|
        print "Reading line: #{line}"
        started_number = nil
        line.chars.each_with_index do |char, x_index|
            if Integer(char, exception: false)
                if started_number.nil?
                    location = NumberLocation.new(x_index, y_index) #when you first initialize, x_start and x_end will be the same
                    started_number = Number.new(char, location)
                else #update started number value and x_end
                    started_number.add_to_value(char)
                    started_number.update_location(x_index)
                end
            else # was not an integer, 'close' started_number if there is one
                if started_number
                    numbers << started_number.dup
                    puts "Added number #{started_number.value}"
                    started_number = nil
                end
            end
        end
        # line ended, 'close' started_number
        numbers << started_number.dup if started_number
        puts "Added number #{started_number.value}" if started_number
    end
end

print numbers

symbols_to_check = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', '<', '>', '/', '?', '~']
File.open(file_path, "r") do |file|
    file.each_line.with_index do |line, y_index|
        print "Reading line: #{line}"
        started_number = nil
        line.chars.each_with_index do |char, x_index|
            if symbols_to_check.include?(char) # we found a symbol, now we need to check if it touches any of the numbers
                numbers.each do |number|
                    if number.touches_symbol?(x_index, y_index)
                        puts "The symbol at #{x_index}, #{y_index} touches #{number.value}"
                        number.touches_symbol = true
                    end
                end
            end
        end
    end
end

#puts numbers.filter { |num| num.touches_symbol }.map(&:value)
total =  numbers.filter { |num| num.touches_symbol }.map(&:value).map(&:to_i).sum
puts "And the grand total is #{total}"