# def check_for_current(num):
#     pairs_amount = 0
#     pairs = []
#     for j in range(num + 1, len(data)):
#         if data[num] * data[j] % 6 == 0:
#             pairs_amount += 1
#             pairs.append((data[num], data[j]))
#     return pairs_amount, pairs
#
#
# with open('dz02_A.txt') as file:
#     data = list(map(int, file.read().split('\n')[1:]))
#     pairs_amount = 0
#     pairs = []
#     for i in range(len(data)):
#         result = check_for_current(i)
#         pairs_amount += result[0]
#         pairs += result[1]
#         # for j in range(i + 1, len(data)):
#         #     if data[i] * data[j] % 6 == 0:
#         #         pairs_amount += 1
#     print(pairs_amount, pairs)

# A: 47
# B: 745460178

with open('dz02_C.txt') as file:
    data = list(map(int, file.read().split('\n')[1:]))
    n_2 = 0
    n_3 = 0
    n_6 = 0
    for i in data:
        if i % 2 == 0 and i % 6 != 0:
            n_2 += 1
        elif i % 3 == 0 and i % 6 != 0:
            n_3 += 1
        elif i % 6 == 0:
            n_6 += 1
    n = len(data)
    k = n - n_6
    print(n_2 * n_3 + ((n * (n - 1))//2 - (k * (k-1)//2)))
    print(n_2 * n_3 + n_6 * k + (n_6 * (n_6-1))//2)

