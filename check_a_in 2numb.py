#Given a number N and 2 numbers .Check whether N is between L and R.print yes/no
c=int(input())
a,b=map(int,input().split())
if(a<b<c):
  print("yes")
else:
  print("no")
