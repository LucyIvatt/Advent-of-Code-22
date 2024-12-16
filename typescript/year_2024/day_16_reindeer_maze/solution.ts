import { MinPriorityQueue } from '@datastructures-js/priority-queue';
import path from 'path';
import { Coord, coordEquals, Direction, Grid, rotate } from '../../utils/grid';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const exploreMaze = (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((row) => row.split('')));
  const startPos = grid.find('S')[0];
  const endPos = grid.find('E')[0];

  let minCost = Infinity;
  const validCoordinates: Set<string> = new Set();

  const pq = new MinPriorityQueue<Path>((path) => path.points);
  pq.enqueue({
    coord: startPos,
    dir: Direction.East,
    points: 0,
    visitedKeys: new Set([createCoordKey(startPos, Direction.East)])
  });

  const visitedMap = new Map<string, number>();

  while (!pq.isEmpty()) {
    const { coord, dir, points, visitedKeys } = pq.dequeue()!;
    const coordKey = createCoordKey(coord, dir);

    if ((visitedMap.has(coordKey) && visitedMap.get(coordKey)! < points) || points > minCost) {
      continue;
    }

    visitedMap.set(coordKey, points);

    if (coordEquals(coord, endPos)) {
      minCost = points;

      for (const item of visitedKeys.values()) {
        const withoutDirection = item.split(',').slice(0, -1); // Remove direction
        validCoordinates.add(withoutDirection.join());
      }
    }

    // Directly in front
    const adj = grid.getAdjacent(coord[0], coord[1], dir);
    if (adj && adj.value !== '#' && !visitedKeys.has(createCoordKey(adj.position, dir))) {
      const newvisitedKeys = new Set([...visitedKeys]);
      newvisitedKeys.add(createCoordKey(adj.position, dir));
      pq.enqueue({
        coord: adj.position,
        dir: dir,
        points: points + 1,
        visitedKeys: newvisitedKeys
      });
    }

    // Rotate left or right
    for (const turn of [rotate(dir, -90), rotate(dir, 90)]) {
      const adj = grid.getAdjacent(coord[0], coord[1], turn);
      if (adj && adj.value !== '#' && !visitedKeys.has(createCoordKey(adj.position, turn))) {
        const newvisitedKeys = new Set([...visitedKeys]);
        newvisitedKeys.add(createCoordKey(adj.position, turn));
        pq.enqueue({
          coord: adj.position,
          dir: turn,
          points: points + 1001,
          visitedKeys: newvisitedKeys
        });
      }
    }
  }
  return { minCost, tiles: validCoordinates.size };
};

interface Path {
  coord: Coord;
  dir: Direction;
  points: number;
  visitedKeys: Set<string>;
}

const createCoordKey = (coord: [number, number], dir: Direction) => {
  return `${coord[0]},${coord[1]},${dir}`;
};

export const partOne = (puzzleInput: string[]) => {
  return exploreMaze(puzzleInput).minCost.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return exploreMaze(puzzleInput).tiles.toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('16', 'reindeer_maze', partOne, partTwo, puzzleInput);
}
