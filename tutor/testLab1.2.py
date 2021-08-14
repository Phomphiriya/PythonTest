from itertools import permutations as pmt
print("*** Fun with permute ***")
inp = input("input : ").split(',')
p = pmt(inp)
print("Original Cofllection :",inp)
for i in p:
    print(i)
