with open('data.txt', 'r') as f:
    data = f.readlines()

data = [list(x.replace('\n', '')) for x in data]

TREE = '#'
WIDTH = len(data[0])
HEIGHT = len(data)

tree_count = 0

move = (3, 1)
position = [0, 0]

while position[1] < HEIGHT:
    # Move
    position[0] = (position[0] + move[0]) % WIDTH
    position[1] = (position[1] + move[1])

    if position[1] < HEIGHT:
        space = data[position[1]][position[0]]
        if space == TREE:
            tree_count += 1

print(tree_count)
