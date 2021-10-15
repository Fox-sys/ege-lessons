with open('DZ3.txt', 'r') as file:
    info = list(map(int, file.read().split('\n')[0: -1]))
    file.close()
    last_elem = None
    counter = 0
    max_sum = -20000
    for i in info:
        if not last_elem:
            last_elem = i
            continue
        else:
            if i % 2 + last_elem % 2 == 1:
                if i % 2 == 0:
                    if i % 4 == 0 and last_elem % 11 == 0:
                        counter += 1
                        sm = last_elem + i
                        if sm > max_sum:
                            max_sum = sm
                else:
                    if last_elem % 4 == 0 and i % 11 == 0:
                        counter += 1
                        sm = last_elem + i
                        if sm > max_sum:
                            max_sum = sm

        last_elem = i

    print(counter, max_sum)
