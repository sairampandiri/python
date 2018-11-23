#given a string s,print it after changing middle element to * (if the length of the string is even ,change the middle elements to *)
a=input()
if(len(a)%2)==1:
  b=len(a)//2
  a=a.replace(a[b],'*')
  print(a)
else:
  b=len(a)//2
  a=a.replace(a[b],'*')
  a=a.replace(a[b-1],'*')
  print(a)
