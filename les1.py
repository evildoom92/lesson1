try:
    a = input("введите число 1 ")
    b = "привет"
    c = int(a)+b
except TypeError:
    print("не тот тип")
except ValueError:
    print("нужны числа")