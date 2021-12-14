counter = 0
needed = None
for num in range(2894, 174883, 1):
    num = str(num)
    if num[-1] == "8" and sum(list(map(int, list(num)))) > 22:
        counter += 1
        if counter == 13:
            needed = num

print(counter, needed)
