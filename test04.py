inp = input("Enter String :").split()
buf1 = inp[0]
buf2 = inp[1]
counter = 0

while True:
    temp = buf1[len(inp[0])-2:]
    temp += buf1[:len(inp[0])-2]
    temp2 = buf2[3:len(inp[1])]
    temp2 += buf2[:3]
    buf1 = temp
    buf2 = temp2
    counter += 1
    if counter <= 5:
        print("{} {} {}".format(counter,temp,temp2))
    if temp == inp[0] and temp2 == inp[1]:
        print(".........")
        break
print(counter,end=' ')
print(temp,temp2)