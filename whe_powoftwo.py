#given a number n find whether it is a power of 2
a=int(input())
if(a==1):
  print("yes")
elif((a**2)%2==0):
  print("yes")
else:
  print("no")
