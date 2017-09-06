#!/usr/bin/env python

n=4
def coord_for(n, a=0, b=12):

    h=(b-a)/n
    list_int = []
    for i in range(n+1):
        list_int.append(a + i*h)

    return list_int

print(coord_for(n))