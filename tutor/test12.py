class Person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def check(self):
        if self.age >= 18:
            return str(self.name + " " +"Pass!!")
        else:
            return str(self.name + " "+"Can't pass!!")

    def __str__(self):
        return ("{} {} {}").format(self.name,self.gender,self.age)

name,gender,age = input("Enter your name,gender and age : ").split(' ')
age = int(age)
p = Person(name,gender,age)
print(p)
print(p.check())