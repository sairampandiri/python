#Given anuber a N,check wheather it is a composite or not
n=int(input())
for i in range(2,n):
  if(n%i)==0:
    print("yes")
    break
else:
  print("no")
