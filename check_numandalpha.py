#given a string s, check if contains numeric and alphabets
m=input()
c=0
d=0
for i in m:
    if(i.isdigit()):
      c=c+1
    if(i.isalpha()):
      d=d+1
    if(c>0 and d>0):
        print('Yes')
        break
if(c==0 or d==0):
  print('No')
