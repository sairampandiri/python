#write a program to compare two strings without using strcmp() function,print the grater string or if equalprint any one string
a,b=input().split()
if(len(a)>len(b)):
  print(a)
elif(len(a)<len(b)):
  print(b)
else:
  print(a)
