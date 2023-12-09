from helpers.aoc_utils import input_data, time_function


def solution(puzzle_input, backwards=False):
    extr_sum = 0
    for history in puzzle_input:
        values = [int(num) for num in history.split()]
        rows = [values]

        curr_row = values

        while not all(val == 0 for val in curr_row):
            differences = [curr_row[i+1]-curr_row[i]
                           for i in range(len(curr_row)-1)]
            rows.append(differences)
            curr_row = differences

        for i in range(len(rows)-1, -1, -1):
            if i == len(rows)-1:
                rows[i].append(0)

            elif not backwards:
                rows[i].append(rows[i][-1] + rows[i+1][-1])
            else:
                rows[i].insert(0, rows[i][0] - rows[i+1][0])

        extr_sum += rows[0][-1] if not backwards else rows[0][0]

    return extr_sum


puzzle_input = input_data("year_2023/day_09_mirage_maintenance/input.txt")

p1, p1_time = time_function(solution, puzzle_input)
p2, p2_time = time_function(solution, puzzle_input, True)

print("--------------------------------------")
print("Day 09: mirage_maintenance")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
