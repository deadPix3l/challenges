#!/usr/bin/env python
import adventapi

x = adventapi.levelInput(2, 2016)

def singlemove(n, direction, keypad):
    if keypad[n+direction] not in "123456789ABCD": return n
    return n + direction

a = '''
       
 123 
 456 
 789 
     
'''
b = '''
      
  1   
 234  
56789 
 ABC  
  D   
      
'''
p1 = {'U': -6, 'D': 6, 'L': -1, 'R': 1}
p2 = {'U': -7, 'D': 7, 'L': -1, 'R': 1}

#PART 1
n = a.index('5')
for line in x.split():
    for char in line:
        n = singlemove(n, p1[char], a)
    print a[n],
print ''


#PART 2
n = b.index('5')
for line in x.split():
    for char in line:
        n = singlemove(n, p2[char], b)
    print b[n],
