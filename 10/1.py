

def load_data():
    with open('practice_data1.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def main():
    data = [int(x) for x in load_data()]

    data.sort()
    data.insert(0, 0)
    data.append(max(data) + 3)
    counts = [len([x for x in [data[i + 1] - data[i] for i in range(len(data) - 1)] if x == y]) for y in (1, 3)]
    print(counts[0]*counts[1])
    return


if __name__ == '__main__':
    main()
