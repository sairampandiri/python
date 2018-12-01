#given two numbers ,find their gcd
a,b=map(int,input().split())
c=""
c=max(a,b)
for i in range(1,c):
  if((a%i)==0 and (b%i)==0):
    c=i
print(c)
