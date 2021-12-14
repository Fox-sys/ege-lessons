def c(start, stop):
    if start < stop:
        return 0
    elif start == stop:
        return 1
    else:
        return c(start, stop+2) + c(start, stop+5)


print(c(23, 2))
