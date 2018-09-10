#!/usr/bin/env ruby

prng = Random.new()
ARGF.readlines.each do |i|
   cnt,die = i.split('d').map { |x| x.to_i }
   y = (1..cnt).map { prng.rand(die)+1 }
   puts "#{cnt}d#{die} - #{y.inject(:+)}: #{y.join(' ')}"
end