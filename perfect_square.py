#Given two numbers N,M.Find their product and check whether it is a perfect square
a,b=map(int,input().split())
n=a*b
if(n==0):
  print("yes")
else:
  for i in range(0,n):
      if i*i==n:
        print("yes")
        break
  else:
    print("no")
    
