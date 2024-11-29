from python.helpers.aoc_utils import input_data, time_function


def solution(puzzle_input, backwards=False):
    extr_sum = 0

    for history in puzzle_input:
        rows = [[int(num) for num in history.split()]]

        while any(value != 0 for value in rows[-1]):
            rows.append([rows[-1][i+1]-rows[-1][i]
                        for i in range(len(rows[-1])-1)])

        for i in range(len(rows) - 1, -1, -1):
            if i == len(rows) - 1:
                rows[i].append(0)
            else:
                val = rows[i][0] - rows[i +
                                        1][0] if backwards else rows[i][-1] + rows[i + 1][-1]
                rows[i] = [val] + rows[i] if backwards else rows[i]+[val]

        extr_sum += rows[0][0] if backwards else rows[0][-1]

    return extr_sum


def main():
    puzzle_input = input_data("python/year_2023/day_09_mirage_maintenance/input.txt")

    p1, p1_time = time_function(solution, puzzle_input)
    p2, p2_time = time_function(solution, puzzle_input, True)

    print("--------------------------------------")
    print("Day 09: mirage_maintenance")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
