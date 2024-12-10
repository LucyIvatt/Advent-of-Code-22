import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Coord, Direction, directionOffsets, Grid } from '../../utils/grid';

const directions = [Direction.North, Direction.East, Direction.South, Direction.West];

const findTrailheads = (grid: Grid<number>) => {
  const trailheads: Coord[] = [];

  grid.array.forEach((row, x) => {
    row.forEach((height, y) => {
      if (height === 0) {
        trailheads.push([x, y] as Coord);
      }
    });
  });
  return trailheads;
};

const analyseTrailheads = (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((r) => r.split('').map(Number)));
  const trailheads = findTrailheads(grid);

  let trailheadScores = 0;
  let trailheadRating = 0;

  for (const trailhead of trailheads) {
    const validSummits = new Set();
    let currentPaths = [[trailhead]];

    // For all paths for a single trail head
    while (currentPaths.length > 0) {
      const newPaths: Coord[][] = [];

      // For each single path
      for (const path of currentPaths) {
        const [i, j] = path.at(-1)!;

        // For each direction possible
        for (const direction of directions) {
          const offset = directionOffsets.get(direction);
          if (!offset) continue;

          try {
            const { value, position } = grid.getAdjacent(i, j, direction);

            if (value === grid.array[i][j] + 1) {
              if (value === 9) {
                validSummits.add(`${position}`);
                trailheadRating += 1;
              } else {
                newPaths.push([...path, position]);
              }
            }
          } catch {
            continue;
          }
        }
      }
      currentPaths = newPaths;
    }
    trailheadScores += validSummits.size;
  }
  return { trailheadScores, trailheadRating };
};

export const partOne = (puzzleInput: string[]) => {
  const { trailheadScores } = analyseTrailheads(puzzleInput);
  return trailheadScores.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const { trailheadRating } = analyseTrailheads(puzzleInput);
  return trailheadRating.toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('10', 'hoof_it', partOne, partTwo, puzzleInput);
}
