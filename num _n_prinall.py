#Given a number N,print all its digits(in same order)
'''x=input()
y=list(str(x))
for a in range(0,len(y)):
  if(a<len(y)-1):
    print(y[a],end=" ")
  else:print(y[a],end="")'''
l=input()
print(" ".join(str(x) for x in l))
