require 'pry'

class WholeFabric
  def initialize
    input = File.read('input3.txt')
    lines = input.chomp.split("\n")

    @fabric = Array.new(2000) { Array.new(2000, 0) }

  	cursor = 0

  	while cursor < lines.size
      request = generate_request(lines[cursor])
      add_request_to_fabric(request)
      cursor += 1
  	end
  end

  def generate_request(line)
    tokens = line.split(" ")
    id = tokens[0]
    from_left = tokens[2].split(',')[0]
    from_top = tokens[2].split(',')[1]
    width = tokens[3].split('x')[0]
    height = tokens[3].split('x')[1]

    FabricPieceRequest.new(id, from_left, from_top, width, height)
  end

  def add_request_to_fabric(request)
    left_index = request.from_left
    end_left = request.from_left + request.width

    while left_index <= end_left
      top_index = request.from_top
      end_top = request.from_top + request.height
      while top_index <= end_top
        @fabric[left_index][top_index] += 1
        top_index += 1
      end
      # binding.pry
      left_index += 1
    end
  end

  def more_than_one_request_count
    count = 0
    @fabric[0...1999].each do |sub_array|
      sub_array[0...1999].each do |item|
        if item > 1
          count +=1
        end
      end
    end

    count      
  end  

  class FabricPieceRequest
    attr_accessor :id, :from_left, :from_top, :width, :height
  	
    def initialize(id, from_left, from_top, width, height)
      @id = id
      @from_left = from_left.to_i
      @from_top = from_top.to_i
      @width = width.to_i
      @height = height.to_i
  	end
  end	
end

fabric = WholeFabric.new
puts fabric.more_than_one_request_count