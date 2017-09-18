#!/usr/bin/env python
#This is the code for converge.py

def compute_sum(kValue, tolValue):
    final_sum=0
    next_sum=((1/k)**2)                     ### k is undefined here
    while next_sum > tol:                   ### tol is undefined here
        final_sum = (final_sum + next_sum)  ### you could use += here
        k+=1
        next_sum = ((1/k)**2)               ### you could define next_sum(k) as a function of k
    return(final_sum)

#for k = .5 on lower and lower tolerances, compute_sum approaches 5)
