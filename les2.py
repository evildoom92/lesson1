class Animal:
    def __init__(self, name, sex):
        self.n = name
        self.s = sex
        self.a = 2
    def Name(self):
        print("Имя: " + self.n)
    def Sex(self):
        print("Пол: " + self.s)
    def Age(self):
        print("Возраст: " + str(self.a))


class Dog(Animal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
    def run(self):
        print("Собака бегает")
class Rabbit(Animal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
    def jump(self):
        print("Кролик прыгает")

class Cat(Animal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
    def sleep(self):
        print("Кошка спит")

Dog1 = Dog("Шарик ", "Мальчик")
Dog1.Name()
Dog1.Sex()
Dog1.run()

Cat1 = Cat("Муся ", "Девочка")
Cat1.Name()
Cat1.Sex()
Cat1.sleep()

Rabbit1 = Rabbit("Федя", "Мальчик")
Rabbit1.Name()
Rabbit1.Sex()
Rabbit1.jump()