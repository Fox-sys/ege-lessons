def func(x):
    nums = [int(x[0]) + int(x[1]), int(x[2]) + int(x[3])]
    nums = sorted(nums)
    result = ''
    result += str(nums[1])
    result += str(nums[0])
    return int(result)


for i in range(1000, 10000):
    if func(str(i)) == 1311:
        print(i)
        break