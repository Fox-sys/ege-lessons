def check_num(num):
    return len(list(num)) == len(set(num))


max_num = 15
min_num = 2000000
counter = 0
if __name__ == '__main__':
    num = 15
    while num <= 2000000:
        if not check_num(str(num)):
            counter += 1
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        num *= 2
    print(counter, max_num-min_num)