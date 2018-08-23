#print each element with its index
n=int(input())
b=[int(x) for x in input().split()]
a=0
for i in b:
  print(i,a)
  a+=1
