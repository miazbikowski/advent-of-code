#!/usr/bin/env ruby
require 'pry'

requirements_lines = File.read('input7.txt').chomp.split("\n")

keys = ("A".."Z").to_a
requirements = {}
keys.each { |key| requirements[key] = [] }

puts requirements

requirements_lines.each do |line|
  line.match(/Step ([A-Z]) must be finished before step ([A-Z])/)
  requirements[$2] << $1
end

puts requirements

def get_next_step(requirements)
  steps_without_requirements = []
  requirements.each do |key, requirements_list|
    steps_without_requirements << key if requirements_list.size == 0
  end
  
  steps_without_requirements.sort[0]
end

def remove_step_requirements(step, requirements)
  requirements.each do |key, requirements_list|
    requirements_list.delete(step)
  end
end  


steps_list = []

while requirements.size != 0
  next_step = get_next_step(requirements)
  steps_list << next_step
  requirements.delete(next_step)
  remove_step_requirements(next_step, requirements)
end

puts steps_list.join('')