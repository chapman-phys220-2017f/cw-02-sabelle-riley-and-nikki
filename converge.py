#!/usr/bin/env python

k = input("Please enter a value for k")

final_sum = 0
def compute_sum(tol=1e-2):
    while next_sum > tol:
        next_sum = ((1/k)**2)
        final_sum = (final_sum + next_sum)
        k+=1
    return(final_sum)    

print(compute_sum)
