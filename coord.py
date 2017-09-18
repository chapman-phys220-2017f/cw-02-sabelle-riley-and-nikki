#!/usr/bin/env python
### INSTRUCTOR NOTE
# Be sure to specify "python3" above. CoCalc defaults to python2 still.
###

def coord_for(n, a, b):
    h=(b-a)/n
    list_int = []
    for i in range(n+1):
        list_int.append(a + i*h)
    return list_int

### INSTRUCTOR NOTE
# Do not have executable code like this outside of a main block.
print(coord_for(n))
###

def coord_while(n,a,b):
    h=(b-a)/n
    list_int=[]
    i=0
    while i < len(range(n+1)):
        list_int.append(a + i*h)
        i+=1
    return list_int
print(coord_while(n))   ### See above

def coord_comp(n,a,b):
    h=(b-a)/n
    list_int=[3*x for x in range(n+1)]   ### This should be [a + i*h for i in range(n+1)]
    return list_int
print(coord_comp(n))    ### See above
