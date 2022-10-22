class number:
    def __init__(self,inp1):
        self.number1 = inp1

    def getPrime(self):
        isPrime = True
        for i in range(2,self.number1):
            if (self.number1 % i) == 0:
               isPrime = False
        if isPrime == True:
            return("Prime")
        else:
            return ("Not prime")

    def showPrime(self):
        isPrime = True
        ls =[]
        for i in range(2,self.number1):
            for j in range(2,i):
                if (i % j) == 0:
                    isPrime = False
                    break
                else:
                    isPrime = True
            if isPrime == True:
                ls.append(i)
        return(ls)

    def __str__(self):
        return ("Your input is {}").format(self.number1)

inp1 = input("Enter number : ")
inp1 = int(inp1)
n = number(inp1)
print(n)
print(n.getPrime())
print(n.showPrime())