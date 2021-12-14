def find_divs(n) -> int:
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return i + n // i
        i += 1
    return 0


result = []
counter = 0
for i in range(700000, 10000000000000):
    m = str(find_divs(i))
    if m[-1] == '8':
        result.append([i, m])
        counter += 1
    if counter == 5:
        break

print(result)