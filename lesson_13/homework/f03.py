def update(buffer: list, dc: dict, new: int):
    if buffer[0] % 2 == 0:
        if buffer[0] % 13 == 0:
            dc['n_13_even'] += 1
        dc['even'] += 1
    else:
        if buffer[0] % 13 == 0:
            dc['n_13_odd'] += 1
        dc['odd'] += 1
    buffer.pop(0)
    if new % 2 == 0 and new % 13 == 0:
        dc['amount'] += dc['odd']
    elif new % 2 == 1 and new % 13 == 0:
        dc['amount'] += dc['even']
    elif new % 13 != 0 and new % 2 == 0:
        dc['amount'] += dc['n_13_odd']
    elif new % 13 != 0 and new % 2 != 0:
        dc['amount'] += dc['n_13_even']
    buffer.append(new)
    print(buffer)
    return buffer, dc


with open('dz4b.txt') as file:
    data = list(map(int, file.read().split('\n')[1:]))
    buffer = data[0: 5]
    dc = {
        'odd': 0,
        'even': 0,
        'n_13_odd': 0,
        'n_13_even': 0,
        'amount': 0
    }
    for i in data[5:]:
        buffer, dc = update(buffer, dc, i)

    print(dc['amount'])
