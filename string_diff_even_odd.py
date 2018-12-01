#Given a string s,print 2 strings one containing all charactersin odd positions and other containing all characters in even positions
a=input()
d=""
g=""
for i in range(0,len(a)):
  if(i%2==0):
    d+=a[i]
for i in range(0,len(a)):
  if(i%2!=0):
    g+=a[i]
print(d,g)
