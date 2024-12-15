import path from 'path';
import { InputFile, readPuzzleInput, split2DArray } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Direction, Grid } from '../../utils/grid';

const DIRECTION_MAP = new Map<string, Direction>([
  ['^', Direction.North],
  ['>', Direction.East],
  ['v', Direction.South],
  ['<', Direction.West]
]);

export const partOne = (puzzleInput: string[]) => {
  const formattedInput = split2DArray(puzzleInput, '');

  const grid = new Grid(formattedInput[0].map((row) => row.split('')));
  const directions = formattedInput[1].flatMap((line) => line.split('').map((char) => DIRECTION_MAP.get(char)!));

  let robotPosition = grid.find('@')[0];

  for (const direction of directions) {
    const nextCell = grid.getAdjacent(robotPosition[0], robotPosition[1], direction);

    if (nextCell?.value == '.') {
      grid.array[robotPosition[0]][robotPosition[1]] = '.';
      robotPosition = nextCell.position;
      grid.array[robotPosition[0]][robotPosition[1]] = '@';
    } else if (nextCell?.value === 'O') {
      const adjBoxCells = [nextCell.position];

      let currentBoxPosition = nextCell.position;
      while (true) {
        const nextBoxPosition = grid.getAdjacent(currentBoxPosition[0], currentBoxPosition[1], direction);
        if (nextBoxPosition?.value !== 'O') break;
        currentBoxPosition = nextBoxPosition.position;
        adjBoxCells.push(currentBoxPosition);
      }

      const [i, j] = adjBoxCells.at(-1)!;
      const nextNonBoxCell = grid.getAdjacent(i, j, direction);

      if (nextNonBoxCell?.value === '.') {
        grid.array[robotPosition[0]][robotPosition[1]] = '.';
        robotPosition = nextCell.position;
        grid.array[robotPosition[0]][robotPosition[1]] = '@';

        adjBoxCells.shift();

        for (const position of [...adjBoxCells, nextNonBoxCell.position]) {
          grid.array[position[0]][position[1]] = 'O';
        }

        grid.array[nextNonBoxCell.position[0]][nextNonBoxCell.position[1]] = 'O';
      }
    }
  }
  console.log(grid.toString(false));
  const boxes = grid.find('O');

  return boxes.reduce((acc, box) => (acc += 100 * box[0] + box[1]), 0).toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return 'Part 2 Answer';
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('15', 'warehouse_woes', partOne, partTwo, puzzleInput);
}
