with open('7.txt', 'r') as file:
    info = file.readline()

current_length = 1
max_length = 1
for i in range(len(info)-1):
    if info[i] != info[i+1]:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
    else:
        current_length = 1
print(max_length)
