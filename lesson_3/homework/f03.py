def func(x):
    k = 1
    a = 0
    b = 0
    while x > 0:
        if x % 10 % 2 == 0:
            a = a * 10 + x % 10
        else:
            k *= 10
            b = b * 10 + x % 10
        x = x // 10
    a = a * k + b
    return a


for i in range(2, 1000000):
    try:
        if func(i) == 26391:
            print(i)
            break
    except OverflowError:
        print(i, end=' ')