import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Coord, Direction, Grid } from '../../utils/grid';

const validDirections = [Direction.North, Direction.East, Direction.South, Direction.West];

const findTrailheads = (grid: Grid<number>) =>
  grid.array.flatMap((row, x) => row.map((height, y) => (height === 0 ? [x, y] : null)).filter(Boolean) as Coord[]);

const isValidLocation = (grid: Grid<number>, i: number, j: number, direction: Direction) => {
  try {
    const { value: height, position } = grid.getAdjacent(i, j, direction);
    if (height === grid.array[i][j] + 1) {
      return { isReachable: true, position };
    }
  } catch {
    // Ignore out of bounds locations or invalid directions
  }
  return { isReachable: false };
};

const findReachableSummits = (grid: Grid<number>, trailhead: Coord) => {
  const reachableSummits = new Set<string>();
  let rating = 0;
  let currentPaths = [[trailhead]];

  while (currentPaths.length) {
    const newPaths: Coord[][] = [];

    for (const path of currentPaths) {
      const [i, j] = path.at(-1)!;

      for (const direction of validDirections) {
        const { isReachable, position } = isValidLocation(grid, i, j, direction);

        if (isReachable && position) {
          if (grid.array[position[0]][position[1]] === 9) {
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
  const trailheads = findTrailheads(grid);

  let trailheadScores = 0;
  let trailheadRating = 0;

  for (const trailhead of trailheads) {
    const { reachableSummits, rating } = findReachableSummits(grid, trailhead);
    trailheadScores += reachableSummits.size;
    trailheadRating += rating;
  }

  return { trailheadScores, trailheadRating };
};

export const partOne = (puzzleInput: string[]) => analyseMap(puzzleInput).trailheadScores.toString();
export const partTwo = (puzzleInput: string[]) => analyseMap(puzzleInput).trailheadRating.toString();

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('10', 'hoof_it', partOne, partTwo, puzzleInput);
}
