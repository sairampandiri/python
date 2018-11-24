#Given two numbers N,M.Find their product and check whether it is a perfect square
a,b=map(int,input().split())
n=a*b
for i in range(1,n):
    if i*i==n:
      print("yes")
      break
else:
  print("no")
    
