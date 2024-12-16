import { MinPriorityQueue } from '@datastructures-js/priority-queue';
import path from 'path';
import { Coord, coordEquals, Direction, Grid, rotate } from '../../utils/grid';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

interface Path {
  coord: Coord;
  dir: Direction;
  points: number;
  visitedKeys: Set<string>;
}

const createCoordKey = (coord: [number, number], dir: Direction) => {
  return `${coord[0]},${coord[1]},${dir}`;
};

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

    if (points > minCost) break; // finish early if this is true as nothing left in queue that is cheaper

    const coordKey = createCoordKey(coord, dir);
    if (visitedMap.has(coordKey) && visitedMap.get(coordKey)! < points) {
      continue;
    }
    visitedMap.set(coordKey, points);

    if (coordEquals(coord, endPos)) {
      minCost = points;

      for (const item of visitedKeys.values()) {
        const withoutDirection = item.split(',').slice(0, -1);
        validCoordinates.add(withoutDirection.join());
      }
    }

    const processAdjacent = (coord: Coord, dir: Direction, points: number, visitedKeys: Set<string>, cost: number) => {
      const adj = grid.getAdjacent(coord[0], coord[1], dir);
      // tries to avoid loop with the visitedKeys check
      if (adj && adj.value !== '#' && !visitedKeys.has(createCoordKey(adj.position, dir))) {
        const newVisitedKeys = new Set([...visitedKeys]);
        newVisitedKeys.add(createCoordKey(adj.position, dir));
        pq.enqueue({
          coord: adj.position,
          dir: dir,
          points: points + cost,
          visitedKeys: newVisitedKeys
        });
      }
    };

    processAdjacent(coord, dir, points, visitedKeys, 1); // move straight

    for (const turn of [rotate(dir, -90), rotate(dir, 90)]) {
      processAdjacent(coord, turn, points, visitedKeys, 1001); // rotate 90 degrees
    }
  }
  return { minCost, tiles: validCoordinates.size };
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
