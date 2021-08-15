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

# test case
# input 1.0 10.0 1.3
# output [1.0, 2.3, 3.6, 4.9, 6.2, 7.5, 8.8]