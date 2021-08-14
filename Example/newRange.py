def rangefor(start=0,stop=0,step=1):
    ls1 = []
    print(start,stop,step)
    i = start
    while i < stop:
        ls1.append(round(i,2))
        i += step
    return ls1

inp = list(map(float,input("Enter input : ").split()))
if len(inp) == 3:
    print(rangefor(inp[0],inp[1],inp[2]))
elif len(inp) == 2:
    print(rangefor(inp[0],inp[1]))
elif len(inp) == 1:
    print(rangefor(stop=inp[0]))
