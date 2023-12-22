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

    def next_position(self):
        row, col = self.pos
        dr, dc = self.dir.value
        return (row + dr, col + dc)

    def __hash__(self):
        return hash((self.dir, self.pos))

    def __eq__(self, other):
        return (self.dir, self.pos) == (other.dir, other.pos)


def simulate_beam(puzzle_input, initial_dir, initial_pos):
    beams = {Beam(initial_dir, initial_pos)}
    processed_beams, visited_tiles = set(), set()

    while beams:
        next_beams = set()
        for beam in beams:
            row, col = beam.next_position()

            if beam not in processed_beams and all(0 <= x < len(puzzle_input) for x in (row, col)):
                visited_tiles.add((row, col))
                key = (puzzle_input[row][col], beam.dir)

                if key in REFLECT_DIRS.keys():
                    next_dirs = REFLECT_DIRS[key]

                    if isinstance(next_dirs, list):
                        next_beams.update(Beam(direction, (row, col))
                                          for direction in next_dirs)
                    else:
                        next_beams.add(Beam(next_dirs, (row, col)))

                else:
                    next_beams.add(Beam(beam.dir, (row, col)))

        processed_beams.update(beams)
        beams = next_beams

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
