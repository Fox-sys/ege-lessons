with open('1.txt') as file:
    content = file.read().split('\n')
    max_buffer = int(content[0].split()[0])
    content = sorted(list(map(int, content[1:])))

current_buffer = 0
amount = 0
for i in content:
    if max_buffer < current_buffer + i:
        break
    current_buffer += i
    amount += 1

print(amount)
