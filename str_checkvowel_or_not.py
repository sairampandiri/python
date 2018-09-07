#Given a String S,check whether it is a vowel or not and print yes or no
a=input()
for i in range(0,len(a)):
  if((a[i]=='a' or a[i]=='e'or a[i]=='i' or a[i]=='o' or a[i]=='u') or (a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U')):
    print("yes")
    break
  else:print("no")
  break
