#validate given string is numeric
a=input()
try:
    a=float(a)
    print("yes")
except:
    print("No")
