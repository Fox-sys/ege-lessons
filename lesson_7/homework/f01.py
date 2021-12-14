def func(x):
    y = str()
    y += f'{x % 2}'
    y += f'{x % 3}'
    y += f'{x % 5}'
    return int(y)


for i in range(10, 100):
    if func(i) == 104:
        print(i)
        break
