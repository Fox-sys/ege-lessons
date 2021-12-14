def func(n):
    n = bin(n)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    return int(n, base=2)


for i in range(1, 10000000):
    if func(i) > 77:
        print(i)
        print(func(i))
        break