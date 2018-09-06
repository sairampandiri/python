#Given 2 numbers N and K followed by N numbers print the number of repitions of the k
n,m=map(int,input().split())
lst=[int(x) for x in input().split()]
c=0
for i in range(0,n):
  if m==lst[i]:
    c+=1
print(c)
