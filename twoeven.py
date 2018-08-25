# Given two numbers display even numbers between two intervals
a,b=map(int,input().split())
for x in range(a,b):
    if(x%2==0 and x<b-2):
      print(x,end=" ")
    elif(x%2==0 and x<b):
      print(x,end="")
