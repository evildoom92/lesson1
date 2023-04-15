from random import random
N = 10
def func(mn,mx):
    for i in range(N):
        a[i] = int(random() * (mx-mn+1)) + mn
a = [0] * N
p = int(input("Ведите минимум "))
q = int(input("Ведите максимум "))
func(p,q)
print(a)