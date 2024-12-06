import path from 'path';
import { Direction, Grid, rotate90Degrees } from '../../utils/grid';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { delay } from '../../utils/time';

export const partOne = async (puzzle_input: string[]) => {
  const grid = new Grid(puzzle_input.map((a) => a.split('')));
  const visited = new Set();

  let loc: [number, number] = grid.find('^')[0];
  let dir = Direction.North;
  let escaped = false;

  visited.add(`${loc[0]},${loc[1]}`);

  while (!escaped) {
    let nextVal, nextPos;

    while (!nextVal || !nextPos || (nextVal !== '.' && nextVal !== 'X')) {
      if (nextVal && nextPos && nextVal !== '.' && nextVal !== 'X') dir = rotate90Degrees(dir);
      try {
        ({ value: nextVal, position: nextPos } = grid.getAdjacent(loc[0], loc[1], dir));
      } catch {
        escaped = true;
        break;
      }
    }

    grid.array[loc[0]][loc[1]] = 'X';
    // console.clear();
    // console.log(grid.toString(false));
    // await delay(75);

    if (escaped) break;

    if (nextPos) {
      loc = nextPos;
      visited.add(`${loc[0]},${loc[1]}`);
    }
  }

  return visited.size.toString();
};

export const partTwo = (puzzle_input: string[]) => {
  let loops = 0;

  for (let i = 0; i < puzzle_input.length; i++) {
    for (let j = 0; j < puzzle_input[i].length; j++) {
      const grid = new Grid(puzzle_input.map((a) => [...a.split('')]));
      let loc: [number, number] = grid.find('^')[0];
      let dir = Direction.North;
      let escaped = false;
      const visited = new Set();

      visited.add(`${loc[0]},${loc[1]},${dir}`);

      if (i === loc[0] && j === loc[1]) break;

      grid.array[i][j] = '#';

      while (!escaped) {
        let nextVal, nextPos;

        while (!nextVal || !nextPos || (nextVal !== '.' && nextVal !== 'X')) {
          if (nextVal && nextPos && nextVal !== '.' && nextVal !== 'X') dir = rotate90Degrees(dir);
          try {
            ({ value: nextVal, position: nextPos } = grid.getAdjacent(loc[0], loc[1], dir));
          } catch {
            escaped = true;
            break;
          }
        }

        grid.array[loc[0]][loc[1]] = 'X';

        if (escaped) {
          break;
        }

        if (nextPos) {
          loc = nextPos;
          if (visited.has(`${loc[0]},${loc[1]},${dir}`)) {
            loops++;
            break;
          }
          visited.add(`${loc[0]},${loc[1]},${dir}`);
        }
      }
    }
  }
  return loops.toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('06', 'guard_gallivant', partOne, partTwo, puzzle_input);
}
