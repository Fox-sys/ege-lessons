with open('9.txt', 'r') as file:
    info = file.readline()

max_length = 1
current_length = 1

for i in range(4, len(info)):
    if info[i-2: i] == 'ad' or info[i-2: i] == 'da':
        current_length = 1
    else:
        current_length += 1
        if max_length < current_length:
            max_length = current_length

print(max_length)
