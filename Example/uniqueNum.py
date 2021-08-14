inp = input("Enter str : ")
dictT = {}
a = 0

for i in inp:
    ls = list(dictT.keys())
    if i in ls:
        pass
    else:
        temp = {i:a}
        dictT.update(temp)
        a += 1
    print(dictT)

ls2 = []
for i in inp:
    a = dictT.get(i)
    ls2.append(a)
print(ls2)