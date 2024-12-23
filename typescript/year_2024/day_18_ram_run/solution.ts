import { MinPriorityQueue } from '@datastructures-js/priority-queue';
import path from 'path';
import { Coord, coordEquals, Grid, STRAIGHT_DIRECTIONS } from '../../utils/grid';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

interface Path {
  coord: Coord;
  points: number;
}

const createGrid = (input: string[], gridSize: number, bytes: number): Grid<string> => {
  const grid = new Grid(Array.from({ length: gridSize }, () => Array.from({ length: gridSize }, () => '.')));
  for (const coord of input.slice(0, bytes)) {
    const [x, y] = coord.split(',').map(Number);
    grid.array[y][x] = '#';
  }
  return grid;
};

const createCoordKey = (coord: [number, number]) => {
  return `${coord[0]},${coord[1]}`;
};

const exploreGrid = (grid: Grid<string>) => {
  const endPos = [grid.array.length - 1, grid.array.length - 1] as Coord;
  let minCost = Infinity;

  const pq = new MinPriorityQueue<Path>((path) => path.points);
  const visited = new Map<string, number>();

  pq.enqueue({ coord: [0, 0], points: 0 });

  while (!pq.isEmpty()) {
    const { coord, points } = pq.dequeue()!;

    if (coordEquals(coord, endPos)) {
      minCost = Math.min(minCost, points);
      continue;
    }

    const coordKey = createCoordKey(coord);
    if (visited.has(coordKey) && visited.get(coordKey)! <= points) continue;

    visited.set(coordKey, points);

    for (const direction of STRAIGHT_DIRECTIONS) {
      const adj = grid.getAdjacent(coord[0], coord[1], direction);
      if (adj && adj.value !== '#') {
        const adjKey = createCoordKey(adj.position);
        if (!visited.has(adjKey) || visited.get(adjKey)! > points + 1) {
          pq.enqueue({ coord: adj.position, points: points + 1 });
        }
      }
    }
  }
  return minCost;
};

export const partOne = (puzzleInput: string[], size: number, bytes: number) => {
  const grid = createGrid(puzzleInput, size, bytes);
  return exploreGrid(grid).toString();
};

export const partTwo = (puzzleInput: string[], size: number) => {
  let lowerBound = 0;
  let upperBound = puzzleInput.length - 1;

  const isPathBlocked = (mid: number): boolean => {
    const grid = createGrid(puzzleInput, size, mid);
    const pathLength = exploreGrid(grid);
    return pathLength === Infinity;
  };

  let result = -1;

  while (lowerBound <= upperBound) {
    const mid = Math.floor((lowerBound + upperBound) / 2);

    if (isPathBlocked(mid)) {
      result = mid;
      upperBound = mid - 1;
    } else {
      lowerBound = mid + 1;
    }
  }

  return puzzleInput[result - 1];
};

if (require.main === module) {
  const inputType = InputFile.INPUT;
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, inputType));

  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore so I can switch input files without needing to redefine width/height
  const { size, bytes } = inputType === InputFile.EXAMPLE ? { size: 7, bytes: 12 } : { size: 71, bytes: 1024 };
  runPuzzle('18', 'ram_run', partOne, partTwo, puzzleInput, size, bytes);
}
