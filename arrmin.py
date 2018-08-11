#given an array for minimun element
n=int(input())
a = [int(x) for x in input().split()]
if 1<=n and n<=100000:
	print(min(a),end="")
