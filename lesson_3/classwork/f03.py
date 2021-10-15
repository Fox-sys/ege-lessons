def func(s):
    n = 100
    while s - n >= 100:
        s += 20
        n += 40
    return s


if __name__ == '__main__':
    result = []
    for i in range(10000):
        if func(i) != i:
            result.append(i)
    print(min(result))
