with open('data.txt', 'r') as f:
    data = f.readlines()

data = [x.replace('\n', '') for x in data]

correct = 0

for line in data:
    password = line.split(':')[1].strip()
    positions = [int(x) - 1 for x in line.split(':')[0].split(' ')[0].split('-')]
    character = line.split(':')[0].split(' ')[1]
    if bool(password[positions[0]] == character) != bool(password[positions[1]] == character):
        correct += 1

print(correct)