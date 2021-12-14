def c(start, stop):
    if stop == 25 or stop < start:
        return 0
    elif start == stop:
        return 1
    elif stop % 2 == 0:
        return c(start, stop // 2) + c(start, stop-1)
    else:
        return c(start, stop - 1)


print(c(2, 14) * c(14, 29))
