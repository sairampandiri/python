# check whether it is armstrong or not
n=int(input())
temp=n
b=0
if(n<=100000):
	while(n>0):
		a=n%10
		b=b+a**3
		n=n//10
	if(temp==b):
		print("yes")
	else:
		print("no")
