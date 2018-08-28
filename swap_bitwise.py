#write a program to swap two numbers by using bit wise operator
a,b=map(int,input().split())
a=a^b
b=a^b
a=a^b
print(a,b)
