# Arthematic progression till n terms
n,a,d=input().split()
n=int(n)
a=int(a)
d=int(d)
if((1<=n)and(d<=100000)):
	ap=((n)*((2*a)+(n-1)*d))//2
	print(ap,end="")
