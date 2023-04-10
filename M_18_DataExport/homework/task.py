d = 7


def func(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

print(func(2))