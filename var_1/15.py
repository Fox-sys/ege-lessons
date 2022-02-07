def func(a, b):
    for x in range(0, 100):
        f = ((a <= x <= b) <= (10 <= x <= 29)) or (13 <= x <= 18)
        if not f:
            return False
    return True


ls = []
for a in range(0, 100):
    for b in range(a, 100):
        result = func(a, b)
        if result:
            ls.append(b-a)
print(max(ls))