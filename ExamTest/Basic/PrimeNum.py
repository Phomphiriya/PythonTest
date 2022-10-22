class Mynum:
    def __init__(self,num):
        self.num = num
    
    def isPrime(self):
        isPrime = True
        for i in range(2,self.num):
            if self.num % i == 0:
                isPrime = False
                return("Not Prime")
            else:
                return("Prime")
    
    def showPrime(self):
        showPrime = True
        ls = []


x,y = map(int,input("Enter 2 number : ").split())
m1 = Mynum(x)
m2 = Mynum(y)
m1.isPrime()

#  *** class MyInt ***
# Enter 2 number : 5 20
# 5 isPrime : True
# 20 isPrime : False
# Prime number between 2 and 5 : 2 3 5
# Prime number between 2 and 20 : 2 3 5 7 11 13 17 19
# 5 - 20 = -5