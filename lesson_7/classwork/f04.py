def find_divs(n) -> (list, None):
    i = 2
    counter = 0
    result = []
    while i ** 2 < n:
        if n % i == 0:
            result.append(i)
            result.append(n//i)
            counter += 2
        if counter > 2:
            return None
        i += 1
    if i ** 2 == n:
        return None
    return result


for i in range(174457, 174506):
    divs = find_divs(i)
    if divs:
        print(divs)

