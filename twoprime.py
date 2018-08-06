# prime number between two intervals
lower,upper =input().split()
lower=int(lower)
upper=int(upper)
for num in range(lower,upper):
	if num > 1:
		for i in range(2,num):
			k=""
			if (num % i) == 0:
				k=""
				break
            		
		else:
			k="f"
			print(num,end=k)
