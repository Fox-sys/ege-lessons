with open('4.txt') as file:
    content = list(map(int, file.read().split('\n')[1:]))
    amounts = {}
    for i in range(1, 100):
        amounts[str(i)] = content.count(i)

pairs = 0
for i in range(1, 50):
    pairs += min(amounts[str(i)], amounts[str(100-i)])
pairs += amounts['50'] // 2
print(pairs)
