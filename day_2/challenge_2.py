from enum import Enum


class IsMultiple(Enum):
    PRIME = "prime"
    ODD = "odd"
    EVEN = "even"


class MultiplesTable:
    multiple_table = {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4]}
    prime_table = set()

    def is_multiple_of(self, num: int) -> list[int]:
        if num in self.multiple_table:
            return self.multiple_table[num]

        divisible_by = 1

        while num // divisible_by and divisible_by <= num // 2:
            if num % divisible_by == 0:
                self.add_num_mult_table(num, divisible_by)

            divisible_by += 1

        return self.multiple_table[num]

    def is_what(self, num: int) -> IsMultiple:
        if num % 2 == 0:
            return IsMultiple.EVEN

        if num in self.prime_table:
            return IsMultiple.PRIME

        return IsMultiple.PRIME if self.is_prime(num) else IsMultiple.ODD

    def is_prime(self, num: int) -> bool:
        divisible_by = 2

        while num // divisible_by and divisible_by < num // 2:
            if num % divisible_by == 0:
                return False

            divisible_by += 1

        self.prime_table.add(num)
        return True

    def add_num_mult_table(self, num, div):
        if num in self.multiple_table:
            self.multiple_table[num].append(div)
        else:
            self.multiple_table[num] = [div]


multiples_table = MultiplesTable()


class Decoder:
    # Invalid IDs start with zero or have two repeating sequences
    # "11-22" -> [11, 22]
    def find_invalid_id_in_range(self, range_str: str) -> list[int] | None:
        start, finish = range_str.split("-")

        return self.generate_invalid(start, finish)

    def generate_invalid(self, start, finish) -> list[int]:
        current = start

        invalids = []

        while True:
            is_what = multiples_table.is_what(len(current))

            if is_what == IsMultiple.PRIME:
                for result in self.generate_prime_pattern(current, start, finish):
                    invalids.append(result)

            if is_what == IsMultiple.ODD or is_what == IsMultiple.EVEN:
                for result in self.generate_non_odd_pattern(current, start, finish):
                    invalids.append(result)

            current = self._generate_new_invalid(current)

            if int(current) > int(finish):
                return invalids

    def _increment_half_and_duplicate(self, current: str):
        half = int(current[: len(current) // 2]) + 1
        half = str(half)

        return half + half

    def generate_prime_pattern(self, current, start, finish) -> list[int]:
        # Primes len can only have repeating numbers

        invalids = set()
        new_current = current[0] * len(current)

        while len(current) == len(new_current):
            if int(new_current) > int(finish):
                break

            if int(new_current) >= int(start) and len(new_current) > 1:
                invalids.add(int(new_current))

            new_current = str(int(new_current[0]) + 1) * len(current)

        return list(invalids)

    def generate_non_odd_pattern(self, current, start, finish) -> list[int]:
        invalids = set()

        multiples = multiples_table.is_multiple_of(len(current))

        for multiple in multiples:
            if multiple > len(current) // 2:
                break

            new_current = (current[:multiple]) * (len(current) // multiple)
            while True:
                if int(new_current) > int(finish):
                    break
                if int(new_current) >= int(start) and len(new_current) > 1:
                    invalids.add(int(new_current))

                new_current = (str(int(new_current[:multiple]) + 1)) * (
                    (len(new_current) // multiple)
                )

        return list(invalids)

    def _is_lower(self, current: str, upper: str) -> bool:
        return int(current) < int(upper)

    def _is_invalid(self, seq: str):
        step_size = 1

        while True:
            if len(seq) % step_size != 0:  # not divisible by step_size
                step_size += 1
                continue

            if step_size > len(seq) // 2:
                return False

            for i in range(step_size):
                for jump in range(1, len(seq) / step_size):
                    if seq[i] != seq[i + step_size * jump]:
                        step_size += 1
                        continue

            return True

    def _matching_len(self, seq1: str, seq2: str):
        for idx, (char_1, char_2) in enumerate(zip(seq1, seq2)):
            if char_1 != char_2:
                return idx

    def _generate_new_invalid(self, current: str):
        return "1" + "0" * len(current)

    def invalid_sum(self, multiple_ranges: list[str]):
        all_invalids = set()

        for range_str in multiple_ranges:
            invalid_list = self.find_invalid_id_in_range(range_str)
            invalid_list.sort()
            print(f"{range_str} -> {invalid_list}")
            for invalid in invalid_list:
                all_invalids.add(invalid)

        return sum(list(all_invalids))


decoder = Decoder()
assert decoder.find_invalid_id_in_range("11-22") == [11, 22]
assert decoder.find_invalid_id_in_range("95-115") == [99, 111]
assert decoder.find_invalid_id_in_range("998-1012") == [999, 1010]
assert decoder.find_invalid_id_in_range("1188511880-1188511890") == [1188511885]
assert decoder.find_invalid_id_in_range("222220-222224") == [222222]
assert decoder.find_invalid_id_in_range("446443-446449") == [446446]
assert decoder.find_invalid_id_in_range("38593856-38593862") == [38593859]
assert decoder.find_invalid_id_in_range("1698522-1698528") == []
assert decoder.find_invalid_id_in_range("565653-565659") == [565656]
assert decoder.find_invalid_id_in_range("824824821-824824827") == [824824824]
assert decoder.find_invalid_id_in_range("2121212118-2121212124") == [2121212121]

assert (
    decoder.invalid_sum(
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(
            ","
        )
    )
    == 4174379265
)

print("Complete test successfully!")

print("\n\nRunning challenge (test.txt)")

file = open("./day_2/test.txt").read()
# file only has one line
ranges_list = file.split(",")

challenge_invalid_sum = decoder.invalid_sum(ranges_list)

print(f"The total invalid sum is {challenge_invalid_sum}")
