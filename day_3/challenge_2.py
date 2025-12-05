class JoltCalculator:
    def max_joltage_per_bank(self, bank: str) -> int:
        digits_idx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        last_idx = len(bank) - 1

        for curr_idx in range(1, len(bank)):
            for digit_idx, digit in enumerate(digits_idx[:curr_idx]):
                units_needed_after = 11 - digit_idx
                units_left = last_idx - curr_idx

                # curr_idx is in the highest position
                # avoid duplication
                if digit == curr_idx:
                    break

                if bank[digit] < bank[curr_idx] and units_left >= units_needed_after:
                    digits_idx[digit_idx] = curr_idx

                    for count, idx in enumerate(range(digit_idx + 1, 12)):
                        digits_idx[idx] = (curr_idx + 1) + count

                    # Biggest unit already used curr_idx
                    break

        return self._str_digit_idx_to_int(digits_idx, bank)

    def _str_digit_idx_to_int(self, digits_idx: list[int], bank: str) -> int:
        bank_value = ""

        for digit_idx in digits_idx:
            bank_value += bank[digit_idx]

        return int(bank_value)

    def sum_bank_collection(self, banks: list[str]) -> int:
        result_sum = 0

        for bank in banks:
            result_sum += self.max_joltage_per_bank(bank)

        return result_sum


jolt_calculator = JoltCalculator()

assert jolt_calculator.max_joltage_per_bank("987654321111111") == 987654321111
assert jolt_calculator.max_joltage_per_bank("811111111111119") == 811111111119
assert jolt_calculator.max_joltage_per_bank("234234234234278") == 434234234278
assert jolt_calculator.max_joltage_per_bank("818181911112111") == 888911112111

assert (
    jolt_calculator.sum_bank_collection(
        ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    )
    == 3121910778619
)

file_lines = open("./day_3/test.txt").read().split("\n")

jolt_calculator = JoltCalculator()

print(jolt_calculator.sum_bank_collection(file_lines))
