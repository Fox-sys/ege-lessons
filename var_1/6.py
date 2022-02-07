def func(s):
    n = 1
    while s > 200:
        s -= 15
        n += 3
    return n


for i in range(1000000):
    if func(i) == 46:
        print(i)

# 425
