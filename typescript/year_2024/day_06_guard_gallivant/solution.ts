import path from 'path';
import { Direction, Grid, rotate90Degrees } from '../../utils/grid';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const navigateGrid = (
  grid: Grid<string>,
  start: [number, number],
  direction: Direction,
  onVisit: (x: number, y: number, direction: Direction) => boolean
): boolean => {
  let [x, y] = start;
  let currentDirection = direction;

  while (true) {
    let nextPos: [number, number] | undefined;
    let nextVal: string | undefined;
    let foundValidMove = false;

    for (let i = 0; i < 4; i++) {
      try {
        ({ value: nextVal, position: nextPos } = grid.getAdjacent(x, y, currentDirection));

        if (nextVal === '.') {
          foundValidMove = true;
          break;
        }
        currentDirection = rotate90Degrees(currentDirection);
      } catch {
        return false;
      }
    }

    if (!foundValidMove || !nextPos) return false;

    [x, y] = nextPos;

    if (onVisit(x, y, currentDirection)) return true; // Custom condition met (e.g., loop detected)
  }
};

export const partOne = async (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((row) => row.split('')));
  const visited = new Set<string>();

  const [x, y] = grid.find('^')[0];
  grid.array[x][y] = '.';
  visited.add(`${x},${y}`);

  navigateGrid(grid, [x, y], Direction.North, (x, y) => {
    visited.add(`${x},${y}`);
    return false;
  });

  return visited.size.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  let loops = 0;

  for (let i = 0; i < puzzleInput.length; i++) {
    for (let j = 0; j < puzzleInput[i].length; j++) {
      if (puzzleInput[i][j] === '^' || puzzleInput[i][j] === '#') continue; // skip start location & current obstacles

      const grid = new Grid(puzzleInput.map((row) => row.split('')));
      const visited = new Set<string>();

      const [x, y] = grid.find('^')[0];
      grid.array[x][y] = '.';
      visited.add(`${x},${y},${Direction.North}`);

      grid.array[i][j] = '#'; // Set new obstacle

      const foundLoop = navigateGrid(grid, [x, y], Direction.North, (x, y, direction) => {
        const state = `${x},${y},${direction}`;
        if (visited.has(state)) {
          return true;
        }
        visited.add(state);
        return false;
      });

      if (foundLoop) loops++;
    }
  }

  return loops.toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('06', 'guard_gallivant', partOne, partTwo, puzzle_input);
}
