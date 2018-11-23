#given two times in hours and minutues format subtract (abs value) them and print in the same format
a,b=map(int,input().split(" "))
c,d=map(int,input().split(" "))
a=a*60+b
c=c*60+d
f=abs(a-c)
print(f//60,f%60)
