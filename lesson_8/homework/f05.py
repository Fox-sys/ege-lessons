a = '1' * 44 + '2' * 21

while '111' in a:
    a = a.replace('111', '2')
    a = a.replace('22', '1')

print(a)