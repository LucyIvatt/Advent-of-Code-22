import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Direction, Grid } from '../../utils/grids';

export const partOne = (puzzle_input: string[]) => {
  const grid = new Grid(puzzle_input.map((line) => line.split('')));
  let xmasCount = 0;

  for (let i = 0; i < grid.array.length; i++) {
    for (let j = 0; j < grid.array[i].length; j++) {
      const char = grid.array[i][j];
      if (char === 'X') {
        for (const direction of Object.values(Direction)) {
          const { values } = grid.walk(i, j, direction, 4);
          if (values.join('') === 'XMAS') xmasCount++;
        }
      }
    }
  }
  return xmasCount.toString();
};

export const partTwo = (puzzle_input: string[]) => {
  const grid = new Grid(puzzle_input.map((line) => line.split('')));
  let x_masCount = 0;

  for (let i = 0; i < grid.array.length; i++) {
    for (let j = 0; j < grid.array[i].length; j++) {
      const { values: se_search } = grid.walk(i, j, Direction.SouthEast, 3);
      const { values: sw_search } = grid.walk(i, j + 2, Direction.SouthWest, 3);

      if (
        (se_search.join('') === 'MAS' || se_search.join('') === 'SAM') &&
        (sw_search.join('') === 'MAS' || sw_search.join('') === 'SAM')
      ) {
        x_masCount++;
      }
    }
  }

  return x_masCount.toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('04', 'ceres_search', partOne, partTwo, puzzle_input);
}
