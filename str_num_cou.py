#count the number of numeric charectors in the string
s=input()
count=0
for a in s:
    if (a>='0' and a<='9'):
        count+= 1
print(count)
