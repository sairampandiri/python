# count nummbers of digits of an integer
n=int(input())
l=0
while(n>0):
	n=n//10
	l+=1
print(l)
