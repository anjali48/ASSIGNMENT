1. class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sq_sum(self):
        print(self.x ** 2 + self.y ** 2 + self.z ** 2)

s1 = Point(2, 3, 4)
s1.sq_sum()

2. name = input()
phy = int(input())
chem = int(input())
bio = int(input())
        
class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
        
    def Total(self):
        return self.phy + self.chem + self.bio
    
    def percentage(self):
        return (Student.Total(self) / 300) * 100
    
std = Student(name, phy, chem, bio)
print("total marks: {}".format(std.Total()))
print("percentage: {}".format(std.percentage()))

3.  class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2
    
num = Calculator(94, 10)
print(num.add())
print(num.subtract())
print(num.multiply())
print(num.divide())