#!/usr/bin/env ruby
# gem 'activesupport'
require 'active_support/core_ext/numeric/time.rb'
require 'pry'

data = File.read('input4.txt').chomp.split("\n")
data.map! { |d| d.match(/\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] (.+)/) }

entries = []

class ScheduleEntry
  attr_accessor :time, :action, :minute
  def initialize(year, month, day, hour, minute, action)
    @time = Time.new(year, month, day, hour, minute)
    @minute = minute
    @action = action
  end

  def self.minutes_asleep_list(start_time, end_time)
    current_time = start_time
    minutes_list = []
    while current_time < end_time
      minutes_list << current_time.min
      current_time += 1.minute
    end

    minutes_list
  end  
end  

data.map(&:to_a).each do |_, year, month, day, hour, minute, action|
  entries << ScheduleEntry.new(year, month, day, hour, minute, action)
end

entries.sort_by! {|obj| obj.time}

guards_sleep_counters = {}
minutes_asleep_counters = {}

id = nil
sleep_start = nil

entries.each do |entry|
  if entry.action.include?('#')
    m = entry.action.match(/(?<id>\d+)/)
    id = m[:id]
  elsif entry.action.include?('falls asleep')
    sleep_start = entry.time
  else
    minutes_asleep = (entry.time - sleep_start) / 60
    counter = guards_sleep_counters.fetch(id, 0)
    total = counter + minutes_asleep
    guards_sleep_counters[id] = total

    minutes_list = ScheduleEntry.minutes_asleep_list(sleep_start, entry.time)
    
    minutes_asleep_counters[id] = {} unless minutes_asleep_counters.has_key?(id)

    minutes_list.each do |minute|
      if minutes_asleep_counters[id].has_key?(minute)
        minutes_asleep_counters[id][minute] += 1
      else
        minutes_asleep_counters[id][minute] = 1
      end    
    end  
  end 
end

top_guard_id = guards_sleep_counters.sort_by {|_key, value| value}.last[0]
puts top_guard_id
top_minute = minutes_asleep_counters[top_guard_id].sort_by {|_key, value| value}.last[0]
puts top_minute
puts "total is:"
puts top_guard_id.to_i * top_minute.to_i
