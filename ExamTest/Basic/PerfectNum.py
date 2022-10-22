inp = int(input("Enter number : "))

if inp < 1:
    print("Error")
else:
    ls1 = []
    for i in range(1,inp):
        if inp % i == 0:
            ls1.append(i)
    
    if sum(ls1) == inp:
        print("It is a perfect Number")
    else:
        print("It is not a perfect Number")
print(f'Factor of {inp} are {ls1}')
