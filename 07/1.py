def load_data():
    with open('data.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def main():
    data = load_data()
    bag_map = {}
    for line in data:
        first_term = line.replace('.', '').split('contain')[0].strip().replace('bags', 'bag')
        contents = [x.strip()[2:].replace('bags', 'bag') for x in line.replace('.', '').split('contain')[1].split(',')]
        bag_map[first_term] = contents

    winners = set()
    store = -1
    while len(winners) != store:
        store = len(winners)
        for k,v in bag_map.items():
            if k in winners:
                continue
            for bag in v:
                if bag in winners:
                    winners.add(k)
                    continue
            if 'shiny gold bag' in v:
                winners.add(k)
    print(len(winners))
    return


if __name__ == '__main__':
    main()
