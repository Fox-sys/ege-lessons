num = str(oct(64**10+2**90-16))
ones = ''
print(num)
for i in num:
    if i == '7':
        ones += i
print(len(ones))
