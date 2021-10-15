def num_system(x, p):
    result = ''
    while x > 0:
        result += str(x % p)
        x //= p
    return result


num = 1 * 7 ** 2

print(num_system(6, 3))
