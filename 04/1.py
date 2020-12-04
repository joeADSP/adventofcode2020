with open('data.txt', 'r') as f:
    data = f.read()

data = data.split('\n\n')
# data = [list(x.replace('\n', '')) for x in data]


targets = ('byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:')

count = 0

for item in data:
    allowed = True
    for target in targets:
        if target not in item:
            allowed = False
            break
    if allowed == True:
        count += 1

print(count)