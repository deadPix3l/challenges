#!/usr/bin/env python
import adventapi


def preprocess(raw_str, funcs):
    a = raw_str.split(" ")
    if a[0]=="turn": 
        a = a[1:]

    x = map(int, a[1].split(","))
    y = map(int, a[3].split(","))
    return (funcs[a[0]], x, y)

def lights(grid, instructions):
    for x in xrange(instructions[1][0], instructions[2][0] + 1):
       for y in xrange(instructions[1][1], instructions[2][1] + 1):
            grid[x][y] = instructions[0](grid[x][y])
    return grid

if __name__ == "__main__":
    x = adventapi.levelInput(6).split("\n")[:-1]
    onoroff = {"off":(lambda _: 0), "on":(lambda _: 1), "toggle":(lambda x: not x)}
    analog = {"off":(lambda x: max(0, x-1)), "on":(lambda x: x+1), "toggle":(lambda x: x+2)}
    
    #part one:
    grid = [[0 for i in xrange(1000)] for i in xrange(1000)]
    for i in x: 
        lights(grid, preprocess(i, onoroff))
    print "part 1:", sum(sum(i) for i in grid)
    
    #part two:
    grid = [[0 for i in xrange(1000)] for i in xrange(1000)]
    for i in x: 
        lights(grid, preprocess(i, analog))
    print "part 2:", sum(sum(i) for i in grid)
