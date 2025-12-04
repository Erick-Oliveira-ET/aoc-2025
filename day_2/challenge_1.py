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
            is_odd_len = len(current) % 2 == 1

            if is_odd_len:
                # go to next bigger even
                len_bigger_even = len(current) + 1
                half_len_even = len_bigger_even // 2
                current = ("1" + "0" * (half_len_even - 1)) * 2

            if not self._is_invalid(current):
                current = current[: len(current) // 2] * 2

            if int(current) > int(finish):
                return invalids

            if int(current) >= int(start):
                invalids.append(int(current))

            current = self._increment_half_and_duplicate(current)

    def _increment_half_and_duplicate(self, current: str):
        half = int(current[: len(current) // 2]) + 1
        half = str(half)

        return half + half

    def _is_lower(self, current: str, upper: str) -> bool:
        return int(current) < int(upper)

    def _is_invalid(self, seq: str):
        return seq[: len(seq) // 2] == seq[len(seq) // 2 :]

    def _matching_len(self, seq1: str, seq2: str):
        for idx, (char_1, char_2) in enumerate(zip(seq1, seq2)):
            if char_1 != char_2:
                return idx

    def invalid_sum(self, multiple_ranges: list[str]):
        invalid_sum = 0

        for range_str in multiple_ranges:
            for invalid in self.find_invalid_id_in_range(range_str):
                invalid_sum += invalid

        return invalid_sum


decoder = Decoder()
assert decoder.find_invalid_id_in_range("11-22") == [11, 22]
assert decoder.find_invalid_id_in_range("95-115") == [99]
assert decoder.find_invalid_id_in_range("998-1012") == [1010]
assert decoder.find_invalid_id_in_range("1188511880-1188511890") == [1188511885]
assert decoder.find_invalid_id_in_range("222220-222224") == [222222]
assert decoder.find_invalid_id_in_range("446443-446449") == [446446]
assert decoder.find_invalid_id_in_range("38593856-38593862") == [38593859]
assert decoder.find_invalid_id_in_range("1698522-1698528") == []
assert decoder.find_invalid_id_in_range("565653-565659") == []
assert decoder.find_invalid_id_in_range("824824821-824824827") == []
assert decoder.find_invalid_id_in_range("2121212118-2121212124") == []

assert (
    decoder.invalid_sum(
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(
            ","
        )
    )
    == 1227775554
)

print("Complete test successfully!")

print("Running challenge (test.txt)")

file = open("./day_2/test.txt").read()
# file only has one line
ranges_list = file.split(",")

print(f"The total invalid sum is {decoder.invalid_sum(ranges_list)}")
