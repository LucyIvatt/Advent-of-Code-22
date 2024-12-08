import path from 'path';
import { Coord, Grid } from '../../utils/grid';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const findAntennaLocations = (grid: Grid<string>) => {
  const locations: Record<string, Coord[]> = {};

  grid.array.forEach((row, x) => {
    row.forEach((symbol, y) => {
      if (symbol !== '.') {
        (locations[symbol] ||= []).push([x, y]);
      }
    });
  });

  return locations;
};

const findAntinodes = (grid: Grid<string>, antennaLocations: Record<string, Coord[]>, shouldExtend = false) => {
  const antinodes = new Set<string>();

  const addAntinodes = (coords: Coord[]) => {
    coords.forEach((coord) => {
      if (grid.isValidLocation(coord)) {
        antinodes.add(coord.join(','));
      }
    });
  };

  for (const coords of Object.values(antennaLocations)) {
    for (let i = 0; i < coords.length; i++) {
      for (let j = i + 1; j < coords.length; j++) {
        const [dx, dy] = [coords[i][0] - coords[j][0], coords[i][1] - coords[j][1]];
        let forward = [coords[i][0] + dx, coords[i][1] + dy] as Coord;
        let backward = [coords[j][0] - dx, coords[j][1] - dy] as Coord;

        if (!shouldExtend) {
          addAntinodes([forward, backward]);
        }

        while (shouldExtend) {
          if (![forward, backward].some((i) => grid.isValidLocation(i))) break;

          addAntinodes([forward, backward]);

          forward = [forward[0] + dx, forward[1] + dy];
          backward = [backward[0] - dx, backward[1] - dy];
        }
      }
    }
  }
  return antinodes;
};

export const partOne = (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((line) => line.split('')));
  const antennaLocations = findAntennaLocations(grid);
  return findAntinodes(grid, antennaLocations).size.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((line) => line.split('')));
  const antennaLocations = findAntennaLocations(grid);
  const antinodes = findAntinodes(grid, antennaLocations, true);

  // Include antenna locations as antinodes
  for (const coords of Object.values(antennaLocations)) {
    for (const coord of coords) {
      antinodes.add(coord.join(','));
    }
  }

  return antinodes.size.toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('08', 'resonant_colinearity', partOne, partTwo, puzzleInput);
}
