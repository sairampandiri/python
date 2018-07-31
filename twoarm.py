# print armstrong number in between two numbers
n,k=input().split()
n=int(n)
k=int(k)
for i in range(n,k+1):
	temp=i
	b=0
	#for j in range(0,i):
	while(temp!=0):
		a=temp%10
		b=b+a**3
		temp=temp//10
	if(i==b):
		print(i,end="")
