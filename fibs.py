#!/usr/bin/env python

n = input ("Type an integer for the amount of fibonacci numbers you want")

def fibs(n):
    
    fib_list = [1]
    a=0
    b=1
    while n > 1:
        fib_list.append(a+b)
        c=a
        a=b
        b=b+c
        n=n-1
    return(fib_list)

print(fibs(n))