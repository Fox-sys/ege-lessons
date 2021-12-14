def func(N):
    x = bin(N)[2:]
    k = ''
    for i in x:
        k += str(int(not bool(int(i))))
    k = int(k[1:], base=2)
    return k + N


for i in range(10, 100):
    if func(i) > 99 and i % 2 == 1:
        print(i)
        break
