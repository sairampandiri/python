#Given a 2 numbers N,M find the difference and check whether it is even or odd
a,b=map(int,input().split())
c=a-b
if(c%2==0):
  print("even")
else:print("odd")
