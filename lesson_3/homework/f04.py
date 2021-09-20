def func(s):
    n = 40
    while s + n < 100:
        s += 25
        n -= 5
    return n


if __name__ == '__main__':
    result = []
    for i in range(10000):
        if func(i) == i:
            print(i)
            break
