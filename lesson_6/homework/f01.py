import re
with open('DZ1.txt') as file:
    info = file.read().split('\n')


def regular_result(info):
    """Решение с регулярками"""
    counter = 0
    for i in info:
        if re.findall(r'A.R', i):
            counter += 1
    return counter


def un_regular_result(info):
    """Решение без регулярок"""
    counter = 0
    for i in info:
        for j in range(len(i)-2):
            if i[j] == 'A' and i[j+2] == 'R':
                counter += 1
                break
    return counter
