# 1 1 2 2 4 4 5 5 5 -1 7 7 8 9
inp = input("Enter : ").split('-1')
ls = []
dictT = {}
for i in inp[0].split():
    ls.append(i)
print(ls)

for i in ls:
    ls1 = list(dictT.keys())
    if i in ls1:
        dictT[i] += 1
    else:
        temp = {i:1}
        dictT.update(temp)

ls2 = list(dictT.keys())
ls3 = list(dictT.values())

maxT = max(ls3)
indexT = ls3.index(maxT)
print(ls2[indexT])