def decorator(func):
    def wrapper():
        return func().upper()
    return wrapper
@decorator
def imy():
    return input("Введите Ваше имя: ")
print("Привет, ", imy())