with open('data.txt', 'r') as f:
    data = f.read()

data = data.split('\n\n')

answers_count = sum([len(set.union(*[set(line) for line in section.split('\n')])) for section in data])

print(answers_count)