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
Animal1 = Animal("Муся", "Девочка")
Animal1.Name()
Animal1.Sex()
Animal1.Age()

