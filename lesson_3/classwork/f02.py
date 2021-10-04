def func(x):
    a = 0
    b = 1
    while x > 0:
        a += 1
        b *= x % 10
        x //= 10
    return (a, b)


for i in range(1, 10000):
    if func(i) == (2, 15):
        print(i)
        break
