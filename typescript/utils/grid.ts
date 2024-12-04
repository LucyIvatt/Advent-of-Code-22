import chalk from 'chalk';

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

export class Grid<Type> {
  array: Type[][];

  constructor(grid: Type[][]) {
    this.array = grid;
  }

  getAdjacent(i: number, j: number, direction: Direction): { value: Type; position: [number, number] } {
    const offset = directionOffsets.get(direction);

    if (!offset) {
      throw new Error(`Invalid direction: ${direction}`);
    }

    const position = [i + offset.dy, j + offset.dx] as [number, number];

    if (position[0] < 0 || position[0] >= this.array.length || position[1] < 0 || position[1] >= this.array[0].length) {
      throw new Error(`Position out of bounds at [${i}, ${j}] moving ${direction} to [${position[0]}, ${position[1]}]`);
    }
    return { value: this.array[position[0]][position[1]], position };
  }

  walk(i: number, j: number, direction: Direction, length: number): { values: Type[]; positions: number[][] } {
    if (length < 1) throw Error('Length must be > 0');

    const values = [this.array[i][j]];
    const positions = [[i, j]];

    while (values.length < length) {
      try {
        const adjacent = this.getAdjacent(i, j, direction);
        values.push(adjacent.value);
        positions.push(adjacent.position);
        i = adjacent.position[0];
        j = adjacent.position[1];
      } catch {
        break;
      }
    }

    return { values, positions };
  }

  toString(): string {
    const cols = this.array[0]?.length || 0;
    const cellWidth = this.getMaxCellWidth();

    const columnHeaders = this.createColumnHeaders(cols, cellWidth);
    const gridRows = this.createGridRows(cellWidth);

    return `${columnHeaders}\n${gridRows}`;
  }

  private getMaxCellWidth(): number {
    return Math.max(
      ...this.array.flat().map((cell) => (cell === null || cell === undefined ? 1 : cell.toString().length)),
      1
    );
  }

  private createColumnHeaders(cols: number, cellWidth: number): string {
    return [
      ' '.repeat(cellWidth),
      ...Array.from({ length: cols }, (_, i) => chalk.blue(i.toString().padStart(cellWidth)))
    ].join(' ');
  }

  private createGridRows(cellWidth: number): string {
    return this.array
      .map(
        (row, rowIndex) =>
          `${chalk.blue(rowIndex.toString().padStart(cellWidth))} ${row
            .map((cell) => (cell ?? ' ').toString().padStart(cellWidth))
            .join(' ')}`
      )
      .join('\n');
  }
}
