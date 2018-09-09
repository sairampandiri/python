#Given two numbers N and K followed by N numbers print the Kth odd number
a,b=map(int,input().split())
c=[int(x) for x in input().split()]
q=0
for i in range(0,a):
  if(c[i]%2)!=0:
    q+=1
  if(b==q):
    print(c[i])
    break
