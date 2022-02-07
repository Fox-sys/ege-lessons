def b(a):
    if a % 2 == 0:
        a = bin(a)
        a = '1' + a[2:]
    else:
        a = bin(a)[2:]
        a += '0'
    if a.count('1') % 2 == 0:
        a += '1'
    else:
        a += '0'
    return int(a, base=2)


for i in range(10000):
    if b(i) > 228:
        print(i)
        break

# 50