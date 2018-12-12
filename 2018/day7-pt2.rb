#!/usr/bin/env ruby
require 'pry'

requirements_lines = File.read('input7.txt').chomp.split("\n")

keys = ("A".."Z").to_a
requirements = {}
keys.each { |key| requirements[key] = [] }

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

class Job
  attr_accessor :letter, :duration, :time_left

  def initialize(letter)
    @letter = letter
    @duration = letter.ord - 4
    @time_left = @duration
  end

  def decrease_time_left
    @time_left -= 1
  end

  def done?
    @time_left == 0
  end  
end

class Worker
  attr_accessor :id, :working_on

  def initialize
    @working_on = nil
  end
  
  def finish
    @working_on = nil
  end

  def busy?
    !@working_on.nil?
  end  
end  

current_second = 0
workers = [Worker.new, Worker.new, Worker.new, Worker.new, Worker.new]
while keys.size != 0
  current_second += 1
  workers.each_with_index do |worker, idx|
    unless worker.busy?
      next_step = get_next_step(requirements)
      next if next_step.nil?
      worker.working_on = Job.new(next_step)
      puts "At second #{current_second} Worker #{idx} started work on step #{worker.working_on.letter} which will take #{worker.working_on.duration} seconds"
      requirements.delete(worker.working_on.letter)
    end

    if !worker.working_on.nil? && worker.working_on.done?
      puts "At second #{current_second} Worker #{idx} finished working on #{worker.working_on.letter}"
      remove_step_requirements(worker.working_on.letter, requirements)
      keys.delete(worker.working_on.letter)
      worker.working_on = nil
    end

    worker.working_on.decrease_time_left if !worker.working_on.nil?
  end
end

puts current_second


# steps_list = []

# while requirements.size != 0
#   next_step = get_next_step(requirements)
#   steps_list << next_step
#   requirements.delete(next_step)
#   remove_step_requirements(next_step, requirements)
# end

# puts steps_list.join('')