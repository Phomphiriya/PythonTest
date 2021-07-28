x = list(input("Enter your number : ").split(','))
print(x)

ls = []
ls1 = list()
ls.append(10) #ต่อท้าย
ls.append(20)
ls.append(30)
print(ls)
print(ls[1]) #print list ตัวที่ทำไหร่
ls.pop(1) #delete 
ls.insert(1,20) #แทรก (index,object)

print(len(ls)) #มีกี่ตัวในlist


#มีกี่ตัวในindex
for i in range(len(ls)):
    if ls[i] == 20:
        ls[i] = 15
print(ls)

for i in ls:
    if i == 20:
        a = ls.index(i)
        ls[a] = 15
print(ls)