#!/usr/bin/env ruby
require_relative 'adventapi'

input = AdventApi::get_day(2,2018).lines

# part 1
x = input.map do |box_id|
  box_id.chars.map { |c| box_id.count c}
end

similar2 = x.count { |i| i.include? 2}
similar3 = x.count { |i| i.include? 3}
puts "part 1: #{similar2 * similar3}"

# part 2 - again: probably refactor it.

def charzip(x, y)
	x.chars.zip(y.chars)
end

def hamming(x, y)
  charzip(x, y).select{ |a,b| a!=b}.size
end


x, y = input.combination(2).find{|a,b| hamming(a,b)==1}
answer = charzip(x, y).select { |a,b| a===b}.map(&:first).join.chomp
puts "part 2: #{answer}"