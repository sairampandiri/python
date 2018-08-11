# Given two numbers N,K and an array of N tntegers,find the sum of first 'k' integers 
c,b=input().split()
c=int(c)
b=int(b)
d=0
a = [int(x) for x in input().split()]
for i in range(0,b):
		d+=a[i]
print(d)
