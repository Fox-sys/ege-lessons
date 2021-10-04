def isTrue(a, b):
    for x in range(0, 1000):
        x /= 10
        P = 5 <= x <= 30
        Q = 14 <= x <= 23
        A = a < x < b
        F = (P == Q) <= (not A)
        if not F:
            return False
    return True


max_len = 0
for a in range(0, 100):
    for b in range(a, 100):
        if isTrue(a, b):
            if b - a > max_len:
                max_len = b - a
print(max_len)
