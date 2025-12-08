class BeamSplitter:

    beam_space: list[list[str]] = []
    beam_row = []

    def __init__(self, beam_map: str):
        self.beam_space = [list(row) for row in beam_map.split("\n")]

        self.beam_row = [False] * len(self.beam_space[0])

        # beam source
        find_s_idx = self.beam_space[0].index("S")
        self.beam_row[find_s_idx] = True

    def analyse_row(self, row_idx):
        count_splitter = 0

        for idx, space_item in enumerate(self.beam_space[row_idx]):
            if space_item != "^":
                continue

            if not self.beam_row[idx]:
                continue
            else:
                count_splitter += 1

            if idx == 0:
                self.beam_row[idx + 1] = True
            elif idx == len(self.beam_row) - 1:
                self.beam_row[idx - 1] = True
            else:
                self.beam_row[idx + 1] = True
                self.beam_row[idx - 1] = True

            self.beam_row[idx] = False

        return count_splitter

    def analyse_entire_map(self):
        total_splitter_hit = 0

        for row_idx in range(1, len(self.beam_space)):
            total_splitter_hit += self.analyse_row(row_idx)

        return total_splitter_hit


example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

beam_splitter_test = BeamSplitter(example)

assert beam_splitter_test.analyse_entire_map() == 21

challenge_map = open("./day_7/test.txt").read()
beam_splitter_challenge = BeamSplitter(challenge_map)

print(f"Challenge result: {beam_splitter_challenge.analyse_entire_map()}")
