def c(start, stop):
    if stop < start:
        return 0
    elif stop == start:
        return 1
    else:
        return c(start, stop - 1) + c(start, stop - 2)


print(c(11, 17)*c(17, 29)+c(11, 23)*c(23, 29)-(c(11, 17)*c(17, 23)*c(23, 29)))
