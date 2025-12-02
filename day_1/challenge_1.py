file = open("./day_1/test.txt")

current_position = 50

class Movement:
    current_position = 50
    zero_count = 0
    
    # Example R30 or L20
    def move(self, movement_code: str):
        direction = movement_code[0]
        value = int(movement_code[1:])

        if direction == "R":
            new_position = (self.current_position + value) % 100
            print(f"R -> curr:{self.current_position} | {value=} | {new_position=}")
        else: 
            new_position = self.current_position - value % 100

            if new_position < 0:
                new_position += 100

            print(f"L -> curr:{self.current_position} | {value=} | {new_position=}")
        
        self._set_position(new_position)
    
    def _set_position(self, new_position):
        if new_position == 0:
            self.zero_count += 1
        
        self.current_position = new_position

movement = Movement()

for line in iter(file):
    print(line.removesuffix("\n"))
    movement.move(line.removesuffix("\n"))

# movement.move("R51")
# print(movement.current_position)
# movement.move("L2")
# print(movement.current_position)


print(movement.zero_count)
file.close()