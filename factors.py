#Given a number N, print its factors
n=int(input())
for i in range(1,n+1):
  if (n%i)==0:
    if(i<n):
      print(i,end=" ")
    else:
      print(i,end="")
