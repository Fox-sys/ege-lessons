def is_prime(n):
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


counter = 0
result = []
for i in range(3532000, 3532161):
    if is_prime(i):
        counter += 1
        result.append([i, counter])

print(result)
