#Given anuber a N,check wheather it is a composite or not
num=int(input())
for k in range(2,num):
  if (num%k)==0:
    print("yes")
    break
else:
  print("no")
