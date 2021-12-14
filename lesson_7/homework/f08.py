def find_divs_amount(n):
    counter = 0
    i = 1
    while i ** 2 < n:
        if n % i == 0:
            counter += 2
        i += 1
    if i ** 2 == n:
        counter += 1
    return counter


line = [[700000, find_divs_amount(700000)]]

last_amount = find_divs_amount(line[-1][0])
for i in range(700001, 1000000000000):
    amount = find_divs_amount(i)
    if last_amount < amount:
        line.append([i, amount])
    else:
        line = [[i, amount]]
    last_amount = amount
    if len(line) == 5:
        break

print(line)
