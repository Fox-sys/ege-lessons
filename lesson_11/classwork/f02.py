with open('3.txt') as file:
    content = [list(map(int, i.split())) for i in file.read().split('\n')[1:]]
    content = sorted(content, key=lambda x: [-x[0], x[1]])

for i in range(len(content)):
    if content[i+1][1] - content[i][1] == 3 and content[i][0] == content[i+1][0]:
        print(content[i][0], content[i][1]+1)
        break
