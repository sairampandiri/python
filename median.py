# median element
n=int(input())
b=[int(x) for x in input().split()]
c=b.sort()
if 1<=n<=1000:
  mn=int(n/2)
  if(n%2==0):
    print(b[mn-1],b[mn])
  else:
    print(b[mn])
