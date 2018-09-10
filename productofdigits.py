#Given a number N.print product of digits
a=int(input())
b=1
if(a<=100000000000):
  while(a!=0):
    n=a%10
    b=b*n
    a=a//10
print(b)
