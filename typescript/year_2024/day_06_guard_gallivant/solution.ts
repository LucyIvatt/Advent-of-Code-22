import path from 'path';
import { Coord, Direction, Grid, rotate } from '../../utils/grid';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const traverseGrid = (grid: Grid<string>, startX: number, startY: number, startDir: Direction) => {
  const visited = new Set<string>();
  let [x, y, direction] = [startX, startY, startDir];
  let escaped = false;

  visited.add(`${x},${y},${direction}`);

  while (!escaped) {
    while (true) {
      try {
        const { value, position } = grid.getAdjacent(x, y, direction);

        if (value !== '#') {
          [x, y] = position;
          const stateKey = `${x},${y},${direction}`;

          if (visited.has(stateKey)) return { visited, loops: true };
          visited.add(stateKey);
          break;
        }

        direction = rotate(direction, 90);
      } catch {
        escaped = true;
        break;
      }
    }
  }

  return { visited, loops: false };
};

const getUniquePositions = (visited: Set<string>): Coord[] =>
  [...new Set([...visited].map((state) => state.split(',').slice(0, 2).join(',')))].map(
    (pos) => pos.split(',').map(Number) as Coord
  );

export const partOne = async (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((row) => row.split('')));
  const [startX, startY] = grid.find('^')[0];
  grid.array[startX][startY] = '.';

  const { visited } = traverseGrid(grid, startX, startY, Direction.North);

  return getUniquePositions(visited).length.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const originalGrid = new Grid(puzzleInput.map((row) => row.split('')));
  const [startX, startY] = originalGrid.find('^')[0];

  const { visited } = traverseGrid(originalGrid, startX, startY, Direction.North);

  let loops = 0;
  for (const [i, j] of getUniquePositions(visited)) {
    if (i === startX && j === startY) continue;

    const grid = new Grid(puzzleInput.map((row) => row.split('')));
    grid.array[startX][startY] = '.';
    grid.array[i][j] = '#';

    if (traverseGrid(grid, startX, startY, Direction.North).loops) loops++;
  }

  return loops.toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('06', 'guard_gallivant', partOne, partTwo, puzzleInput);
}
