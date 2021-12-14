with open('DZ5.txt', 'r') as file:
    info = list(map(int, file.read().split('\n')[0:-1]))
    # pos = None
    # max_num = -10000
    # counter = 1
    # for i in range(len(info)):
    #     if max_num < info[i]:
    #         max_num = info[i]
    #         counter = 1
    #         pos = i + 1
    #     elif max_num == info[i]:
    #         counter += 1
    # print(counter, pos)
    max_num = max(info)
    pos = info.index(max_num)
    amount = info.count(max_num)
    print(amount, pos+1)
