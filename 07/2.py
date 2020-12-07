def load_data():
    with open('data.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def search_tree_for_gold_bag(bag, bag_map):
    if bag == ' other bag':
        return False
    contents = bag_map[bag]
    if 'shiny gold bag' in contents:
        return True
    for item in contents:
        found = search_tree_for_gold_bag(item, bag_map)
        if found:
            return found
    return found


def bag_counter(bag, bag_map, muliplier, total):
    if bag == 'o other bag':
        return 0
    contents = bag_map[bag]
    node_total = 0
    for item in contents:
        num = item[0]
        node_total += num * muliplier
        node_total += muliplier * bag_counter(item[1], bag_map, item[0], total)
    total += node_total
    return total


def main():
    data = load_data()
    bag_map = {}
    for line in data:
        first_term = line.replace('.', '').split('contain')[0].strip().replace('bags', 'bag')
        contents = []
        for section in line.replace('.', '').replace('bags', 'bag').split('contain')[1].split(','):
            try:
                n = int(section[:2])
            except ValueError:
                n = 0
            contents.append([n, section[2:].strip()])
        bag_map[first_term] = contents
    
    count = bag_counter('shiny gold bag', bag_map, 1, 0)
    print(count)
    return


if __name__ == '__main__':
    main()
