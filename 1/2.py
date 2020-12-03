with open('data.txt', 'r') as f:
    data = f.readlines()

data = [int(x.replace('\n', '')) for x in data]


for i in data:
    for j in data:
        for k in data:
            if i == j or j == k or i == k:
                continue
            if i + j + k == 2020:
                print(i, j, k,  i+j+k, i*j*k)
                exit()