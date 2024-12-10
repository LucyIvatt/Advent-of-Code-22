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

export const partOne = (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((r) => r.split('').map(Number)));
  const trailheads = findTrailheads(grid);

  let trailheadScores = 0;

  for (const trailhead of trailheads) {
    const validSummits = new Set();
    let currentPaths = [[trailhead]];

    // For all paths for a single trail head
    while (currentPaths.length > 0) {
      console.log(currentPaths);
      const newPaths: Coord[][] = [];

      // For each single path
      for (const path of currentPaths) {
        const [i, j] = path.at(-1)!;

        // For each direction possible
        for (const direction of directions) {
          const offset = directionOffsets.get(direction);
          if (!offset) continue;

          try {
            console.log(i, j);
            const { value, position } = grid.getAdjacent(i, j, direction);
            console.log(direction);
            console.log(value, position);

            if (value === grid.array[i][j] + 1) {
              if (value === 9) {
                console.log('hello');
                validSummits.add(`${position}`);
              } else {
                newPaths.push([...path, position]);
              }
            }
          } catch {
            continue;
          }
        }
        console.log('----');
      }
      currentPaths = newPaths;
    }
    console.log(trailhead, validSummits);
    trailheadScores += validSummits.size;
  }

  return trailheadScores.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return 'Part 2 Answer';
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('10', 'hoof_it', partOne, partTwo, puzzleInput);
}
