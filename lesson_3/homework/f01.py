for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not (not x or y or (not z and w)):
                    print(f'{x}  {y}  {z}  {w}')

# x: 4
# y: 1
# z: 2
# w: 3
