print('c a d b')

for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            for d in (0, 1):
                if ((a and b) == (not c)) and (b <= d) and c:
                    print(c, a, d, b)

# cadb
