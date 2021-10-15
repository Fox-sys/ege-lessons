def func(n):
    if n % 7 == 0 and int(str(n)[0]) + int(str(n)[-1]) > 10:
        return True
    else:
        return False


ls = []
for i in range(4563, 7913):
    if func(i):
        ls.append(i)

print(max(ls), len(ls))
