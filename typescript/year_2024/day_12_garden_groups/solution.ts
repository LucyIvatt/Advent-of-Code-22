import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Coord, Direction, Grid } from '../../utils/grid';

// for each coordinate, check if tis been processed or skip

// if not been processed, create a new region,
// iterate through open sides (need to find a way to not reprocess backwards) - keep previous and say if not previous?
// for each cell, add closed sides to permeter and add to list of processed coordinates

// finish when open coordinates  queue to process is empty
// once done find the area by counting cooordinates

const coordEquals = (a: Coord, b: Coord): boolean => a[0] === b[0] && a[1] === b[1];
const coordInList = (coord: Coord, list: Coord[]): boolean => list.some((c) => coordEquals(c, coord));

export class Region {
  plantType: string;
  startLocation: Coord;
  locations: Coord[];
  area: number;
  perimeter: number;

  constructor(plantType: string, startLocation: Coord) {
    this.plantType = plantType;
    this.startLocation = startLocation;
    this.locations = [startLocation];
    this.area = 0;
    this.perimeter = 0;
  }
}

const VALID_DIRECTIONS = [Direction.North, Direction.East, Direction.South, Direction.West];

const getOpenSides = (i: number, j: number, grid: Grid<string>, region: Region) => {
  const openSides = [];
  const typeOfPlant = grid.array[i][j];
  let perimeter = 0;

  for (const dir of VALID_DIRECTIONS) {
    try {
      const { value, position } = grid.getAdjacent(i, j, dir);
      if (typeOfPlant !== value) perimeter += 1;
      else {
        if (!coordInList(position, region.locations)) openSides.push(position);
      }
    } catch {
      perimeter += 1;
    }
  }
  return { openSides, perimeter };
};

export const partOne = (puzzleInput: string[]) => {
  const plants = new Grid(puzzleInput.map((row) => row.split('')));
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

          const { openSides, perimeter } = getOpenSides(coordToProcess[0], coordToProcess[1], plants, region);
          region.perimeter += perimeter;

          region.locations = region.locations.concat(openSides);

          coordsToProcess.splice(0, 1);
          coordsToProcess = coordsToProcess.concat(openSides);
          processedCoords = processedCoords.concat([coordToProcess]);
        }
      }
    });
  });

  console.log(regions);

  // const processedLocations: Coord[] = [];
  // console.log(plants);

  return 'Part 1 Answer';
};

export const partTwo = (puzzleInput: string[]) => {
  return 'Part 2 Answer';
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('12', 'garden_groups', partOne, partTwo, puzzleInput);
}
