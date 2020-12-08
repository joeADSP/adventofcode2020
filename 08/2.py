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


def create_amended_data_with_flipped_element(code, data, target_line_id):
    amended_data = data.copy()
    flips = ('jmp', 'nop')
    for i, item in enumerate(flips):
        if code == item:
            amended_data[target_line_id] = amended_data[target_line_id].replace(item, flips[i - 1]) 
    return amended_data


def main():
    data = load_data()

    for target_line_id, line in enumerate(data):
        code, _ = parse_instruction(line)

        if code == 'acc':
            continue
        
        amended_data = create_amended_data_with_flipped_element(code, data, target_line_id)

        acc, pos, exit_properly, history = 0, 0, False, []
        while True:
            if step_seen_before(history, pos):
                break
            if pos == len(data):
                exit_properly = True
                break
            
            history.append(pos)
            instruction = amended_data[pos]
            pos, acc = increment_pos_and_acc_using_instruction(instruction, pos ,acc)
        
        if exit_properly:
            break
    print(acc)
    return


if __name__ == '__main__':
    main()
