require 'pry'

$num_recipes = 702831

recipes = []

elf1 = 0
elf2 = 1

recipes << 3
recipes << 7

$found_match = false

def print_recipes(elf1, elf2, recipes)
  recipes_dup = recipes.dup
  recipes_dup[elf1] = "(" + recipes_dup[elf1].to_s + ")"
  recipes_dup[elf2] = "[" + recipes_dup[elf2].to_s + "]"
  p recipes_dup
end

def get_next_elf_location(elf_location, recipes)
  current_recipe = recipes[elf_location]
  next_move = current_recipe + 1
  next_location = elf_location + next_move
  if next_location >= recipes.size
  	next_location =  next_location % recipes.size # if your next location is [8] for a recipes size 3 [0][1][2][3], really the location is [0]
  end
  next_location
end

def check_for_match(recipes)
  if recipes.size >= 6
    subrecipes = recipes[-6..recipes.size-1].map!(&:to_s).join('')
  end

  # puts "Looking for match between #{subrecipes} and #{$num_recipes}"

  $found_match = subrecipes == $num_recipes.to_s
end	

def calculate_elves_recipe_and_add(elf1, elf2, recipes)
  total_score = recipes[elf1] + recipes[elf2]
  new_recipe_scores = total_score.to_s.split('').map(&:to_i)
  recipes << new_recipe_scores[0]
  check_for_match(recipes)
  if new_recipe_scores.size > 1
    recipes << new_recipe_scores[1]
    check_for_match(recipes)
  end  
end	

subrecipes = recipes.map(&:to_s).join('')
until ($found_match)
  calculate_elves_recipe_and_add(elf1, elf2, recipes)
   
  elf1 = get_next_elf_location(elf1, recipes)
  elf2 = get_next_elf_location(elf2, recipes)
  # print_recipes(elf1, elf2, recipes)
end	
puts recipes.size - 6

puts recipes[-11..recipes.size-1].map!(&:to_s).join('')