#!/usr/bin/env ruby

prng = Random.new()
ARGF.readlines.each do |i|
   cnt,die = i.split('d').map { |x| x.to_i }
   puts (1..cnt).map { prng.rand(die)+1 }.inject(:+)
end