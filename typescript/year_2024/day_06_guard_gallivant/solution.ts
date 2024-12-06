import path from 'path';
import { Direction, Grid, rotate90Degrees } from '../../utils/grid';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

export const partOne = async (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((row) => row.split('')));
  const visited = new Set<string>();

  let [x, y] = grid.find('^')[0];
  grid.array[x][y] = '.';

  let direction = Direction.North;

  visited.add(`${x},${y}`);

  let escaped = false;

  while (!escaped) {
    let nextPos: [number, number] | undefined;
    let nextVal: string | undefined;
    let foundValidMove = false;

    for (let i = 0; i < 4; i++) {
      try {
        ({ value: nextVal, position: nextPos } = grid.getAdjacent(x, y, direction));

        if (nextVal === '.') {
          foundValidMove = true;
          break;
        }

        direction = rotate90Degrees(direction);
      } catch {
        escaped = true;
        break;
      }
    }

    if (escaped) break;

    if (foundValidMove && nextPos) {
      [x, y] = nextPos;
      visited.add(`${x},${y}`);
    }
  }

  return visited.size.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  let loops = 0;

  for (let i = 0; i < puzzleInput.length; i++) {
    for (let j = 0; j < puzzleInput[i].length; j++) {
      const grid = new Grid(puzzleInput.map((row) => row.split('')));

      const visited = new Set<string>();

      let [x, y] = grid.find('^')[0];
      let direction = Direction.North;

      grid.array[x][y] = '.';
      grid.array[i][j] = '#';

      visited.add(`${x},${y},${direction}`);

      let escaped = false;

      while (!escaped) {
        let nextPos: [number, number] | undefined;
        let nextVal: string | undefined;
        let foundValidMove = false;

        for (let i = 0; i < 4; i++) {
          try {
            ({ value: nextVal, position: nextPos } = grid.getAdjacent(x, y, direction));

            if (nextVal === '.') {
              foundValidMove = true;
              break;
            }

            direction = rotate90Degrees(direction);
          } catch {
            escaped = true;
            break;
          }
        }

        if (escaped) break;

        if (foundValidMove && nextPos) {
          [x, y] = nextPos;
          if (visited.has(`${x},${y},${direction}`)) {
            loops++;
            break;
          }
          visited.add(`${x},${y},${direction}`);
        }
      }
    }
  }
  return loops.toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('06', 'guard_gallivant', partOne, partTwo, puzzle_input);
}
