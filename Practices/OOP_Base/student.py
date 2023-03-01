class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def GetName(self):
        return self.name

    def GetAge(self):
        return self.age

    def GetGroupNumber(self):
        return self.groupNumber

    def SetNameAge(self, name, age):
        self.name = name
        self.age = age

    def SetGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

    def printInfo(self):
        print(f'name: {self.name} groupNumber: {self.groupNumber} age: {self.age}')
