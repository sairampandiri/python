#Given 2 numbers N,M,print whether the product of two numbers is even or odd
a,b=map(int,input().split())
c=a*b
if(c%2)==0:
  print("even")
else:print("odd")
