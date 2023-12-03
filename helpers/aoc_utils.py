def input_data(filename):
    """Returns the data imported from file - 
    """
    file = open(filename, "r")
    puzzle_input = file.readlines()
    file.close()
    return puzzle_input

def get_adjacent_and_diagonal_coords(coords, x_limit, y_limit):
    directions = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)]

    adjecent_coords = []

    for coord in coords:
        x, y = coord
        adjecent_coords += [
        (x + dx, y + dy) for dx, dy in directions
        if 0 <= x + dx < x_limit and 0 <= y + dy < y_limit
    ]
    
    
    return set([coord for coord in adjecent_coords if coord not in coords])



    
