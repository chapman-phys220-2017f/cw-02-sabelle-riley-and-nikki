#!/usr/bin/env python

### INSTRUCTOR NOTE
# Never use input. No production code will ask the user to type something.
# Also, any code that is not a definition should be put in the main block.
n = input ("Type an integer for the amount of fibonacci numbers you want")
###

def fibs(n):
    
    fib_list = []
    a=0
    b=1
    while n > 0:
        fib_list.append(b)
        a,b = b,a+b
        n=n-1
    return(fib_list)
#print(fibs(n))              ### Remove extraneous comments like this

def fibs_generator():
    a,b = 0, 1
    while True:
        yield b
        a,b = b, a+b
    return g                 ### No need for this return. It will never execute anyway.
        
#g = fibs_generator()        ### Remove extraneous comments.
#print([next(g) for _ in range(n)] )
