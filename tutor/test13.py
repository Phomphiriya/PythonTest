def palin(inp):
    lis = []
    for i in reversed(inp):
        lis.append(i)
    return lis == inp
inp = list(input())
print(palin(inp))