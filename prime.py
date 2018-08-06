# prime number
a=int(input())
if a<=1000:
	if a>1:
		for i in range(2,a):
			if (a%i)==0:
				print("no",end="")
				break
		else:
			print("yes",end="")
	else:
		print("yes",end="")
else:
	print("no",end="")
