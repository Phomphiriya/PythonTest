inp = input("Enter your num")
ls = []
for k in inp.split(','):
    o = k.split()
    print(o)
    
    ls.append(o[0])
print(ls)