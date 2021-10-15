def func(n):
    if n <= 5:
        return n
    elif n > 5 and n % 5 == 0:
        return n + func(n/2 - 3)
    elif n > 5 and n % 5 != 0:
        return n + func(n+4)


last_i = 6
for i in range(6, 1000000):
    try:
        mx = func(i)
    except RecursionError:
        print(i-1)
        break
