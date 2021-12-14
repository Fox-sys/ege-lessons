with open('DZ4.txt', 'r') as file:
    info = file.read()


counter = 0
for i in range(len(info)-5):
    if info[i: i+5] == info[i+4:i-1:-1]:
        counter += 1
print(counter)
