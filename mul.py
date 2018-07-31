# given a number and multiply 5 times
n=int(input())
i=1
for i in range(1,6):
	if(i<6):
		print(n*i,end=" ")
	else:
		print(n*i,end="")
	i+=1
