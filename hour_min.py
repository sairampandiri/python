# given time in minutues,print it in hours and minutes
a=int(input())
b=0
mn=a
for i in range(0,a+1):
  if(i%60==0 and i>=60):
    b+=1
    mn-=60
print(b,mn)
