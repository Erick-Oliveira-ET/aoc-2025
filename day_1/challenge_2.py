file = open("./day_1/test.txt")

current_position = 50



class Movement:
    current_position = 50
    zero_count = 0
    dial_size = 100
    
    # Example R30 or L20
    def move(self, movement_code: str):
        direction = movement_code[0]
        value = int(movement_code[1:])

        full_revolutions, remainder = self._full_rev_remainder_calc(value)

        if direction == "R":
            new_position = (self.current_position + remainder) % self.dial_size

            passed_zero = 1 if self.current_position > new_position else 0

            print(f"{movement_code} -> curr:{self.current_position} | {value=} | {new_position=} | {full_revolutions=} | {passed_zero=}")
        else: 
            new_position = (self.current_position - remainder) % 100

            if new_position < 0:
                new_position += 100
            
            passed_zero = 1 if self.current_position < new_position else 0

            print(f"{movement_code} -> curr:{self.current_position} | {value=} | {new_position=} | {full_revolutions=} | {passed_zero=}")
        
        self._set_position(new_position, full_revolutions, passed_zero)

    def _full_rev_remainder_calc(self, value):
        full_revolution = 0

        if value > 100:
            full_revolution = int(value / self.dial_size)

        return full_revolution, int(value % self.dial_size)
    
    def _set_position(self, new_position, full_revolutions, passed_zero: int):
        if new_position == 0:
            self.zero_count += 1

        # current_position == 0 was counted on the run before and new_position == 0 will be counted on zero_count
        double_count = self.current_position == 0 or new_position == 0

        if double_count:
            passed_zero = 0

        self.zero_count += abs(full_revolutions) + passed_zero
        
        self.current_position = new_position

movement_test = Movement()

movement_test.move("L68")
movement_test.move("L30")
movement_test.move("R48")
movement_test.move("L5")
movement_test.move("R60")
movement_test.move("L55")
movement_test.move("L1")
movement_test.move("L99")
movement_test.move("R14")
movement_test.move("L82")

print(movement_test.zero_count)

if movement_test.zero_count != 6:
    raise Exception(f"Test failed -> expected 6, received {movement_test.zero_count}")

del movement_test

movement = Movement()

for line in iter(file):
    print(line.removesuffix("\n"))
    movement.move(line.removesuffix("\n"))

print(movement.zero_count)

file.close()