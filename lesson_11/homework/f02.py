with open('dz2.txt') as file:
    raw = file.read().split('\n')
    k = list(map(int, raw[0].split()))[1]
    info = [list(map(int, i.split())) for i in raw[1:]]
    info = sorted(info, key=lambda x: [x[1]/x[0], -x[0]])
    print(info)

mass = 0
max_mass = 0
max_price = 0
for i in info[0:k]:
    mass += i[0]
    if max_mass < i[0]:
        max_mass = i[0]
        max_price = i[1]
print(max_price, mass)
