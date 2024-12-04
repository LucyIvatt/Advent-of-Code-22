import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Direction, Grid } from '../../utils/grids';

const countXmas = (i: number, j: number, grid: Grid<string>): number =>
  Object.values(Direction).filter((direction) => {
    const { values } = grid.walk(i, j, direction, 4);
    return values.join('') === 'XMAS';
  }).length;

const isMasOrSam = (values: string[]): boolean => ['MAS', 'SAM'].includes(values.join(''));

export const partOne = (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((line) => line.split('')));

  return grid.array
    .flatMap((row, i) => row.map((cell, j) => (cell === 'X' ? countXmas(i, j, grid) : 0)))
    .reduce((sum, count) => sum + count, 0)
    .toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((line) => line.split('')));

  return grid.array
    .flatMap((row, i) =>
      row.map((cell, j) => {
        if (cell === 'A' && i > 0 && i < grid.array.length - 1 && j > 0 && j < grid.array[0].length - 1) {
          const { values: se_sequence } = grid.walk(i - 1, j - 1, Direction.SouthEast, 3);
          const { values: sw_sequence } = grid.walk(i - 1, j + 1, Direction.SouthWest, 3);
          return isMasOrSam(se_sequence) && isMasOrSam(sw_sequence) ? 1 : (0 as number);
        }
        return 0;
      })
    )
    .reduce((sum, count) => sum + count, 0)
    .toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('04', 'ceres_search', partOne, partTwo, puzzle_input);
}
