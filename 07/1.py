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


def main():
    data = load_data()
    bag_map = {}
    for line in data:
        first_term = line.replace('.', '').split('contain')[0].strip().replace('bags', 'bag')
        contents = [x.strip()[2:].replace('bags', 'bag') for x in line.replace('.', '').split('contain')[1].split(',')]
        bag_map[first_term] = contents

    total = sum([search_tree_for_gold_bag(bag, bag_map) for bag in bag_map.keys()])
    print(total)
    return


if __name__ == '__main__':
    main()
