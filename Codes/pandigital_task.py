#!/usr/bin/env python

from itertools import permutations
from math import sqrt

def isPrime(x):
    if x == 1:
	return 0
    for n in range(2,int(sqrt(x))+1):
	if x % n == 0:
	    return 0
	else:
	    pass
    return 1
def ispan():
    for i in permutations('7654321'):
        i = int("".join(i))
        if isPrime(i):
	   return i
	   break
#===================================#
if __name__ == '__main__':
    print "The largest existing n-digit pandigital prime is -",ispan()