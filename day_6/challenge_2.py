operations_map = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
}


class CephalopodTable:
    numbers_table: list[list[int]]
    operations_row: list[str]  # * or +

    def math(self, raw_table: str):

        lines = [list(row) for row in raw_table.split("\n")]

        self.operations_row = lines[-1]

        total_for_column = []
        temp_num_for_op = []
        operation_idx = len(self.operations_row) - 1

        for x in range(len(lines[0]) - 1, -1, -1):
            str_num = ""
            for y in range(len(lines) - 1):  # -> -1 operation line
                item = lines[y][x]
                if not item == " ":
                    str_num += lines[y][x]
            if str_num == "":
                continue

            temp_num_for_op.append(int(str_num))
            if x == operation_idx:
                operation = self.operations_row[operation_idx]

                if operation == "+":
                    total_for_column.append(sum(temp_num_for_op))
                else:
                    total = 1

                    for value in temp_num_for_op:
                        total *= value

                    total_for_column.append(total)

                temp_num_for_op = []

                # next operation idx

                self.operations_row[operation_idx] = " "
                while self.operations_row[operation_idx] == " " and operation_idx >= 0:
                    operation_idx -= 1

        print(total_for_column)

        return sum(total_for_column)


test = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

test_cephalopod_table = CephalopodTable().math(test)
assert test_cephalopod_table == 3263827

challenge = open("./day_6/test.txt").read()
challenge_ceph_table = CephalopodTable().math(challenge)
print(f"Answer: {challenge_ceph_table}")
