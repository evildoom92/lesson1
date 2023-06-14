def sum(n):
    if n < 10:
        return n
    return sum(n // 10) + n % 10
n = int(input())
if n < 0: n = -n;
print(sum(n))