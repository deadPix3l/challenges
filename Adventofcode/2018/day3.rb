#!/usr/bin/env ruby
require_relative 'adventapi'

class Fabric
  attr_reader :spaces, :claims
  def initialize
    @spaces = Hash.new()
    @claims = Array.new()
  end

  def add_area area
    # sx -> start x; ly -> length y
    id, sx, sy, lx, ly = area.tr('^0-9',' ').split[0..4].map(&:to_i)
    @claims << id
    (sx...sx+lx).each do |cx|
      (sy...sy+ly).each do |cy|
        @spaces[[cx,cy]] = [] if @spaces[[cx,cy]].nil?
        @spaces[[cx,cy]] = @spaces[[cx,cy]] << id
      end
    end # block
  end # method - add_area
end # class

ctr = Fabric.new
input = AdventApi::get_day(3,2018).lines
#input = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
input.each { |section| ctr.add_area section}
puts "part 1: #{ctr.spaces.count{ |k,v| v.size > 1}}"

ctr.spaces.select {|key,val| val.size >1}.each do |k,v|
    v.each {|i| ctr.claims.delete(i)}
end
puts "part 2: #{ctr.claims[0]}"
