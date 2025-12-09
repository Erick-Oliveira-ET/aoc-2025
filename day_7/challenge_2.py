class BeamSplitter:

    beam_space: list[list[str]] = None
    beam_row = None

    def __init__(self, beam_map: str):
        self.beam_space = [list(row) for row in beam_map.split("\n")]

        self.beam_row = []

        # beam source
        for item in self.beam_space[0]:
            self.beam_row.append(1 if item == "S" else 0)

    def analyse_row(self, row_idx):
        for idx, space_item in enumerate(self.beam_space[row_idx]):
            if space_item != "^":
                continue

            if not self.beam_row[idx]:
                continue

            if idx == 0:
                self.beam_row[idx + 1] += self.beam_row[idx]
            elif idx == len(self.beam_row) - 1:
                self.beam_row[idx - 1] += self.beam_row[idx]
            else:
                self.beam_row[idx + 1] += self.beam_row[idx]
                self.beam_row[idx - 1] += self.beam_row[idx]

            self.beam_row[idx] = 0

    def analyse_entire_map(self):
        total_splitter_hit = 0

        for row_idx in range(2, len(self.beam_space)):
            self.analyse_row(row_idx)
            self.print_row(row_idx)

        print(f"Total timelines: {self.beam_row}")

        return sum(self.beam_row)

    def print_row(self, row_idx: str):
        beam_row_temp = []
        for beam in self.beam_row:
            beam_row_temp.append(beam)

        space_row = list(beam_row_temp)
        for space_idx, space in enumerate(self.beam_space[row_idx]):
            if space == "^":
                space_row[space_idx] = space

        print("".join([str(item) for item in space_row]))

        print("".join([str(item) for item in beam_row_temp]))


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

assert beam_splitter_test.analyse_entire_map() == 40

second_example = """.......S.......
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
..............."""

beam_splitter_test = BeamSplitter(second_example)

assert beam_splitter_test.analyse_entire_map() == 20

challenge_map = open("./day_7/test.txt").read()
beam_splitter_challenge = BeamSplitter(challenge_map)

print(f"Challenge result: {beam_splitter_challenge.analyse_entire_map()}")
