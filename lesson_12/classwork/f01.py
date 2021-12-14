win_num = int(input())

matrix = [[None for j in range(win_num*2)] for i in range(win_num*2)]

for i in range(0, win_num*2):
    for j in range(0, win_num*2):
        if i + j >= win_num:
            matrix[i][j] = 0

print(matrix)

for s in range(win_num-1, 0, -1):
    for i in range(1, s, 1):
        j = s - i
        print(f'{j} {s} {i}')
        next = [matrix[i+1][j], matrix[i*2][j], matrix[i][j+1], matrix[i][j*2]]
        print(next)
        odd = [x for x in next if x % 2 == 1]
        even = [x for x in next if x % 2 == 0]
        if len(even) == 0:
            matrix[i][j] = max(odd) + 1
        else:
            matrix[i][j] = min(even) + 1

    # if matrix[i*2] % 2 == 0 and matrix[i+1] % 2 == 0:
    #     matrix[i] = min(matrix[i*2], matrix[i+1]) + 1
    # elif matrix[i*2] % 2 == 0:
    #     matrix[i] = matrix[i*2] + 1
    # elif matrix[i+1] % 2 == 0:
    #     matrix[i] = matrix[i+1] + 1
    # else:
    #     matrix[i] = max(matrix[i*2], matrix[i+1]) + 1

with open('1.txt', 'a') as file:
    for i in range(1, win_num):
        for j in range(1, win_num):
            file.write(f'{matrix[i][j]};')
        file.write('\n')
