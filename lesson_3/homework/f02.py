def func(x):
    a = 0
    b = 1
    while x > 0:
        if x % 2 > 0:
            a += 1
        else:
            b += x % 7
        x //= 7
    return [a, b]


for i in range(0, 10000):
    if func(i) == [2, 5]:
        print(i)
        break

