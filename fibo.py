#given a number n and print fibonacci series
n=int(input())
a=0
b=1
for i in range(0,n):
  c=a+b
  a=b
  b=c
  if i<n-1:
    print(a,end=" ")
  else:
    print(a,end="")
