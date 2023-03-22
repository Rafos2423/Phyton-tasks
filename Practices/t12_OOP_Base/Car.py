class Car:
    def __init__(self, color="red", type="maslcar", year="1977"):
        self.color = color
        self.type = type
        self.year = year

    def turn_on(self):
        print("Автомобиль заведен")

    def turn_off(self):
        print("Автомобиль заглушен")

    def setColor(self, color):
        self.color = color

    def setType(self, type):
        self.type = type

    def setYear(self, year):
        self.year = year

    def printInfo(self):
        print(f'color: {self.color} type: {self.type} year: {self.year}')