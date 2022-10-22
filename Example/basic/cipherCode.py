# def charToAscii(char):
#     char[0] = str(char[0])
#     sym = {"A":65,"B":66,"C":67,"D":68,"E":69,"F":70,"G":71,"H":72,"I":73,"J":74,"K":75,"L":76,"M":77,"N":78,"O":79,"P"
#     :80,"Q":81,"R":82,"S":83,"T":84,"U":85,"V":86,"W":87,"X":88,"Y":89,"Z":90}
#     ls1 = list(sym.keys())
#     ls2 = list(sym.values())
#     i = 0
#     while i < len(char[0]):
#         a = sym.get(char[0][i])+int(char[1])
#         i += 1
#         indexValue = ls2.index(a)
#         print(ls1[indexValue],end="")
#     return

# inp = input("Enter input : ").split(',')
# charToAscii(inp)

# Test case
# ABCD,2
# CDEF

def chartoAscii(char,num):
    ls1 = []
    ans = ""
    for i in char:
        ls1.append(ord(i))
    for i in ls1:
        ans += (chr(i+num))
    return(ans)

inp = input("Enter : ").split(',')
inp1 = str(inp[0])
inp2 = int(inp[1])
print(chartoAscii(inp1,inp2))
