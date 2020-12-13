def load_data():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()
    return data


def main():
    data = load_data()

    pairs = []
    for i, time in enumerate(data[1].split(',')):
        if time == 'x':
            continue
        pairs.append((int(time), int(i) + 1))

    print(pairs)
    n = 1
    step = 1
    for num, j in pairs:
        while (n + j) % num != 0:
            n += step
        step *= num
    print(n+1)
    return


if __name__ == "__main__":
    main()
