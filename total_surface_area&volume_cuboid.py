#write a program to calculate the total surface area and volume of cuboid.Input contain 3 space separated positive integers L,B,H denoting the length,Width and Height of cuboid respectively
a,b,c=map(int,input().split())
print((2*a*b)+(2*a*c)+(2*b*c),end=" ")
print(a*b*c)
