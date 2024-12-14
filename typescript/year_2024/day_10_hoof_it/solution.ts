import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Coord, Direction, Grid } from '../../utils/grid';

const VALID_DIRECTIONS = [Direction.North, Direction.East, Direction.South, Direction.West];
const SUMMIT_HEIGHT = 9;
const TRAILHEAD_HEIGHT = 0;

const findTrailheads = (grid: Grid<number>) =>
  grid.array.flatMap(
    (row, x) => row.map((height, y) => (height === TRAILHEAD_HEIGHT ? [x, y] : null)).filter(Boolean) as Coord[]
  );

const isValidLocation = (grid: Grid<number>, i: number, j: number, direction: Direction) => {
  const adjacent = grid.getAdjacent(i, j, direction);
  if (!adjacent) return { isReachable: false };

  return { isReachable: adjacent.value === grid.array[i][j] + 1, position: adjacent.position };
};

const findReachableSummits = (grid: Grid<number>, trailhead: Coord) => {
  const reachableSummits = new Set<string>();
  let rating = 0;
  let currentPaths = [[trailhead]];

  while (currentPaths.length) {
    const newPaths = [];

    for (const path of currentPaths) {
      const [i, j] = path.at(-1)!;

      for (const direction of VALID_DIRECTIONS) {
        const { isReachable, position } = isValidLocation(grid, i, j, direction);

        if (isReachable && position) {
          if (grid.array[position[0]][position[1]] === SUMMIT_HEIGHT) {
            reachableSummits.add(position.toString());
            rating++;
          } else {
            newPaths.push([...path, position]);
          }
        }
      }
    }
    currentPaths = newPaths;
  }
  return { reachableSummits, rating };
};

const analyseMap = (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((row) => row.split('').map(Number)));

  return findTrailheads(grid).reduce(
    (acc, trailhead) => {
      const { reachableSummits, rating } = findReachableSummits(grid, trailhead);
      acc.scores += reachableSummits.size;
      acc.ratings += rating;
      return acc;
    },
    { scores: 0, ratings: 0 }
  );
};

export const partOne = (puzzleInput: string[]) => analyseMap(puzzleInput).scores.toString();
export const partTwo = (puzzleInput: string[]) => analyseMap(puzzleInput).ratings.toString();

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('10', 'hoof_it', partOne, partTwo, puzzleInput);
}
