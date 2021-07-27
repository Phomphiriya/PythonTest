def pyramidFull(inp):
    k = inp - 1
    n = 1
    l = (2*inp - 1)-2
    for i in range((inp)-1):
        for o in range(k):
            print(" ",end='')
        k = k-1    
        for j in range(2*i+1):
            print("*",end='')
        print(end='\n')
    print("*"*(2*inp-1),end='\n')
    for i in range((inp)-1,0,-1):
        for o in range(n):
            print(" ",end='')
        n += 1
        for j in range(l):
            print("*",end='')
        print(end='\n')
        l -= 2        




inp = int(input())
pyramidFull(inp)