PREAMBLE_SIZE = 25


def load_data():
    with open('data.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def main():
    counter = 0
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

    batch_size = 2
    found = False
    larger = []  # store pos values that lead to contiguous_sum > value
    while not found:
        # As we're increasing batch_size, might as well skip positions that lead to > value
        # when using a smaller batch_size.
        positions = [x for x in range(0, len(data) - batch_size + 1) if x not in larger]
        for pos in positions:
            counter += 1
            section = data[pos:pos+batch_size]
            contiguous_sum = sum(section)
            if contiguous_sum == value:
                found = True
                break
            if contiguous_sum > value:
                larger.append(pos)
        batch_size += 1

    if found:
        answer = max(section) + min(section)
        print(answer)
        print(counter)

    return


if __name__ == '__main__':
    main()
