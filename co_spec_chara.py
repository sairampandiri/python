#count the number of special characters in agiven string
n=input()
a=0
for i in range(0,len(n)):
  if(n[i]!=" " and n[i].isalnum()==False):
    a+=1
print(a)
