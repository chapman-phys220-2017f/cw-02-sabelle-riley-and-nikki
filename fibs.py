#!/usr/bin/env python

n = input ("Type an integer for the amount of fibonacci numbers you want")

def fibs(n):
    
    fib_list = []
    a=0
    b=1
    while n > 0:
        fib_list.append(b)
        a,b = b,a+b
        n=n-1
    return(fib_list)

print(fibs(n))

def fibs_generator():
    
    a,b = 0, 1
    
    while True:
        yield b
        a,b = b, a+b

g = fibs_generator()
print([next(g) for _ in range(n)] )

    