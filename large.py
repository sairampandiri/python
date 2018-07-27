num1,num2,num3=map(int,input().split())
if(num1>num2 or num2>num3):
	if(num1>num2):
		print(num1)
	else:
		print(num2)
else:
	print(num3)
