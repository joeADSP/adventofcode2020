def load_data():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()
    return data


def parse_instruction(instruction):
    command = instruction[:1]
    units = int(instruction[1:])
    return command, units


class Ferry:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._vector_x = 1
        self._vector_y = 0

    def move_east(self, units):
        self._x += units
        return

    def move_west(self, units):
        self._x -= units
        return

    def move_north(self, units):
        self._y += units
        return

    def move_south(self, units):
        self._y -= units
        return

    def forward(self, units):
        self._x += self._vector_x * units
        self._y += self._vector_y * units
        return

    def rotate_clockwise(self, degrees):
        self._rotate(degrees)
        return

    def rotate_anticlockwise(self, degrees):
        self._rotate(360 - degrees)
        return

    def _rotate(self, degrees):
        steps = degrees // 90
        for i in range(steps):
            self._vector_x, self._vector_y = self._vector_y, -self._vector_x
        return

    @property
    def manhattan_distance(self):
        return abs(self._x) + abs(self._y)


def main():
    data = load_data()
    ferry = Ferry()
    for instruction in data:
        command, units = parse_instruction(instruction)
        if command == "N":
            ferry.move_north(units)
        if command == "E":
            ferry.move_east(units)
        if command == "S":
            ferry.move_south(units)
        if command == "W":
            ferry.move_west(units)
        if command == "F":
            ferry.forward(units)
        if command == "R":
            ferry.rotate_clockwise(units)
        if command == "L":
            ferry.rotate_anticlockwise(units)
    print(ferry.manhattan_distance)
    return


if __name__ == "__main__":
    main()
