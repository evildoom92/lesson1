class Animal:
    def __init__(self, name, sex):
        self.n = name
        self.s = sex
        self.a = 2
    def Name(self):
        print("���: " + self.n)
    def Sex(self):
        print("���: " + self.s)
    def Age(self):
        print("�������: " + str(self.a))


class Dog(Animal):
    def __init__(self, name="�����", sex="�������"):
        super().__init__(name, sex)
    def run(self):
        print("������ ������")
    def Name(self):
        print("��� ������: " + self.n)
class Rabbit(Animal):
    def __init__(self, name="����", sex="�������"):
        super().__init__(name, sex)
    def jump(self):
        print("������ �������")
    def Sex(self):
        print("��� �������: " + self.s)

class Cat(Animal):
    def __init__(self, name="�����", sex="�������"):
        super().__init__(name, sex)
    def sleep(self):
        print("����� ����")
    def Age(self):
        print("������� �����: " + str(self.a))

Dog1 = Dog()
Dog1.Name()
Dog1.Sex()
Dog1.run()

Cat1 = Cat("���� ",)
Cat1.Name()
Cat1.Sex()
Cat1.Age()
Cat1.sleep()

Rabbit1 = Rabbit(sex="�������")
Rabbit1.Name()
Rabbit1.Sex()
Rabbit1.jump()