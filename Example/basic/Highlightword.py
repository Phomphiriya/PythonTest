inp1,inp2 = input("Enter your text and word : ").split(',')
outp = ""
for i in inp1:
    if i == inp2:
        outp += "[{}]".format(i) ####
    else:
        outp += i
print(outp)