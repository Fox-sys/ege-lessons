def c(start, stop):
    if stop < start:
        return 0
    elif start == stop:
        return 1
    elif stop % 2 == 0:
        return c(start, stop // 2) + c(start, stop-1)
    else:
        return c(start, stop - 1)


print(c(1, 10) * c(10, 21))
