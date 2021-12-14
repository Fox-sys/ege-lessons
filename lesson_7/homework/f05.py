counter = 0
max_sum = 0
max_c = 0

for i in range(1, 5001):
    for j in range(i, 5001):
        c = round((i ** 2 + j ** 2) ** 0.5)
        if 5000 >= c and i ** 2 + j ** 2 == c ** 2:
            counter += 1
            if i + j + c >= max_sum:
                max_c = c
                max_sum = i + j + c
print(counter, max_c)
