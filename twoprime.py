# prime number between two intervals
lower,upper =input().split()
lower=int(lower)
upper=int(upper)
count=0
for num in range(lower,upper):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				break
            		
		else:
			count+=1
			if(count==1):
				k=''
			else:
				k=" "
			print(end=k)
			print(num,end='')# your code goes here
