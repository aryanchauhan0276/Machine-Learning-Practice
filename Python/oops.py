'''class shape:
    def area(self):
        pass

class Circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.radius*self.radius*3.14
class sqaure(shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length*self.length
    
def calculate(shape):
    print (shape.area())

circle1=Circle(10)
square1=sqaure(4)
l=[circle1,square1]
for sh in l:
    calculate(sh)
class shape:
    def identify(self):
        pass

class Circle(shape):
    def identify(self):
        return "This is a circle"
class sqaure(shape):
    def identify(self):
        return "This is a square"
def calculate(shape):
    print (shape.identify())

circle1=Circle()
square1=sqaure()
calculate(circle1)
calculate(square1)
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("This is a Car")

class Bike(Vehicle):
    def start_engine(self):
        print("This is a bike")

def identify(Vehicle):
    Vehicle.start_engine()

b1=Bike()
c1=Car()
identify(b1)
identify(c1)
class bank:
    def __init__(self,accno,bal=0):
        self.__accno=accno
        if bal<0:
            print("Balance cannot be negative")
        else:
            self.__bal=bal
    def deposit(self,amount):
        self.__bal=amount+self.__bal
        print(self.__bal)
    def withdraw(self,amount):
        self.__bal=self.__bal-amount
        print(self.__bal)
    def check(self):
        print(self.__bal)
aman=bank(1234,1000)
aman.deposit(1000)
aman.withdraw(100)
aman.check() 
'''
