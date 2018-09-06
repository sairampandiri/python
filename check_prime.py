#Given a number s,check whether it is prime
a=int(input())
for i in range(2,a):
    if(a%i)==0:
      print("no")
      break
else:print("yes")
