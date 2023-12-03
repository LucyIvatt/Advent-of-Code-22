def input_data(filename):
    """Returns the data imported from file - 
    """
    with open(filename, "r") as file:
        puzzle_input = [line.strip() for line in file.readlines()]
        return puzzle_input

def get_adjacent_coords(coords, x_limit, y_limit, diagonal=False):
    '''Returns all of the adjacent coordinates, including diagonals) for a list of coordinates. Removes any duplicates and any coordinates
    that were present in the original input.'''
    if diagonal:
        directions = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)]
    else:
        directions = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0) and (dx == 0 or dy == 0)]

    adjecent_coords = []

    for coord in coords:
        x, y = coord
        adjecent_coords += [
        (x + dx, y + dy) for dx, dy in directions
        if 0 <= x + dx < x_limit and 0 <= y + dy < y_limit
    ]
    
    
    return set([coord for coord in adjecent_coords if coord not in coords])



    
