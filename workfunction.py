import numpy as np
import os

def complement(a, b):
        b = set(b)
        return [i for i in a if i not in b]

def workfunction(D,d,T,M,N):
	#D is the number of days total
	#d is the day of signup
	#T is the time required for signup for library j
	#M is the number of books per day for library j
	#N is the number of books in library j
	return np.min([(D-d-T)*M,N])

def maxScore(s,B,Z,D,d,T,M):
	#s is the ordered score list for all books remaining
	#B is the list of books for library j
	#Z is the global worklist
	#D is the number of days total
	#d is the day of signup
	#T is the time required for signup for library j
	#M is the number of books per day for library j

	b = complement(B,Z)
	w = workfunction(D,d,T,M,len(b))
	dZ = b[:w]
	return np.sum([s[i] for i in dZ]),dZ

for i in range(int(1E5)):
	maxScore([100,50,2,1],[1,2,3],[2,3],3,0,1,1)
