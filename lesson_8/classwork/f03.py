def c(start, stop):
    if stop < start:
        return 0
    elif start == stop:
        return 1
    elif str(stop)[-2] == '9':
        print('Привет, ты где то там, где не должен быть')
    else:
        return c(start, stop-1) + c(start, stop-10)


print(c(15, 28))
