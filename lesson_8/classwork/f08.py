def c(start, stop):
    if start < stop:
        return 0
    elif start == stop:
        return 1
    else:
        return c(start, stop+1) + c(start, stop * 2) + c(start, (stop * 2) + 1)


print(c(55, 6))