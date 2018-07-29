# Given two numbers display odd numbers between two intervals
n,s=map(int,input().split())
for i in range(n,s):
	if((i%2==1)and(i<=100000)):
		print(i,end=" ")
