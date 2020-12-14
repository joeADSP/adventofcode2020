import re


def load_data():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()
    return data


def set_bit_to_1(value, index):
    return value | (1 << index)


def set_bit_to_0(value, index):
    return value & ~(1 << index)


def apply_mask(value, mask):
    for i, item in enumerate(mask[::-1]):
        if item == 'X':
            continue
        if item == '1':
            fnc = set_bit_to_1
        if item == '0':
            fnc = set_bit_to_0

        value = fnc(value, i)
    return value


def main():
    data = load_data()
    memory = {}
    for line in data:
        if line.startswith('mask'):
            mask = line[len("mask = "):]
            continue
        position = int(re.findall(r"mem\[(\d*)\]", line)[0])
        value = int(re.findall(r"mem\[\d*\] = (\d*)", line)[0])
        memory[position] = apply_mask(value, mask)

    answer = sum(v for v in memory.values())
    print(answer)
    return


if __name__ == "__main__":
    main()
