from Practices.t12_OOP_Base.Car import Car
from Practices.t12_OOP_Base.Math import Math
from Practices.t12_OOP_Base.Student import Student

first = Student("Tom", 18, "11A")
first.printInfo()

second = Student("Vlad", 14, "7Б")
second.printInfo()

third = Student()
third.SetNameAge("Sam", 15)
third.SetGroupNumber("8A")
third.printInfo()

forth = Student()
forth.SetNameAge("Tim", 11)
forth.SetGroupNumber("5B")
forth.printInfo()

fifth = Student()
fifth.SetNameAge("Nick", 8)
fifth.printInfo()


math = Math(1, 2)
print(math.division())
print(math.addition())


car = Car("black", "camry", 2019)
car.printInfo()
car.turn_on()
car.turn_off()

car.setColor("grey")
car.printInfo()





