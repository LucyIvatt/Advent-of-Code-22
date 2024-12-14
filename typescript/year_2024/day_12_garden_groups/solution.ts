import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Coord, DIAGONAL_DIRECTIONS, Direction, Grid, rotate, STRAIGHT_DIRECTIONS } from '../../utils/grid';

class Region {
  plantType: string;
  startLocation: Coord;
  locations: Coord[] = [];
  perimeter: number = 0;
  corners: number = 0;

  constructor(plantType: string, startLocation: Coord) {
    this.plantType = plantType;
    this.startLocation = startLocation;
    this.locations.push(startLocation);
  }

  getArea = () => this.locations.length;
  getFencePrice = () => this.getArea() * this.perimeter;
  getDiscountPrice = () => this.getArea() * this.corners;
}

// Rotate directions by 45 degrees and find the common direction
const getDiagonalDirectionForLShape = (directions: Direction[]): Direction => {
  const [dir1, dir2] = directions;
  const diagonals1 = [rotate(dir1, 45), rotate(dir1, -45)];
  const diagonals2 = [rotate(dir2, 45), rotate(dir2, -45)];

  return diagonals1.find((d) => diagonals2.includes(d))!;
};

// Finds middle direction for T shape and provides diagonal directions 45 degrees either side of it
const getDiagonalDirectionsForTShape = (directions: Direction[]): Direction[] => {
  const middle = directions.find(
    (dir) => directions.includes(rotate(dir, 90)) && directions.includes(rotate(dir, -90))
  )!;

  return [rotate(middle, 45), rotate(middle, -45)];
};

const coordEquals = (a: Coord, b: Coord): boolean => a[0] === b[0] && a[1] === b[1];

const findOpenSides = (i: number, j: number, grid: Grid<string>, region: Region) => {
  const openSides: Coord[] = [];
  const plantType = grid.array[i][j];
  const openDirections: Direction[] = [];
  let perimeter = 0;
  let corners = 0;

  for (const direction of STRAIGHT_DIRECTIONS) {
    const adjacent = grid.getAdjacent(i, j, direction);
    if (!adjacent) perimeter += 1;
    else {
      if (adjacent.value !== plantType) perimeter += 1;
      else {
        if (!region.locations.some((coord) => coordEquals(coord, adjacent.position))) openSides.push(adjacent.position);
        openDirections.push(direction);
      }
    }
  }

  switch (openDirections.length) {
    case 0:
      corners = 4;
      break;
    case 1:
      corners = 2;
      break;
    case 2:
      if (openDirections[0] !== rotate(openDirections[1], 180)) {
        const diagonalDir = getDiagonalDirectionForLShape(openDirections);
        const diagonalAdjacent = grid.getAdjacent(i, j, diagonalDir);
        corners = diagonalAdjacent && diagonalAdjacent.value === plantType ? 1 : 2;
      }
      break;
    case 3: {
      const diagonalDirs = getDiagonalDirectionsForTShape(openDirections);
      corners = diagonalDirs.reduce((count, dir) => {
        const diagAdjacent = grid.getAdjacent(i, j, dir);
        return count + (diagAdjacent && diagAdjacent.value === plantType ? 0 : 1);
      }, 0);
      break;
    }
    case 4:
      corners = DIAGONAL_DIRECTIONS.reduce((count, dir) => {
        const diagAdjacent = grid.getAdjacent(i, j, dir);
        return count + (diagAdjacent && diagAdjacent.value === plantType ? 0 : 1);
      }, 0);
      break;
  }

  return { openSides, perimeter, corners };
};
const findRegions = (plants: Grid<string>): Region[] => {
  const processed: Coord[] = [];
  const regions: Region[] = [];

  plants.array.forEach((row, i) => {
    row.forEach((plant, j) => {
      if (!processed.some((coord) => coordEquals(coord, [i, j]))) {
        const region = new Region(plant, [i, j]);
        regions.push(region);

        const toProcess: Coord[] = [[i, j]];
        processed.push([i, j]);

        while (toProcess.length > 0) {
          const coord = toProcess.shift()!;
          const { openSides, perimeter, corners } = findOpenSides(coord[0], coord[1], plants, region);

          region.perimeter += perimeter;
          region.corners += corners;
          region.locations.push(...openSides);
          toProcess.push(...openSides);
          processed.push(coord);
        }
      }
    });
  });
  return regions;
};

export const partOne = (puzzleInput: string[]) => {
  return findRegions(new Grid(puzzleInput.map((row) => row.split(''))))
    .reduce((acc, region) => acc + region.getFencePrice(), 0)
    .toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return findRegions(new Grid(puzzleInput.map((row) => row.split(''))))
    .reduce((acc, region) => acc + region.getDiscountPrice(), 0)
    .toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('12', 'garden_groups', partOne, partTwo, puzzleInput);
}
