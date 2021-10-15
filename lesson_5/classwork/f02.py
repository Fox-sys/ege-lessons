def get_data():
    with open('5.txt', 'r') as f:
        result = list(map(int, f.read().split('\n')))
    return result


def check_pair(a, b):
    if a % 3 == 0 or b % 3 == 0:
        return True
    else:
        return False

ls = []
data = get_data()
for i in range(len(data)):
    try:
        if check_pair(data[i], data[i+1]):
            ls.append([data[i], data[i+1]])
    except IndexError:
        pass

mx = -100000
for i in ls:
    if sum(i) > mx:
        mx = sum(i)

print(len(ls), mx)
