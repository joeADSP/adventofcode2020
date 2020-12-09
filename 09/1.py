
PREAMBLE_SIZE = 25


def load_data():
    with open('data.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def main():
    data = [int(x) for x in load_data()]
    for pos in range(PREAMBLE_SIZE, len(data)):
        value = data[pos]
        section = data[pos-PREAMBLE_SIZE:pos]
        for item in section:
            ok = False
            if (value - item) in section:
                ok = True
                break
        if not ok:
            break
    print(value)
    return


if __name__ == '__main__':
    main()
