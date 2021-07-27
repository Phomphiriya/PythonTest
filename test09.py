def findmorethan(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return "Equal"

inp = input("Enter your number :").split(",")
a,b = int(inp[0]),int(inp[1])
print(findmorethan(a,b))