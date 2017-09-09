#!/usr/bin/env python

n=4
def coord_for(n, a=0, b=12):
    h=(b-a)/n
    list_int = []
    for i in range(n+1):
        list_int.append(a + i*h)
    return list_int
print(coord_for(n))


n=4
def coord_while(n, a=0, b=12):
    h=(b-a)/n
    list_int=[]
    i=0
    while i < len(range(n+1)):
        list_int.append(a + i*h)
	i+=1
    return list_int
print(coord_while(n))

n=4
def coord_comp(n, a=0, b=12):
    h=(b-a)/n
    list_int=[3*x for x in range(n+1)]
    return list_int
print(coord_comp(n))
