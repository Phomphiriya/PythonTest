inp = int(input("Enter your number :"))

for i in range(inp):
    for j in range(i+1):
        print("*",end='')
    print(end='\n')