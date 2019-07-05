#!/usr/bin/env ruby

# This code is just bad. but it works. will fix later.
# cant use AdventApi because it's unsorted.
# download the input and run GNU sort.

currentGuard = nil
fellAsleep = nil
guards = Hash.new { |h,k| h[k]=[] }

File.open("day4.sorted").each do |line|
  time, action = line.sub("Guard","").tr('[]','').split(' ')[1..2]
  time = time.split(':')[1].to_i
  case action
  when /\#(\d+)/
    currentGuard = $1.to_i
  when /falls/
    fellAsleep = time
  when /wakes/
    guards[currentGuard] << [fellAsleep, time]
  end
end

y = guards.transform_values do |v|
  v.map { |a,b| b-a}.sum
end.max_by{|k,v| v}

guardMostAsleep = y[0]
mostAsleepTimes = guards[guardMostAsleep]
blah = {}
(0..59).each {|t| blah[t] = mostAsleepTimes.count {|a,b| a<=t and t<b}}

minute = blah.max_by{|k,v| v}[0]
p1Answer = minute.to_i * guardMostAsleep.to_i
puts "part 1: #{p1Answer} (#{minute} * #{guardMostAsleep})"
