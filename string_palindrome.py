#Given a string s ,check the palindrome.print yes/no
a=input()
b=a[::-1]
if(a==b):
  print("yes")
else:
  print("no")
'''b=""
for i in range(len(a)-1,-1,-1):
  b=b+a[i]
print(a.reverse())'''
