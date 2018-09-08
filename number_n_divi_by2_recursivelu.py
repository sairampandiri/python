#Given a number N,print the number obtaining by dividing it by 2 recursively till it is not divisible
a=int(input())
if(1<=a<=10):
  if(a%2)==0:print(a//2)
  else:print(a)
