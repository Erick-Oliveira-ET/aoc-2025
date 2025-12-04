class JoltCalculator:
    def max_joltage_per_bank(self, bank: str) -> int:
        decimal_idx = 0
        unit_idx = 1

        for curr_idx in range(2, len(bank)):
            if bank[decimal_idx] < bank[curr_idx] and curr_idx != len(bank) - 1:
                decimal_idx = curr_idx
                unit_idx = decimal_idx + 1
                continue

            if int(bank[decimal_idx] + bank[unit_idx]) < int(
                bank[decimal_idx] + bank[curr_idx]
            ):
                unit_idx = curr_idx
                continue

        return int(bank[decimal_idx] + bank[unit_idx])

    def sum_bank_collection(self, banks: list[str]) -> int:
        result_sum = 0

        for bank in banks:
            result_sum += self.max_joltage_per_bank(bank)

        return result_sum


jolt_calculator = JoltCalculator()

assert jolt_calculator.max_joltage_per_bank("987654321111111") == 98
assert jolt_calculator.max_joltage_per_bank("811111111111119") == 89
assert jolt_calculator.max_joltage_per_bank("234234234234278") == 78
assert jolt_calculator.max_joltage_per_bank("818181911112111") == 92

assert (
    jolt_calculator.sum_bank_collection(
        ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    )
    == 357
)

file_lines = open("./day_3/test.txt").read().split("\n")

print(jolt_calculator.sum_bank_collection(file_lines))
