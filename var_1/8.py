g = ("а", "в", "д", "п", "р")
i = 0
for a in g:
    for b in g:
        for c in g:
            for d in g:
                i += 1
                word = a + b + c + d
                if not 'а' in word and 'в' in word and 'д' in word and 'п' in word and 'р' in word:
                    print(i)

# 195
