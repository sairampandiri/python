#given a string s and a number k,print the first s characters
a,b=input().split()
b=int(b)
for i in range(0,len(a)):
  if(b>i):
    print(a[i],end="")
