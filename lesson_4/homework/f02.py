def func(n):
    if n < 2:
        return 1
    elif n >= 2 and n % 3 == 0:
        return func(n/3) - 1
    elif n >= 2 and n % 3 != 0:
        return func(n-1) + 17

ls = []
for i in range(2, 100000):
    if func(i) == 110:
        ls.append(i)
print(len(ls))
