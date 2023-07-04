class Car:
    def __init__(self, brand, country):
        self.b = brand
        self.c = country
    def Cars(self):
        print("Автомобиль: " + self.b + " Производство: " + self.c)
Car1 = Car("Мерседес", "Германия")
Car1.Cars()
Car1 = Car("Рено", "Франция")
Car1.Cars()
Car1 = Car("Ситроен", "Франция")
Car1.Cars()
Car1 = Car("Хонда", "Япония")
Car1.Cars()
Car1 = Car("Хюндай", "Япония")
Car1.Cars()