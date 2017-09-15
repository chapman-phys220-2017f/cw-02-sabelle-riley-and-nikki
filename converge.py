#!/usr/bin/env python
#This is the code for converge.py

def compute_sum(kValue, tolValue):
    final_sum=0
    next_sum=((1/k)**2)
    while next_sum > tol:
        final_sum = (final_sum + next_sum)
        k+=1
        next_sum = ((1/k)**2)
    return(final_sum)

#for k = .5 on lower and lower tolerances, compute_sum approaches 5)
