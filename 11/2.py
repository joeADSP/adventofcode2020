import copy


def load_data():
    with open('data.txt', 'r') as f:
        temp = f.read().splitlines()
    data = []
    for row in temp:
        data.append([x for x in row])
    return data


def get_state(seat):
    if seat == 'L':
        return 'empty'
    if seat == '#':
        return 'occupied'
    if seat == '.':
        return 'floor'


def get_neighbours(x, y, data):
    height = len(data)
    width = len(data[0])
    neighbours = []
    for a in (-1,0,1):
        for b in (-1,0,1):
            if a == 0 and a == b:
                continue
            neighbour = None
            for i in range(1, height):
                if y + (a * i) < 0:
                    continue    
                if x + (b * i) < 0:
                    continue
                if y + (a * i) >= height:
                    continue
                if x + (b * i) >= width:
                    continue

                neighbour = get_cell(y+(a*i), x+(b*i), data)
                if neighbour != '.':
                    break
            neighbours.append(neighbour)
    return neighbours


def get_cell(y, x, data):
    return data[y][x]


def get_next_state(current_state, neighbours):
    if current_state == 'empty':
        if neighbours.count('#') == 0:
            return '#'
    if current_state == 'occupied':
        if neighbours.count('#') >= 5:
            return 'L'
    return current_state


def main():
    data = load_data()
    i = 0
    count_changes = -1
    while count_changes != 0:
        count_changes = 0
        next_stage = copy.deepcopy(data)
        for y, row in enumerate(data):
            for x, seat in enumerate(row):
                current_state = get_state(seat)
                neighbours = get_neighbours(x, y, data)
                next_state = get_next_state(current_state, neighbours)
                if next_state != current_state:
                    count_changes += 1
                    next_stage[y][x] = next_state

        print(count_changes)
        data = copy.deepcopy(next_stage)
        i += 1
    
    count_occupied = 0
    for row in data:
        for cell in row:
            if cell == '#':
                count_occupied += 1
    print(count_occupied)
    return


if __name__ == '__main__':
    main()
