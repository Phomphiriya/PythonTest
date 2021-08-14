def findCode(inp):
    temp = ''
    for i in inp:
        if i != temp:
            temp = i
        else:
            break
    print(temp)
    return temp

def decode(temp):
    for j in range(ord('a'),ord('z')+1):
        if chr(j) == temp:
            div = (j - ord('a')+1)

            return 4*(div)


inp = input("Enter code : ")
print(decode(findCode(inp)))