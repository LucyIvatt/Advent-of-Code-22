import { ColourCode } from './colours';

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

export const DirectionMap = new Map<Direction, { dx: number; dy: number }>([
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

  getAdacent(i: number, j: number, direction: Direction): { val: Type; newPos: [number, number] } {
    const offset = DirectionMap.get(direction);

    if (!offset) {
      throw new Error(`Invalid direction: ${direction}`);
    }

    const newPos = [i + offset.dy, j + offset.dx] as [number, number];

    if (newPos[0] < 0 || newPos[0] >= this.array.length || newPos[1] < 0 || newPos[1] >= this.array[0].length) {
      throw new Error(`Position out of bounds: ${newPos}`);
    }
    return { val: this.array[newPos[0]][newPos[1]], newPos };
  }

  walk(i: number, j: number, direction: Direction, length: number): { val: Type; pos: [number, number] }[] {
    const elements = [{ val: this.array[i][j], pos: [i, j] as [number, number] }];

    while (elements.length < length) {
      try {
        const adjacent = this.getAdacent(i, j, direction);
        elements.push({ val: adjacent.val, pos: adjacent.newPos });
        i = adjacent.newPos[0];
        j = adjacent.newPos[1];
      } catch {
        break;
      }
    }

    return elements;
  }

  toString(): string {
    const cols = this.array[0]?.length || 0;

    const cellWidth = Math.max(
      ...this.array.flat().map((cell) => (cell === null || cell === undefined ? 1 : cell.toString().length)),
      1
    );

    const columnHeaders = [
      ' '.repeat(cellWidth),
      ...Array.from(
        { length: cols },
        (_, i) => `${ColourCode.Blue}${i.toString().padStart(cellWidth)}${ColourCode.Reset}`
      )
    ].join(' ');

    const gridRows = this.array
      .map(
        (row, rowIndex) =>
          `${ColourCode.Blue}${rowIndex.toString().padStart(cellWidth)}${ColourCode.Reset} ${row
            .map((cell) => (cell ?? ' ').toString().padStart(cellWidth))
            .join(' ')}`
      )
      .join('\n');

    return `${columnHeaders}\n${gridRows}`;
  }
}

// const newGrid = new Grid([
//   [1, 2, 3],
//   [4, 5, 6],
//   [7, 8, 9]
// ]);

// console.log(newGrid.toString());
// console.log(newGrid.walk(2, 2, Direction.NorthWest, 4));
