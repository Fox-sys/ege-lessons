win_num = int(input())
S = int(input())

matrix = [None for i in range(S)]

matrix[1] = 0
matrix[0] = 0
matrix[2] = 1
for i in range(3, S):
    next = []
    if i % 2 == 0:
        next.append(matrix[i // 2])
    else:
        next.append(matrix[i - 2])
    if i % 3 == 0:
        next.append(matrix[i // 3])
    else:
        next.append(matrix[i - 3])

    odd = [x for x in next if x % 2 == 1]
    even = [x for x in next if x % 2 == 0]
    if len(even) == 0:
        matrix[i] = max(odd) + 1
    else:
        matrix[i] = min(even) + 1


with open('2.txt', 'a') as file:
    for i in range(1, S):
        file.write(f'{matrix[i]};')
        # file.write('\n')
