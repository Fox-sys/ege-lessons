with open('DZ3.txt') as file:
    info = list(map(int, file.read()[0:-1]))

info = info + [0]
counter = 0
for i in range(1, len(info)-5):
    if info[i-1] >= info[i] < info[i+1] < info[i+2] < info[i+3] < info[i+4] >= info[i+5]:
        # print(f'{info[i - 1]} > {info[i]} < {info[i + 1]} < {info[i + 2]} < {info[i + 3]} < {info[i + 4]} > {info[i + 5]}')
        counter += 1
print(counter)
