#given an array for maximum element
n=int(input())
a = [int(x) for x in input().split()]
if 1<=n and n<=100000:
	print(max(a),end="")
