import { clear } from 'console';
import { createGrid, hasTreeStump, printGrid, Robot, updateGrid } from './solution';
import { delay } from '../../utils/time';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import path from 'path';

export const partTwoAnimation = async (puzzleInput: string[], gridWidth: number, gridHeight: number) => {
  const robots = puzzleInput.map((data) => new Robot(data, gridWidth, gridHeight));
  const grid = createGrid(gridWidth, gridHeight);

  robots.forEach((robot) => robot.movePosition(7850));

  while (!hasTreeStump(grid, robots)) {
    robots.forEach((robot) => robot.movePosition());
    updateGrid(grid, robots);
    clear();
    printGrid(grid);
    await delay(500);
  }

  printGrid(grid, true);
};

const run = async () => {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  await partTwoAnimation(puzzleInput, 101, 103);
};

run();
