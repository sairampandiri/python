#subtraction of hours to minutues
a,b=map(int,input().split())
k,j=map(int,input().split())
nm=b
nmm=j
s=0
print(nm)
if(a>k):
  s=a-k
  nm=b-j
  if(b<=0):
    a-=1
    nm+=1
  print(s,nm)
