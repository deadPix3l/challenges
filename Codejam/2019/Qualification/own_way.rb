#!/usr/bin/env ruby

ARGF.readline.to_i.times do |x|
  n = ARGF.readline.to_i
  puts "Case ##{x+1}: #{ARGF.readline.tr('SE','ES')}"
end
