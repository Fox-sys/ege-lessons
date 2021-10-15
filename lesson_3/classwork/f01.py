def func(d):
    n = 1
    while d // n > 0:
        d -= 2
        n += 3
    return n


if __name__ == '__main__':
    result = []
    for i in range(10000):
        if func(i) == 46:
            result.append(i)
    print(max(result) + min(result))
