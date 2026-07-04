'''class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start_engine(self):
        print("Engine of the car started")

BMW=Car("Maruti","VXK",2026)
print(BMW.make)
print(BMW.model)
print(BMW.year)
BMW.start_engine()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
stu1=Student("krish",31)
print(stu1.name)
print(stu1.age)

class bank:
    def __init__(self,account,balance=0):
        self.__account=account
        self.__balance=balance
    def get_deposit(self,deposit):
        self.__balance=deposit+self.__balance
        print(self.__balance)

    def withdraw(self,amount):
        self.__balance=self.__balance-amount
        print(self.__balance)

    def check(self):
        print(self.__balance)
ranu=bank(1234)
ranu.check
ranu.get_deposit(5000)
ranu.withdraw(1234)
ranu.check()

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
class Dog(Animal):
    def __init__(self, name, species,breed):
        self.breed=breed
        super().__init__(name, species)
    def __str__(self):
        return f"{self.name} is a {self.breed}"
    def bark(self):
        print(f"{self.name} says Woof!")


Kutta1=Dog("Buddy","Dog","German")
print(Kutta1.name)
print(Kutta1.species)
print(Kutta1.breed)
print(Kutta1.__str__())
print(Kutta1.bark())

 '''
class Walker:
    def walk(self):
        print("Walker is Walking")
class Runner:
    def run(self):
        print("Runner is running")
class Athlete(Walker,Runner):
    def walk(self):
        print("Athelete is here")
        super().walk()

ram=Athlete()
ram.walk()
ram.run()