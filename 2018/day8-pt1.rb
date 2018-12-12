require 'pry'

inputs = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ').map(&:to_i)
# inputs = File.read('input8.txt').chomp.split(" ").map(&:to_i)

class Tree
  $total_metadata = 0

  def generate_nodes(inputs)
    root_node = Node.new(inputs)
    puts root_node.value
  end  

  class Node
    attr_accessor :num_children, :num_metadata, :children, :metadata, :value

    def initialize(inputs)
      @num_children = inputs.slice!(0)
      @num_metadata = inputs.slice!(0)
      @children = []
      @metadata = nil
      @value = 0
      get_children_then_set_metadata(inputs)
    end

    def set_value
      @value = 0
      if @num_children == 0
        @value += @metadata.inject(0, &:+)
        puts "I have no children and have a value of #{@value}"
      else
        @metadata.each do |metadata|
          unless @children[metadata-1].nil?
            child_value = @children[metadata-1].set_value
            puts "Child at #{metadata} has a value of #{child_value}"
            @value += child_value
          end
        end
      end

      puts "Value for this node is: #{@value}"
      @value
    end  

    def get_children_then_set_metadata(inputs)
      idx = 0
      puts "num children #{@num_children}"
      while idx < @num_children
        children << Node.new(inputs)
        idx += 1
      end

      puts "num metadata #{@num_metadata}"
      start = 0
      stop = @num_metadata - 1
      if @num_metadata > 1
        @metadata = inputs.slice!(start..stop)
      else
        @metadata = [inputs.slice!(start)]
      end

      # PART 2
      set_value  

      # PART 1
      # puts "metadata: #{@metadata}"
      # $total_metadata += @metadata.inject(0, &:+)
      # puts "total_metadata #{$total_metadata}"
    end  
  end
end  

tree = Tree.new
tree.generate_nodes(inputs)
