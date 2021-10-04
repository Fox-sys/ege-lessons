COUNTER = 0


def F(n):
    global COUNTER
    if n > 0:
        COUNTER += n
        F(n - 2)
        F(n // 3)


F(7)
print(COUNTER)
