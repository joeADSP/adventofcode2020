with open('data.txt', 'r') as f:
    data = f.readlines()

data = [int(x.replace('\n', '')) for x in data]

for i in data:
    for j in data:
        if i == j:
            continue
        if i + j == 2020:
            print(i, j, i+j, i*j)
            exit()