import chalk from 'chalk';

export type Coord = [number, number];
export type Cell = { value: string | number; position: Coord };

export enum Direction {
  North = 'North',
  NorthEast = 'NorthEast',
  East = 'East',
  SouthEast = 'SouthEast',
  South = 'South',
  SouthWest = 'SouthWest',
  West = 'West',
  NorthWest = 'NorthWest'
}

export const STRAIGHT_DIRECTIONS = [Direction.North, Direction.East, Direction.South, Direction.West];
export const DIAGONAL_DIRECTIONS = [Direction.NorthEast, Direction.SouthEast, Direction.SouthWest, Direction.NorthWest];

/**
 * A map that associates each direction with its corresponding offset in the grid,
 * representing the change in the x and y coordinates when moving a single cell in that direction.
 */
export const directionOffsets = new Map<Direction, { dx: number; dy: number }>([
  [Direction.North, { dx: 0, dy: -1 }],
  [Direction.NorthEast, { dx: +1, dy: -1 }],
  [Direction.East, { dx: +1, dy: 0 }],
  [Direction.SouthEast, { dx: +1, dy: +1 }],
  [Direction.South, { dx: 0, dy: +1 }],
  [Direction.SouthWest, { dx: -1, dy: +1 }],
  [Direction.West, { dx: -1, dy: 0 }],
  [Direction.NorthWest, { dx: -1, dy: -1 }]
]);

/**
 * Rotates a given direction by a specified number of degrees.
 *
 * @param direction - The initial direction to rotate from, represented as a value from the Direction enum.
 * @param degrees - The number of degrees to rotate, which must be a multiple of 45.
 * @returns The new direction after rotation.
 * @throws Will throw an error if the degrees are not in 45-degree increments.
 */
export const rotate = (direction: Direction, degrees: number): Direction => {
  if (degrees % 45 !== 0) throw new Error('Degrees must be in 45 degree increments');

  const directions = Object.values(Direction);
  const currentIndex = directions.indexOf(direction);
  const newIndex = (currentIndex + degrees / 45 + directions.length) % directions.length;

  return directions[newIndex];
};

export const manhattanDistance = (pos1: Coord, pos2: Coord) => {
  return Math.abs(pos1[0] - pos2[0]) + Math.abs(pos1[1] - pos2[1]);
};
export class Grid<Type> {
  array: Type[][];

  /**
   * Creates an instance of the grid.
   *
   * @param grid - A two-dimensional array representing the grid.
   */
  constructor(grid: Type[][]) {
    if (grid.length === 0 || grid[0].length === 0) {
      throw new Error('Grid must have at least one element.');
    }
    this.array = grid;
  }

  find(value: Type) {
    const locations = [] as Coord[];

    for (let i = 0; i < this.array.length; i++) {
      for (let j = 0; j < this.array[i].length; j++) {
        if (this.array[i][j] === value) locations.push([i, j]);
      }
    }
    return locations;
  }

  isValidLocation([i, j]: Coord) {
    return i >= 0 && i < this.array.length && j >= 0 && j < this.array[i].length;
  }

  /**
   * Retrieves the adjacent cell value and its position based on the given direction.
   *
   * @param i - The row index of the current cell.
   * @param j - The column index of the current cell.
   * @param direction - The direction to move from the current cell.
   * @returns An object containing the value of the adjacent cell and its position as a tuple [row, column].
   * @throws Will throw an error if the direction is invalid or if the resulting position is out of bounds.
   */
  getAdjacent(i: number, j: number, direction: Direction): { value: Type; position: Coord } | undefined {
    const offset = directionOffsets.get(direction);

    if (!offset) {
      throw new Error(`Invalid direction: ${direction}`);
    }

    const position = [i + offset.dy, j + offset.dx] as Coord;

    if (position[0] < 0 || position[0] >= this.array.length || position[1] < 0 || position[1] >= this.array[0].length) {
      return undefined;
    }
    return { value: this.array[position[0]][position[1]], position };
  }

  getAdjacents(i: number, j: number, diagonal = false): { value: Type; position: Coord }[] {
    const directions = diagonal ? STRAIGHT_DIRECTIONS.concat(DIAGONAL_DIRECTIONS) : STRAIGHT_DIRECTIONS;
    const adjacents: { value: Type; position: Coord }[] = [];

    for (const direction of directions) {
      const adjacent = this.getAdjacent(i, j, direction);
      if (adjacent) adjacents.push(adjacent);
    }

    return adjacents;
  }

  /**
   * Walks through the grid starting from the given coordinates (i, j) in the specified direction
   * for a certain length and collects the values and positions encountered.
   *
   * @param i - The starting row index.
   * @param j - The starting column index.
   * @param direction - The direction to walk in.
   * @param length - The number of steps to walk. Must be greater than 0.
   * @returns An object containing the values and positions encountered during the walk.
   */
  walk(i: number, j: number, direction: Direction, length: number): { values: Type[]; positions: number[][] } {
    if (length < 1) throw Error('Length must be > 0');

    const values = [this.array[i][j]];
    const positions = [[i, j]];

    while (values.length < length) {
      const adjacent = this.getAdjacent(i, j, direction);
      if (!adjacent) break;

      values.push(adjacent.value);
      positions.push(adjacent.position);
      i = adjacent.position[0];
      j = adjacent.position[1];
    }

    return { values, positions };
  }

  /**
   * Converts the grid to a string representation.
   *
   * The string representation includes column headers and grid rows.
   * Each cell is formatted to have a consistent width based on the
   * maximum cell width in the grid.
   *
   * @returns {string} The string representation of the grid.
   */
  toString(showHeaders = true): string {
    const cols = this.array[0].length;
    const cellWidth = this.getMaxCellWidth();

    const columnHeaders = showHeaders ? this.createColumnHeaders(cols, cellWidth) : '';
    const gridRows = this.createGridRows(cellWidth, showHeaders);

    return showHeaders ? `${columnHeaders}\n${gridRows}` : gridRows;
  }

  /**
   * Calculates the maximum width of the cells in the grid.
   *
   * This method flattens the 2D array of cells into a single array,
   * then maps each cell to its string length (or 1 if the cell is null or undefined).
   * Finally, it returns the maximum value found in the mapped array.
   *
   * @returns {number} The maximum width of the cells in the grid.
   */
  private getMaxCellWidth(): number {
    return Math.max(
      ...this.array.flat().map((cell) => (cell === null || cell === undefined ? 1 : cell.toString().length)),
      1
    );
  }

  /**
   * Creates a string representing the column headers for a grid.
   *
   * @param cols - The number of columns in the grid.
   * @param cellWidth - The width of each cell in characters.
   * @returns A string with the column headers, where each header is padded to the specified cell width and colored blue.
   */
  private createColumnHeaders(cols: number, cellWidth: number): string {
    return [
      ' '.repeat(cellWidth),
      ...Array.from({ length: cols }, (_, i) => chalk.blue(i.toString().padStart(cellWidth)))
    ].join(' ');
  }

  /**
   * Creates a string representation of the grid with rows formatted to a specified cell width.
   * Each row is prefixed with its index, and cells are padded to align properly.
   *
   * @param cellWidth - The width to pad each cell to.
   * @returns A string representation of the grid with formatted rows.
   */
  private createGridRows(cellWidth: number, showHeaders: boolean): string {
    return this.array
      .map(
        (row, rowIndex) =>
          `${showHeaders ? chalk.blue(rowIndex.toString().padStart(cellWidth)) + ' ' : ''}${row
            .map((cell) => (cell ?? ' ').toString().padStart(cellWidth))
            .join(' ')}`
      )
      .join('\n');
  }
}
