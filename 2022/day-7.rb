$total_under_100000 = 0
$directories_big_enough = []
$space_needed = nil

class Tree
  attr_accessor :root
end

class Directory
  attr_accessor :files, :directories, :parent_directory, :name

  def initialize(name)
    @name = name
    @files = []
    @directories = []
    @parent_directory = nil
  end

  def files_size
    @files.sum { |file| file.size}
  end

  def directories_size
    @directories.sum { |directory| directory.size }
  end

  def size
    total_size = files_size + directories_size
    # for part 1
    if total_size <= 100000
      $total_under_100000 += total_size
    end

    # for part 2
    if $space_needed && total_size >= $space_needed
      $directories_big_enough << total_size
    end

    total_size
  end
end

class File_
  attr_accessor :size
  def initialize(size)
    @size = size
  end
end

file = File.open("input-7")
file_data = file.readlines

tree = Tree.new
current_dir = nil
file_data.each do |line|
  line.strip!
  case line
  when /cd \//
    home_dir = Directory.new('home')
    tree.root = home_dir
    current_dir = home_dir
  when /cd [a-zA-Z]+/
    new_dir = Directory.new(line)
    current_dir.directories << new_dir
    new_dir.parent_directory = current_dir
    current_dir = new_dir  
  when /cd ../
    current_dir = current_dir.parent_directory
  when /ls\z/
    # no-op
  when /dir [a-zA-Z]+/
    # no-op
  when /[0-9]+ .+/
    file_size = line.scan(/\d/).join('').to_i
    current_dir.files << File_.new(file_size)
  else
    puts "Something went wrong"
  end
end

# part 1
puts tree.root.size
puts $total_under_100000

# part 2
$space_needed = 30000000 - (70000000 - tree.root.size)
puts "Space needed: #{$space_needed}"
tree.root.size
puts "Directory to delete: #{$directories_big_enough.min}"
