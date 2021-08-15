def findSum(inp):
    inpLen = len(inp)
    lsAns = []
    ls = []
    if inpLen < 3:
        return "Your input must be more than 2 numbers"
    else:
        for i in range(inpLen):
            for j in range(i+1,inpLen):
                for k in range(j+1,inpLen):
                    eqZero = inp[i] + inp[j] + inp[k]
                    ls = [inp[i],  inp[j],  inp[k]] #********
                    if eqZero == 0 and ls not in lsAns:
                        lsAns.append(ls)
    return lsAns


inp = list(map(int,input("Enter your num : ").split()))
print(findSum(inp))

# test case
# input 3 3 -3 -3 6 5 -8
# output [[3, 5, -8], [-3, -3, 6]]