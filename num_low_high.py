#given a number N followed by N numbers find the lowest and highest number in the array
a=int(input())
b=[int(x) for x in input().split()]
if(a<10000):
  while(len(b)>a):
    n=int(input())
    b.append(n)
  print(min(b),max(b))
