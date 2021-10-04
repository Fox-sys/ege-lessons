a = 1024
b = 81
while b:
    a, b = b, a % b
print(a)
