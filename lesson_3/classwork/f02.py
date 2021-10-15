def func(d):
    s = 5
    n = 7
    while s <= 3011:
        s += d
        n += 124
    return n


if __name__ == '__main__':
    result = []
    for i in range(1, 100000):
        if func(i) == 1247:
            result.append(i)
    print(result)
