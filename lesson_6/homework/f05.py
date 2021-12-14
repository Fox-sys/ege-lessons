with open('DZ3.txt') as file:
    info = list(map(int, file.read()))

counter = 0
for i in range(0, len(info), 5):
    if info[i] < info[i+1] < info[i+2] < info[i+3] < info[i+4] < info[i+4] < info[i+5] > info[i+6]:
        counter += 1

print(counter)