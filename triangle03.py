inp = int(input("Enter your number :"))
k = inp
for i in range(inp+1):
    for j in range(k):
        print(" ",end='')
    k -= 1
    for m in range((2*i-1)):
        print("*",end="")
    print(end="\n")