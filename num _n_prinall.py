#Given a number N,print all its digits(in same order)
'''x=input()
y=list(str(x))
for a in range(0,len(y)):
  if(a<len(y)-1):
    print(y[a],end=" ")
  else:print(y[a],end="")'''
'''l=input("Enter the value:")
print(" j".join(str(x) for x in l))'''
N=int(input())
n=N%10
m=N//10
g=m%10
h=m//10
print(h,g,n)
