import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { findDirectionFromOffset, Grid, manhattanDistance, rotate } from '../../utils/grid';

const findAntennaLocations = (grid: Grid<string>) => {
  const symbolMap: Record<string, [number, number][]> = {};

  for (let i = 0; i < grid.array.length; i++) {
    for (let j = 0; j < grid.array[i].length; j++) {
      const symbol = grid.array[i][j];
      if (symbol !== '.') {
        if (!symbolMap[symbol]) {
          symbolMap[symbol] = [];
        }
        symbolMap[symbol].push([i, j]);
      }
    }
  }
  return symbolMap;
};

export const partOne = (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((line) => line.split('')));
  const antennaLocations = findAntennaLocations(grid);

  const antinodeLocations = new Set();

  for (const coordinates of Object.values(antennaLocations)) {
    for (let a = 0; a < coordinates.length; a++) {
      for (let b = a + 1; b < coordinates.length; b++) {
        const dx = coordinates[a][0] - coordinates[b][0];
        const dy = coordinates[a][1] - coordinates[b][1];

        const aNode = [coordinates[a][0] + dx, coordinates[a][1] + dy] as [number, number];
        const bNode = [coordinates[b][0] - dx, coordinates[b][1] - dy] as [number, number];

        if (grid.isValidLocation(aNode)) antinodeLocations.add(`${aNode[0]},${aNode[1]}`);
        if (grid.isValidLocation(bNode)) antinodeLocations.add(`${bNode[0]},${bNode[1]}`);
      }
    }
  }
  return new Set(antinodeLocations).size.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const grid = new Grid(puzzleInput.map((line) => line.split('')));
  const antennaLocations = findAntennaLocations(grid);

  const antinodeLocations = new Set();

  for (const coordinates of Object.values(antennaLocations)) {
    for (let a = 0; a < coordinates.length; a++) {
      for (let b = a + 1; b < coordinates.length; b++) {
        const dx = coordinates[a][0] - coordinates[b][0];
        const dy = coordinates[a][1] - coordinates[b][1];

        let aNode = coordinates[a] as [number, number];
        let bNode = coordinates[b] as [number, number];

        while (grid.isValidLocation(aNode) || grid.isValidLocation(bNode)) {
          if (grid.isValidLocation(aNode)) {
            antinodeLocations.add(`${aNode[0]},${aNode[1]}`);
            aNode = [aNode[0] + dx, aNode[1] + dy];
          }
          if (grid.isValidLocation(bNode)) {
            antinodeLocations.add(`${bNode[0]},${bNode[1]}`);
            bNode = [bNode[0] - dx, bNode[1] - dy];
          }
        }
      }
    }
  }
  return new Set(antinodeLocations).size.toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('08', 'resonant_colinearity', partOne, partTwo, puzzleInput);
}
