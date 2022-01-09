def a():
    with open('01_B.txt') as file:
        data = file.read().split('\n')[1:]
        min_dif = 10000
        sum_nums = 0
        for i in data:
            pairs = list(map(int, i.split()))
            num = max(pairs)
            dif = max(pairs) - min(pairs)
            if dif % 3 != 0 and dif < min_dif:
                min_dif = dif
            sum_nums += num
        if sum_nums % 3 == 0:
            sum_nums -= min_dif
    return sum_nums


def b():
    with open('dz01_B.txt') as file:
        data = file.read().split('\n')[1:]
        min_dif_1 = 10000
        min_dif_2 = 10000
        sum_nums = 0
        for i in data:
            pairs = list(map(int, i.split()))
            num = max(pairs)
            dif = max(pairs) - min(pairs)
            if dif % 3 == 2 and dif < min_dif_2:
                min_dif_2 = dif
            if dif % 3 == 1 and dif < min_dif_1:
                min_dif_1 = dif
            sum_nums += num
        if sum_nums % 3 == 2:
            sum_nums -= min_dif_2
        elif sum_nums % 3 == 1:
            sum_nums -= min_dif_1
    return sum_nums
