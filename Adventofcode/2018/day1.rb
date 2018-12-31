#!/usr/bin/env ruby
require_relative 'adventapi'

input = AdventApi::get_day(1,2018).lines.map(&:to_i)

# part 1
puts input.inject(:+)

# part 2 - refactor maybe later? but it does work.
x = 0
seen = [0]
while seen.uniq == seen
	input.each do |i|
		x += i
		if seen.include? x
			seen << x
			break
		end
		
		seen << x
	end
end

puts x