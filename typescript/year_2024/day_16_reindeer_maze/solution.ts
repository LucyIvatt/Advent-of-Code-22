import path from 'path';
import { coordEquals, Direction, Grid, rotate } from '../../utils/grid';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

function coordToString(coord: [number, number], dir: Direction) {
  return `${coord[0]},${coord[1]},${dir}`;
}

export const partOne = async (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((row) => row.split('')));
  const startPos = grid.find('S')[0];
  const endPos = grid.find('E')[0];

  const validPathScores: number[] = [];
  const validLocations = new Set();
  const currentPaths = [
    {
      coord: startPos,
      dir: Direction.East,
      points: 0,
      visitedDirectionSet: new Set([coordToString(startPos, Direction.East)])
    }
  ];
  const minCostMap = new Map<string, number>();

  while (currentPaths.length > 0) {
    const { coord, dir, points, visitedDirectionSet } = currentPaths.shift()!;
    const coordKey = coordToString(coord, dir);

    if (coordEquals(coord, endPos)) {
      validPathScores.push(points);
      if (points === 11048) {
        for (const item of visitedDirectionSet.values()) {
          const withoutDirection = item.split(',').slice(0, -1);

          validLocations.add(withoutDirection.join());
        }
      }
    }

    // Skip this path if it has a higher cost than the stored minimum
    if (minCostMap.has(coordKey) && minCostMap.get(coordKey)! <= points) {
      continue;
    }
    minCostMap.set(coordKey, points);

    // Directly in front
    const adj = grid.getAdjacent(coord[0], coord[1], dir);
    if (
      adj &&
      adj.value !== '#' &&
      (!minCostMap.has(coordToString(adj.position, dir)) ||
        minCostMap.get(coordToString(adj.position, dir))! > points + 1)
    ) {
      const newVisitedDirectionSet = new Set(visitedDirectionSet);
      newVisitedDirectionSet.add(coordToString(adj.position, dir));
      currentPaths.push({
        coord: adj.position,
        dir: dir,
        points: points + 1,
        visitedDirectionSet: newVisitedDirectionSet
      });
    }

    // Rotate left or right
    for (const turn of [rotate(dir, -90), rotate(dir, 90)]) {
      const adj = grid.getAdjacent(coord[0], coord[1], turn);
      if (
        adj &&
        adj.value !== '#' &&
        (!minCostMap.has(coordToString(adj.position, turn)) ||
          minCostMap.get(coordToString(adj.position, turn))! > points + 1001)
      ) {
        const newVisitedDirectionSet = new Set(visitedDirectionSet);
        newVisitedDirectionSet.add(coordToString(adj.position, turn));
        currentPaths.push({
          coord: adj.position,
          dir: turn,
          points: points + 1001,
          visitedDirectionSet: newVisitedDirectionSet
        });
      }
    }
  }

  console.log(validLocations);
  for (const coord of validLocations) {
    const lol = (coord as string).split(',').map(Number);
    grid.array[lol[0]][lol[1]] = 'O';
  }
  console.log(grid.toString(false));
  return Math.min(...validPathScores).toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return 'Part 2 Answer';
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('16', 'reindeer_maze', partOne, partTwo, puzzleInput);
}
