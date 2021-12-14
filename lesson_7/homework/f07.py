def is_prime(n):
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


result = []
for x in range(27):
    for p in range(3, 98):
        if not is_prime(p):
            continue
        if 77777777 <= 2 ** x * p ** 4 <= 88888888:
            result.append([2 ** x * p ** 4, p])

print(result)