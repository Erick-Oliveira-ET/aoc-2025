def parse_fresh_id_ranges(fresh_id_ranges: list[str]) -> list[list[int]]:
    fresh_id_ranges_int = []
    for str_range in fresh_id_ranges:
        start, end = str_range.split("-")

        fresh_id_ranges_int.append([int(start), int(end)])

    return sorted(fresh_id_ranges_int, key=lambda x: x[0])


def merge_ranges(ranges: list[list[int]]):
    i = 0

    while i < len(ranges) - 1:
        curr_range = ranges[i]
        next_range = ranges[i + 1]

        if curr_range[0] <= next_range[0] <= curr_range[1] <= next_range[1]:
            next_range[0] = curr_range[0]

            ranges = ranges[:i] + ranges[i + 1 :]
            i -= 1

        elif next_range[0] <= curr_range[0] <= next_range[1] <= curr_range[1]:
            next_range[1] = curr_range[1]

            ranges = ranges[:i] + ranges[i + 1 :]
            i -= 1
        i += 1

    return ranges


def split_input_range_items(input_str: str):
    ranges, items = input_str.split("\n\n")

    return ranges.split("\n"), items.split("\n")


class Cafeteria:
    fresh_id_ranges: list[tuple[int]]
    items_ids: list[int]

    def __init__(self, fresh_id_ranges: list[str], items_ids: list[str]):
        parsed_fresh_id_ranges = parse_fresh_id_ranges(fresh_id_ranges)
        self.fresh_id_ranges = merge_ranges(parsed_fresh_id_ranges)

        self.items_ids = sorted([int(item) for item in items_ids])

    def count_fresh_ingredients(self):
        count = 0

        range_idx = 0
        item_idx = 0

        while range_idx < len(self.fresh_id_ranges) and item_idx < len(self.items_ids):
            item = self.items_ids[item_idx]
            curr_range = self.fresh_id_ranges[range_idx]

            if item < curr_range[0]:
                item_idx += 1
            if curr_range[0] <= item <= curr_range[1]:
                count += 1
                item_idx += 1
            elif curr_range[1] < item:
                range_idx += 1

        return count


example = """3 - 5
10 - 14
16 - 20
12 - 18

1
5
8
11
17
32"""

assert Cafeteria(*split_input_range_items(example)).count_fresh_ingredients() == 3

challenge = open("./day_5/test.txt").read()

print(Cafeteria(*split_input_range_items(challenge)).count_fresh_ingredients())
