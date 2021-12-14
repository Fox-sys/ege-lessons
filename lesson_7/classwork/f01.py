def func(n):
    ls = list(sorted(list(map(int, str(n)))))
    if ls[0] == 0:
        first = int(f'{ls[1]}{ls[0]}')
    else:
        first = int(f'{ls[0]}{ls[1]}')
    second = int(f'{ls[-1]}{ls[-2]}')
    return second - first


for i in range(100, 1000):
    if func(i) == 40 and i != 400:
        print(i)
        break
