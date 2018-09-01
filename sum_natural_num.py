#write a program to print the sum of the first n natural numbers
a=int(input())
c=0
if(a<100000):
  for i in range(0,a+1):
    c+=i
print(c)
