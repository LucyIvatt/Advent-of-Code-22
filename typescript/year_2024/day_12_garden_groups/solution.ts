import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Coord, DIAGONAL_DIRECTIONS, Direction, Grid, rotate, STRAIGHT_DIRECTIONS } from '../../utils/grid';

// Rotate directions by 45 degrees and find the common direction
export const getDiagonalDirectionForLShape = (directions: Direction[]): Direction => {
  const [dir1, dir2] = directions;

  const diagonals1 = [rotate(dir1, 45), rotate(dir1, -45)];
  const diagonals2 = [rotate(dir2, 45), rotate(dir2, -45)];

  const [diagonal] = diagonals1.filter((d) => diagonals2.includes(d));
  return diagonal;
};

// finds middle direction by getting the direction 90 degrees left and right and checking if the array includes them
export const getDiagonalDirectionsForTShape = (directions: Direction[]): Direction[] => {
  const middle = directions.find(
    (dir) => directions.includes(rotate(dir, 90)) && directions.includes(rotate(dir, -90))
  )!;

  const diagonal1 = rotate(middle, 45); // Clockwise diagonal
  const diagonal2 = rotate(middle, -45); // Counterclockwise diagonal
  return [diagonal1, diagonal2];
};

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

const findOpenSides = (i: number, j: number, grid: Grid<string>, region: Region) => {
  const openSides = [];
  const typeOfPlant = grid.array[i][j];
  const openDirections = [];
  let perimeter = 0;

  for (const direction of STRAIGHT_DIRECTIONS) {
    try {
      const { value, position } = grid.getAdjacent(i, j, direction);
      if (typeOfPlant !== value) perimeter += 1;
      else {
        if (!coordInList(position, region.locations)) openSides.push(position);
        openDirections.push(direction);
      }
    } catch {
      perimeter += 1;
    }
  }

  let corners = 0;

  if (openDirections.length === 0) corners = 4; // single cell region, must have 4 corners
  if (openDirections.length === 1) corners = 2; // end of a tunnel, must always have 2 corners

  // no corners if opposite ends open (but if L shape could have 1 or 2 corners)
  if (openDirections.length === 2 && openDirections[0] !== rotate(openDirections[1], 180)) {
    const diag = getDiagonalDirectionForLShape(openDirections);
    try {
      const diagonal = grid.getAdjacent(i, j, diag);
      if (diagonal.value === typeOfPlant)
        corners = 1; // valid position directly diagonal from L shape corneer (no addtional corner needed)
      else corners = 2; // corner direction diagonal from L shape corner
    } catch {
      corners = 2; // corner direction diagonal from L shape corner
    }
  }
  // T shaped opening - could have 2 additional corners
  if (openDirections.length === 3) {
    const diagonalDirections = getDiagonalDirectionsForTShape(openDirections);

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

  // completely open space, could have up to 4 additional corners
  if (openDirections.length === 4) {
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

          const { openSides, perimeter, corners } = findOpenSides(coordToProcess[0], coordToProcess[1], plants, region);
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
