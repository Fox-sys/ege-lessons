def check_num(num):
    return str(num)[-1] == '9' and num > 0


with open('17-204.txt', 'r') as file:
    data = list(map(int, file.read().split('\n')))
    max_sum = -100000
    counter = 0
    for i in range(1, len(data)-1):
        num = data[i]
        if check_num(num) and not (check_num(data[i-1]) or check_num(data[i+1])):
            counter += 1
            max_sum = max(max_sum, sum(data[i-1:i+2]))

print(max_sum, counter)