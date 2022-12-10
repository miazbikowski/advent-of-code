require 'pry-byebug'
file = File.open("input-8")
file_data = file.readlines

trees = []

file_data.each do |line|
  tree_line = line.strip.split('')
  trees.append(tree_line)
end

def visible?(trees, tree, x, y)
  return true if(x == 0 || y == 0 || x == trees.length-1 || y == trees.length-1)
  size = trees.length
  temp_y = y.dup
  temp_x = x.dup

  visible_from_left, visible_from_right, visible_from_top, visible_from_below = true, true, true, true
  # check left
  while temp_y > 0
    temp_y -= 1
    if trees[x][temp_y] >= tree
      visible_from_left = false
      break
    end
  end

  temp_y = y.dup
  # check right
  while temp_y < size-1
    temp_y += 1
    if trees[x][temp_y] >= tree
      visible_from_right = false
      break
    end
  end

  # check top
  while temp_x > 0
    temp_x -= 1
    if trees[temp_x][y] >= tree
      visible_from_top = false
      break
    end
  end

  temp_x = x.dup
  # check below
  while temp_x < size-1
    temp_x += 1
    if trees[temp_x][y] >= tree
      visible_from_below = false 
      break
    end
  end

  if visible_from_left || visible_from_right || visible_from_top || visible_from_below
    return true
  else
    return false
  end
end

def get_scenic_score(trees, tree, x, y)
  size = trees.length
  temp_y = y.dup
  temp_x = x.dup

  seen_left, seen_right, seen_top, seen_below = 0,0,0,0
  # check left
  while temp_y > 0
    temp_y -= 1
    if trees[x][temp_y] == tree
      seen_left +=1
      break
    elsif trees[x][temp_y] > tree
      seen_left +=1
      break
    end

    seen_left+=1
  end

  temp_y = y.dup
  # check right
  while temp_y < size-1
    temp_y += 1
    if trees[x][temp_y] == tree
      seen_right +=1
      break
    elsif trees[x][temp_y] > tree
      seen_right +=1
      break
    end

    seen_right+=1
  end

  # check top
  while temp_x > 0
    temp_x -= 1
    
    if trees[temp_x][y] == tree
      seen_top +=1
      break
    elsif trees[temp_x][y] > tree
      seen_top +=1
      break
    end

    seen_top+=1
  end

  temp_x = x.dup
  # check below
  while temp_x < size-1
    temp_x += 1
    
    if trees[temp_x][y] == tree
      seen_below +=1
      break
    elsif trees[temp_x][y] > tree
      seen_below +=1
      break
    end

    seen_below+=1
  end

  seen_left*seen_right*seen_top*seen_below
end

scenic_scores = []
visible_count = 0
trees.each_with_index do |row, row_index|
  row.each_with_index do |tree, col_index|
    visible_count +=1 if visible?(trees, tree, row_index, col_index)
    scenic_scores << get_scenic_score(trees, tree, row_index, col_index)
  end
end

puts visible_count
puts scenic_scores.max