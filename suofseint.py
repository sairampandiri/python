# Given two numbers N,K and an array of N tntegers,find the sum of first 'k' integers 
from array import array
N=int(input())
K=int(input())
b=0
N = array("i")
for x in range(1,K+1):
	b+=x
print(b)
