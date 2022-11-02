db = int(input("день рождения "))
mb = int(input("месяц рождения "))
yb = int(input("год рождения "))
dn = 5
mn = 11
yn = 2022
y = yn-yb
if mb-mn > 0:
    y-=1
if mb-mn == 0 and db-dn < 0:
    y-=1
print("Полных лет ", y)