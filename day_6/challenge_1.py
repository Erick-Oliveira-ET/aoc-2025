operations_map = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
}


class CephalopodTable:
    numbers_table: list[list[int]]
    operations_row: list[str]  # * or +

    def __init__(self, raw_table: str):

        whole_table = []

        for i, row in enumerate(raw_table.split("\n")):
            whole_table.append([])
            for j, item in enumerate(row.split(" ")):
                if item == "":
                    continue

                if item == "*" or item == "+":
                    whole_table[i].append(item)

                else:
                    whole_table[i].append(int(item))

        self.numbers_table = whole_table[:-1]
        self.operations_row = whole_table[-1]

    def cephalopod_math(self):
        result = 0
        for i in range(len(self.numbers_table[0])):
            cum = 0 if self.operations_row[i] == "+" else 1
            for j in range(len(self.numbers_table)):
                if self.operations_row[i] == "+":
                    cum += self.numbers_table[j][i]
                else:
                    cum *= self.numbers_table[j][i]
            result += cum

        return result


test = """123 328  51 64  
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

test_cephalopod_table = CephalopodTable(test)
assert test_cephalopod_table.cephalopod_math() == 4277556

challenge = open("./day_6/test.txt").read()
challenge_ceph_table = CephalopodTable(challenge)
print(f"Answer: {challenge_ceph_table.cephalopod_math()}")
