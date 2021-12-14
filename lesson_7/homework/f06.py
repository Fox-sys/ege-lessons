result = []

for i in range(1, 100, 2):
    for j in range(0, 100, 2):
        if 100000000 < (2 ** i) * (5 ** j) < 300000000:
            result.append([(2 ** i) * (5 ** j), i + j])

print(result)
