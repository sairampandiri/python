# Given two numbers display even numbers between two intervals
n,s=map(int,input().split())
for i in range(n+1,s+1):
	if(i%2==0):
		print(i,end=" ")
