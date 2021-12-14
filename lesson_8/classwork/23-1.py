def C(n0,n):
    if n<n0:
        return 0
    elif n==n0:
        return 1
    elif n % 3 == 0:
        return C(n0,n-1) + C(n0,n//3)
    else:
        return C(n0,n-1)

print(C(1,20))
