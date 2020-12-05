

def load_boarding_passes():
    with open('data.txt', 'r') as f:
        data = f.readlines()
    return [x.replace('\n', '') for x in data]


def binary_locate(n, codes, markers):
    lower = 0
    upper = 2**n - 1
    for i, code in enumerate(codes):
        diff = 2**(n - i - 1)
        if diff == 1:
            if code == markers[0]:
                return lower
            if code == markers[1]:
                return upper
        halfway = lower + diff
        if code == markers[0]:
            upper = halfway - 1
        if code == markers[1]:
            lower = halfway
    return


def get_seat_id(row, col):
    return (row * 8) + col


def main():
    seat_ids = []
    boarding_passes = load_boarding_passes()
    for boarding_pass in boarding_passes:
        row_codes = boarding_pass[:7]
        col_codes = boarding_pass[7:]

        row = binary_locate(7, row_codes, ('F', 'B'))
        col = binary_locate(3, col_codes, ('L', 'R'))

        seat_id = get_seat_id(row, col)
        seat_ids.append(seat_id)
    
    for i in range(128):
        for j in range(8):
            id = get_seat_id(i, j)
            if id not in seat_ids:
                if (id + 1 in seat_ids) and (id - 1 in seat_ids):
                    print(id)
    return


if __name__ == '__main__':
    main()
