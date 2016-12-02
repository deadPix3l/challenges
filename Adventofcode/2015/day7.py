#!/usr/bin/env python
import collections
import adventapi

def calculate(op):
    vals = []
    action = ""
    args = op.split(" ")
    print args
    
    
    for i in args:
        try: vals.append(int(i))
        except ValueError:
            if i.islower():
                vals.append(wires[i])
            else:
                action = i
    
    print vals
    print ""
    if action == "": return vals[0]
    elif action == "AND": return vals[0] & vals[1]
    elif action == "OR": return vals[0] | vals[1]
    elif action == "NOT": return ~ vals[0]
    elif action == "LSHIFT": return vals[0] << vals[1]
    elif action == "RSHIFT": return vals[0] >> vals[1]
    else: raise ValueError("{} is not a supported gate.".format(action))
    
if __name__ == "__main__":
    
    wires = collections.defaultdict(int)
    lines = adventapi.levelInput(7).split("\n")

    for i in lines:
        try:
           op, result = i.split(' -> ')
        except ValueError:
            print i.split('->')
            continue
        
        wires[result] = calculate(op) & 0xffff
        
    print "part 1:", wires['a']
    for k in wires:
        print k, wires[k]