# sort array of n element
n=int(input())
c=0
a = [int(x) for x in input().split()]
if 1<=n<=1000:
	a.sort()
for i in range(0,len(a)):
		if(i==c):
			c+=1
			if(c==1):
				k=""
			else:
				k=" "
		else:
			k=""
		print(end=k)
		print(a[i],end="")
