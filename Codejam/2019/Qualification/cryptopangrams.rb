#!/usr/bin/env ruby
require 'prime'

class Array
  def ljust; fill(1,length...2) end
end

T = ARGF.readline.to_i

i = 1
T.times do |time_cnt|
  n,line = ARGF.readline.split(' ')
  l = ARGF.readline
  a = l.split(' ').map {|i| i.to_i.prime_division.map{|x,y| x}.ljust}
  b = a.flatten.uniq.sort.zip(('A'..'Z')).to_h
  a.map! {|x,y| [b[x],b[y]]}
  c = a.each_cons(2).to_a.reverse.map{|x,y| y.include?(x[0]) ? x[1] : x[0]}.reverse + a.last
  puts "Case ##{i}: #{c.join}" 
  i+=1
end
