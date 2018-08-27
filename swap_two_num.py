#write a program to swap two numbers
a,b=map(int,input().split())
c=a
a=b
b=c
if(a<=100000 and b<=100000):
  print(a,b)
