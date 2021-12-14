with open('dz1.txt') as file:
    content = file.read().split('\n')
    minus_amount = int(content[0].split()[1])
    info = sorted(list(map(int, content[1:])))[minus_amount:-minus_amount]

print(int(sum(info)/len(info)), info[-1])

