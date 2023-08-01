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
    def __init__(self, name="Чарли", sex="Мальчик"):
        super().__init__(name, sex)
    def run(self):
        print("Собака бегает")
    def Name(self):
        print("Имя собаки: " + self.n)
class Rabbit(Animal):
    def __init__(self, name="Боби", sex="Девочка"):
        super().__init__(name, sex)
    def jump(self):
        print("Кролик прыгает")
    def Sex(self):
        print("Пол кролика: " + self.s)

class Cat(Animal):
    def __init__(self, name="Генри", sex="Мальчик"):
        super().__init__(name, sex)
    def sleep(self):
        print("Кошка спит")
    def Age(self):
        print("Возраст кошки: " + str(self.a))

Dog1 = Dog()
Dog1.Name()
Dog1.Sex()
Dog1.run()

Cat1 = Cat("Муся ",)
Cat1.Name()
Cat1.Sex()
Cat1.Age()
Cat1.sleep()

Rabbit1 = Rabbit(sex="Мальчик")
Rabbit1.Name()
Rabbit1.Sex()
Rabbit1.jump()