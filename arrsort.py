# sort array of n element
n=int(input())
a = [int(x) for x in input().split()]
if 1<=n<=1000:
	a.sort()
	print(a,end="")
