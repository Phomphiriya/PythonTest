import math

def functionName():
    return "Hello world"

def summation(a,b):
    sum = int(a + b)
    return sum

def sortList(a):
    a.sort()
    return a

print(functionName())

a =2
b =3
print(summation(a,b))

ls =[3,5,4,15,83,13]
print(sortList(ls))

def area(r):
    pi = math.pi
    area = pi*(math.pow(r,2))
    area = round(area,2)
    return area

def findthemost(a):
    return max(a)

inp = int(input("Enter your radius :"))
print(area(inp))
inp2 = list(map(int,input("Enter list of number: ").split(',')))
print(inp2)
print(findthemost(inp2))