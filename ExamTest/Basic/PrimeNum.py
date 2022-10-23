class Mynum:
    def __init__(self,num):
        if num == None:
            self.num = "Empty"
        else: 
            self.num = num
    
    def isPrime(self):
        print(self.num)
        for i in range(2,self.num):
            if self.num % i == 0:
                return str(self.num) + " is Not Prime"
            else:
                return str(self.num) + " is Prime"
    
    def showPrime(self):
        isPrime = True
        ls = []
        for i in range(2,self.num):
            for k in range(2,i):
                if i % k == 0:
                    isPrime = False
                    break
                else:
                    isPrime = True
            if isPrime == True:
                ls.append(i)
        return ls



inp = list(map(int,input("Enter number : ").split()))
print(inp)
time = len(inp)
# print(type(time))
for i in range(time):
    # print(i)
    ans = Mynum(inp[i])
    print(ans.isPrime())
    print(ans.showPrime())


#  *** class MyInt ***
# Enter 2 number : 5 20
# 5 isPrime : True
# 20 isPrime : False
# Prime number between 2 and 5 : 2 3 5
# Prime number between 2 and 20 : 2 3 5 7 11 13 17 19
# 5 - 20 = -5