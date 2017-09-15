#!/usr/bin/env python

def coord_for(n, a, b):
    h=(b-a)/n
    list_int = []
    for i in range(n+1):
        list_int.append(a + i*h)
    return list_int
print(coord_for(n))

def coord_while(n,a,b):
    h=(b-a)/n
    list_int=[]
    i=0
    while i < len(range(n+1)):
        list_int.append(a + i*h)
        i+=1
    return list_int
print(coord_while(n))

def coord_comp(n,a,b):
    h=(b-a)/n
    list_int=[3*x for x in range(n+1)]
    return list_int
print(coord_comp(n))