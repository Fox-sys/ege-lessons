from functools import lru_cache


@lru_cache(maxsize=None)
def F(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n % 2 == 0 and n > 1:
        return F(n-1) - F(n-2) + 3 * n
    elif n % 2 == 1 and n > 1:
        return F(n-2) - F(n-3) + 2 * n

print(F(80))

