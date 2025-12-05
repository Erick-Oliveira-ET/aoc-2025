class ForkLiftMap:
    max_adjacent_rolls = 4
    rolls_map: list[str]
    new_map: list[str]

    def __init__(self, rolls_map: str):
        self.rolls_map = self.str_map_to_array(rolls_map)
        self.new_map = self.rolls_map

    def rolls_accessible(self):
        count_rolls_accessible = 0
        last_cycle_count = -1

        while last_cycle_count != count_rolls_accessible:
            last_cycle_count = count_rolls_accessible
            self.rolls_map = self.new_map

            for y in range(len(self.rolls_map)):
                for x in range(len(self.rolls_map[0])):
                    if self.rolls_map[y][x] is not "@":
                        continue

                    if self._count_rolls_adjacent(x, y) < self.max_adjacent_rolls:
                        count_rolls_accessible += 1
                        self.new_map[y][x] = "X"

        return count_rolls_accessible

    def _count_rolls_adjacent(self, x, y):
        adjacent_relative = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        count_adjacent = 0

        for x_r, y_r in adjacent_relative:
            if self._is_roll_in_position(x + x_r, y + y_r):
                count_adjacent += 1

        return count_adjacent

    def _is_roll_in_position(self, x, y):
        if x < 0 or y < 0:
            return False

        if x > len(self.rolls_map[0]) - 1 or y > len(self.rolls_map) - 1:
            return False

        if self.rolls_map[y][x] == "@":
            return True

        return False

    def print_new_map(self):
        print("\n".join(["".join(row) for row in self.new_map]))

    def str_map_to_array(self, str_map: str) -> list[str]:
        return [list(row) for row in str_map.split("\n")]


test_map = """@@@
@.@
@@@"""

assert ForkLiftMap(test_map).rolls_accessible() == 8
test_map = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

example_test = ForkLiftMap(test_map)
example_rolls_accessible = example_test.rolls_accessible()

print(example_test.print_new_map())

assert example_rolls_accessible == 43

file = open("./day_4/test.txt").read()

challenge_map = ForkLiftMap(file)
print(challenge_map.rolls_accessible())
