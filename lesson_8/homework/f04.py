def executor(string):
    return sum(list(map(int, list(string.replace('21', '5')))))


print(executor('2121211212111211'))
