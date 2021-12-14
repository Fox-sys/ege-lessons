def c(start, stop):
    if stop < start:
        return 0
    elif start == stop:
        return 1
    elif stop % 2 == 1:
        return c(start, stop-1) + c(start, stop-2) + c(start, (stop - 1) // 2)
    else:
        return c(start, stop-1) + c(start, stop-2)


print(c(2, 10))