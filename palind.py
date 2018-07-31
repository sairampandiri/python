# print palindrome or not
n=int(input())
temp=n
b=0
if(n<=1000):
	#for i in range(0,n):
	while(n>0):
		a=n%10
		b=b*10+a
		n=n//10
		
if(temp==b):
	print("yes")
else:
	print("no")
