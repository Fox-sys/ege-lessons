def f(n):
    if n <= 5:
        return n
    elif n > 5 and n % 8 == 0:
        return n + f(n/2-3)
    elif n > 5 and n % 8 != 0:
        return n + f(n+4)


for i in range(5, 10000):
    try:
        print(f'{i}: {f(i)}')
    except RecursionError:
        continue
