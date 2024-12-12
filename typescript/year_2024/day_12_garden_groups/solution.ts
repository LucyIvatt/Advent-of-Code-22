import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Coord, DIAGONAL_DIRECTIONS, Direction, Grid, rotate } from '../../utils/grid';

export const getDiagonalDirectionsForTShape = (directions: Direction[]): Direction[] => {
  const [d1, d2, d3] = directions;
  const stem = [d1, d2, d3].find(
    (dir) => directions.includes(rotate(dir, 90)) && directions.includes(rotate(dir, -90))
  )!;

  const diagonal1 = rotate(stem, 45); // Clockwise diagonal
  const diagonal2 = rotate(stem, -45); // Counterclockwise diagonal
  return [diagonal1, diagonal2];
};

const VALID_DIRECTIONS = [Direction.North, Direction.East, Direction.South, Direction.West];

const coordEquals = (a: Coord, b: Coord): boolean => a[0] === b[0] && a[1] === b[1];
const coordInList = (coord: Coord, list: Coord[]): boolean => list.some((c) => coordEquals(c, coord));

const calculatePrice = (regions: Region[]) => {
  return regions.reduce((acc, region) => {
    return (acc += region.perimeter * region.getArea());
  }, 0);
};

export class Region {
  plantType: string;
  startLocation: Coord;
  locations: Coord[];
  perimeter: number;
  corners: number;

  constructor(plantType: string, startLocation: Coord) {
    this.plantType = plantType;
    this.startLocation = startLocation;
    this.locations = [startLocation];
    this.perimeter = 0;
    this.corners = 0;
  }

  getArea = () => this.locations.length;
  getSecondPrice = () => this.getArea() * this.corners;
}

const getOpenSides = (i: number, j: number, grid: Grid<string>, region: Region) => {
  const openSides = [];
  const typeOfPlant = grid.array[i][j];
  const directionOfMatch = [];
  let perimeter = 0;

  for (const dir of VALID_DIRECTIONS) {
    try {
      const { value, position } = grid.getAdjacent(i, j, dir);
      if (typeOfPlant !== value) perimeter += 1;
      else {
        if (!coordInList(position, region.locations)) openSides.push(position);
        directionOfMatch.push(dir);
      }
    } catch {
      perimeter += 1;
    }
  }

  let corners = 0;
  if (directionOfMatch.length === 1) corners = 2; // end of tunnel, must have 2 corners

  // no corners if opposite ends open (but if L shape could have 1 or 2 corners)
  if (directionOfMatch.length === 2 && directionOfMatch[0] !== rotate(directionOfMatch[1], 180)) {
    const diag = getDiagonalDirection(directionOfMatch[0], directionOfMatch[1])!;
    try {
      const diagonal = grid.getAdjacent(i, j, diag);
      if (diagonal.value === typeOfPlant) corners = 1;
      else corners = 2;
    } catch {
      corners = 2;
    }
  }
  // could have no corners, 1, or even 2 if T shaped
  if (directionOfMatch.length === 3) {
    const diagonalDirections = getDiagonalDirectionsForTShape(directionOfMatch);

    let invalidDiags = 0;
    for (const diagDirec of diagonalDirections) {
      try {
        const diagonal = grid.getAdjacent(i, j, diagDirec);
        if (diagonal.value !== typeOfPlant) invalidDiags += 1;
      } catch {
        invalidDiags += 1;
      }
    }
    corners = invalidDiags;
  }
  if (directionOfMatch.length === 0) corners = 4; // single cell region, must have 4 corners

  if (directionOfMatch.length === 4) {
    let invalidDiags = 0;
    for (const diagDirec of DIAGONAL_DIRECTIONS) {
      try {
        const diagonal = grid.getAdjacent(i, j, diagDirec);
        if (diagonal.value !== typeOfPlant) invalidDiags += 1;
      } catch {
        invalidDiags += 1;
      }
    }
    corners = invalidDiags;
  }

  return { openSides, perimeter, corners };
};

function getDiagonalDirection(dir1: Direction, dir2: Direction): Direction | null {
  const directionSet = new Set([dir1, dir2]);

  if (directionSet.has(Direction.North) && directionSet.has(Direction.East)) {
    return Direction.NorthEast;
  } else if (directionSet.has(Direction.East) && directionSet.has(Direction.South)) {
    return Direction.SouthEast;
  } else if (directionSet.has(Direction.South) && directionSet.has(Direction.West)) {
    return Direction.SouthWest;
  } else if (directionSet.has(Direction.West) && directionSet.has(Direction.North)) {
    return Direction.NorthWest;
  }

  return null; // Return null if the directions are not at a 90-degree angle
}

const findRegions = (plants: Grid<string>) => {
  let processedCoords: Coord[] = [];
  const regions: Region[] = [];

  plants.array.forEach((line, i) => {
    line.forEach((plant, j) => {
      if (!coordInList([i, j], processedCoords)) {
        const region = new Region(plant, [i, j]);
        regions.push(region);

        let coordsToProcess: Coord[] = [[i, j]];
        processedCoords.push([i, j]);

        while (coordsToProcess.length > 0) {
          const coordToProcess = coordsToProcess[0];

          const { openSides, perimeter, corners } = getOpenSides(coordToProcess[0], coordToProcess[1], plants, region);
          region.perimeter += perimeter;
          region.corners += corners;

          region.locations = region.locations.concat(openSides);

          coordsToProcess.splice(0, 1);
          coordsToProcess = coordsToProcess.concat(openSides);
          processedCoords = processedCoords.concat([coordToProcess]);
        }
      }
    });
  });
  return regions;
};

export const partOne = (puzzleInput: string[]) => {
  const plants = new Grid(puzzleInput.map((row) => row.split('')));
  const regions = findRegions(plants);
  return calculatePrice(regions).toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const plants = new Grid(puzzleInput.map((row) => row.split('')));
  const regions = findRegions(plants);
  let price = 0;
  regions.forEach((region) => {
    price += region.getSecondPrice();
  });
  return price.toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('12', 'garden_groups', partOne, partTwo, puzzleInput);
}
