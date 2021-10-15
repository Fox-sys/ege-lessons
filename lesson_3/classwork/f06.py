num = str(bin(4**2016-2**2018+8**800-80))
ones = ''
print(num)
for i in num:
    if i == '1':
        ones += i
print(len(ones))
