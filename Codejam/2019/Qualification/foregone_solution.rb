#!/usr/bin/env ruby
T = ARGF.readline
lines = ARGF.readlines

lines.each_with_index do |n,i|
  a = n.tr('4','3').to_i
  b = n.tr('123456789','00010').to_i
  puts "Case ##{i+1}: #{a} #{b}" 
end
