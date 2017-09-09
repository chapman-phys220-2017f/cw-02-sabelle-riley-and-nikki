#!/usr/bin/env python


def compute_sum(tol=1e-2):
    k = input("Please enter a value for k")
    final_sum=0
    next_sum=((1/k)**2)
    while next_sum > tol:
        final_sum = (final_sum + next_sum)
        k+=1
	next_sum = ((1/k)**2)
    print("Final Sum:",final_sum)
compute_sum()

compute_sum(1)
compute_sum(.5)
compute_sum(.25)
