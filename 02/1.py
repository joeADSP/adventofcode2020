with open('data.txt', 'r') as f:
    data = f.readlines()

data = [x.replace('\n', '') for x in data]

correct = 0

for line in data:
    password = line.split(':')[1].strip()
    allowed_range = [int(x) for x in line.split(':')[0].split(' ')[0].split('-')]
    character = line.split(':')[0].split(' ')[1]
    count = password.count(character)
    if count >= allowed_range[0] and count <= allowed_range[1]:
        correct += 1

print(correct)