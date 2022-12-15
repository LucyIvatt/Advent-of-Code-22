def importList(filename):
    formation = []
    with open(filename, "r") as file:
        for line in file:
            formation.append([int(char) for char in line.strip()])
    return formation


def simulate_step(formation):
    flashed = [[False for j in range(len(formation[i]))]
               for i in range(len(formation))]

    # Increases energy of each octopus by 1
    formation = [[octopus + 1 for octopus in row] for row in formation]

    # Energy level greater than 9 flashes
    finished_flashing = False
    while not finished_flashing:
        for i in range(len(formation)):
            for j in range(len(formation[i])):
                if formation[i][j] > 9 and flashed[i][j] == False:
                    flashed[i][j] = True
                    for k, l in get_neighbors_coords(formation, i, j):
                        formation[k][l] += 1

        # Checks if all values > 9 have already flashed
        finished_flashing = True
        for i in range(len(formation)):
            for j in range(len(formation[i])):
                if formation[i][j] > 9 and flashed[i][j] == False:
                    finished_flashing = False
            if not finished_flashing:
                break

    # Calculates number of flashes
    flash_count = sum(row.count(True) for row in flashed)

    # Sets flashed octopuses to
    formation = [[octopus if octopus <= 9 else 0 for octopus in row]
                 for row in formation]

    return(formation, flash_count)


def get_neighbors_coords(formation, x, y):
    neighbors_coords = []
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        new_x, new_y = x + dx, y + dy
        if new_x >= 0 and new_x < len(formation):
            if new_y >= 0 and new_y < len(formation[new_x]):
                neighbors_coords.append((new_x, new_y))
    return neighbors_coords


def part_one():
    formation = importList("Day 11 Dumbo Octopus\input.txt")
    total_flashes = 0
    for i in range(100):
        formation, flashes = simulate_step(formation)
        total_flashes += flashes
    return total_flashes


def part_two():
    formation = importList("Day 11 Dumbo Octopus\input.txt")
    synchronized_flash = False
    step = 0
    while not synchronized_flash:
        step += 1
        formation, flashes = simulate_step(formation)
        if(flashes == len(formation) * len(formation[0])):
            synchronized_flash = True
            return step


print("--------------------------------------")
print("DAY 11: DUMBO OCTOPUS")
print("Part One Answer: " + str(part_one()))
print("Part Two Answer: " + str(part_two()))
print("--------------------------------------")
