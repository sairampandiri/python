#given a number n,print the sum of all digits
n=int(input())
a=0
for i in range(0,n):
  if(n>0):
    a=a+n%10
    n=n//10
print(a)
