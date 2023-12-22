from helpers.aoc_utils import input_data, time_function, Direction

REFLECT_DIRS = {("|", Direction.EAST): [Direction.NORTH, Direction.SOUTH],
                ("|", Direction.WEST): [Direction.NORTH, Direction.SOUTH],

                ("-", Direction.NORTH): [Direction.EAST, Direction.WEST],
                ("-", Direction.SOUTH): [Direction.EAST, Direction.WEST],

                ("/", Direction.NORTH): Direction.EAST,
                ("/", Direction.EAST): Direction.NORTH,
                ("/", Direction.SOUTH): Direction.WEST,
                ("/", Direction.WEST): Direction.SOUTH,

                ("\\", Direction.NORTH): Direction.WEST,
                ("\\", Direction.EAST): Direction.SOUTH,
                ("\\", Direction.SOUTH): Direction.EAST,
                ("\\", Direction.WEST): Direction.NORTH,
                }


class Beam():
    def __init__(self, direction, pos):
        self.dir = direction
        self.pos = pos

    def __repr__(self) -> str:
        return f"Beam({self.dir}, {self.pos})"

    def next_pos(self):
        row, col = self.pos
        dr, dc = self.dir.value
        return (row + dr, col + dc)

    def __hash__(self):
        return hash((self.dir, self.pos))

    def __eq__(self, other):
        return (self.dir, self.pos) == (other.dir, other.pos)


def simulate_beam(puzzle_input, initial_dir, initial_pos):
    beams = [Beam(initial_dir, initial_pos)]
    processed_beams = set()
    visited_tiles = set()

    while len(beams) > 0:
        new_beams = []
        for beam in beams:
            r, c = beam.next_pos()

            if beam not in processed_beams:
                if 0 <= r < len(puzzle_input) and 0 <= c < len(puzzle_input[0]):

                    visited_tiles.add((r, c))
                    current_symbol = puzzle_input[r][c]
                    key = (current_symbol, beam.dir)

                    if key in REFLECT_DIRS.keys():

                        next_dirs = REFLECT_DIRS[(current_symbol, beam.dir)]
                        if type(next_dirs) == list:
                            for direction in next_dirs:
                                new_beams.append(Beam(direction, (r, c)))

                        else:
                            new_beams.append(Beam(next_dirs, (r, c)))

                    else:
                        new_beams.append(Beam(beam.dir, (r, c)))

        processed_beams.update(beams)
        beams = new_beams

    return len(visited_tiles)


def part_one(puzzle_input):
    return simulate_beam(puzzle_input, Direction.EAST, (0, -1))


def part_two(puzzle_input):
    coords = {Direction.NORTH: lambda i: (len(puzzle_input[0]) + 1, i),
              Direction.SOUTH: lambda i: (-1, i),
              Direction.EAST: lambda i: (i, -1),
              Direction.WEST: lambda i: (i, len(puzzle_input) + 1)}

    return max(simulate_beam(puzzle_input, d, pos(i)) for d, pos in coords.items() for i in range(len(puzzle_input)))


def main():
    puzzle_input = input_data(
        "year_2023/day_16_the_floor_will_be_lava/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 16: the_floor_will_be_lava")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()


# Print that can be added to the loop for a little animation!
# os.system('cls' if os.name == 'nt' else 'clear')
# for i in range(len(puzzle_input)):
#     print("".join(
#         [x if (i, j) not in visited_tiles else "#" for j, x in enumerate(puzzle_input[i])]))
# time.sleep(0.1)
