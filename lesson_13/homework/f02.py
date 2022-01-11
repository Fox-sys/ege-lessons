with open('dz3b.txt') as file:
    data = list(map(int, file.read().split('\n')[1:]))
    dc = [0 for i in range(12)]
    for i in data:
        dc[i % 12] += 1
    pairs = (dc[0] * (dc[0] - 1))//2 + (dc[6] * (dc[6] - 1))//2
    for i in range(1, len(dc)//2):
        pairs += dc[i] * dc[-i]
    print(pairs)
