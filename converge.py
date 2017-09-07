#!/usr/bin/env python

k = input("Please enter a value for k")

final_sum = 0
next_sum = ((1/k)**2)
def compute_sum(tol=1e-2):
    while next_sum > tol:

        final_sum = (final_sum + next_sum)
        
    return(final_sum)    

print(compute_sum)
