def load_data():
    with open('data.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def parse_instruction(line):
    return line[:3], int(line[4:])


def step_seen_before(history, i):
    return i in history


def get_pos_and_acc_movements(line):
    code, value = parse_instruction(line)
    if code == 'acc':
        movements = (1, value)
    if code == 'nop':
        movements = (1, 0)
    if code == 'jmp':
        movements = (value, 0)
    return movements


def increment_pos_and_acc_using_instruction(instruction, pos, acc):
    pos_delta, acc_delta = get_pos_and_acc_movements(instruction)
    pos += pos_delta
    acc += acc_delta
    return pos, acc


def main():
    data = load_data()

    acc, pos, history = 0, 0, []
    while True:
        if step_seen_before(history, pos):
            break
        
        history.append(pos)
        instruction = data[pos]
        pos, acc = increment_pos_and_acc_using_instruction(instruction, pos ,acc)
    
    print(acc)
    return


if __name__ == '__main__':
    main()
