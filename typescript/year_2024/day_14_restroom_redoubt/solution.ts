import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import chalk from 'chalk';

const ROBOT_SYMBOL = '#';
const EMPTY_SYMBOL = '.';

export class Robot {
  position: { x: number; y: number };
  velocity: { dx: number; dy: number };
  gridWidth: number;
  gridHeight: number;

  constructor(robotData: string, gridWidth: number, gridHeight: number) {
    const [x, y, dx, dy] = robotData.match(/-?\d+/g)!.map(Number);
    this.position = { x, y };
    this.velocity = { dx, dy };
    this.gridWidth = gridWidth;
    this.gridHeight = gridHeight;
  }

  movePosition(steps: number = 1) {
    this.position.x = this.teleport(this.position.x + this.velocity.dx * steps, this.gridWidth);
    this.position.y = this.teleport(this.position.y + this.velocity.dy * steps, this.gridHeight);
  }

  private teleport(position: number, limit: number) {
    return ((position % limit) + limit) % limit;
  }
}

export const createGrid = (width: number, height: number) =>
  Array.from({ length: height }, () => Array(width).fill(EMPTY_SYMBOL));

export const printGrid = (grid: string[][], green = false) => {
  const print = green ? chalk.green : (x: any) => x;
  grid.forEach((row) => console.log(print(row.join(''))));
};

export const updateGrid = (grid: string[][], robots: Robot[]) => {
  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid[0].length; x++) {
      grid[y][x] = EMPTY_SYMBOL;
    }
  }

  robots.forEach(({ position: { x, y } }) => {
    grid[y][x] = ROBOT_SYMBOL;
  });
};

export const hasTreeStump = (grid: string[][], robots: Robot[]) => {
  for (const {
    position: { x, y }
  } of robots) {
    if (x >= 1 && y >= 1 && x < grid[0].length - 1 && y < grid.length - 1) {
      if (
        Array.from({ length: 3 }).every((_, i) =>
          Array.from({ length: 3 }).every((_, j) => grid[y + i - 1][x + j - 1] === ROBOT_SYMBOL)
        )
      )
        return true;
    }
  }
  return false;
};

export const partOne = (puzzleInput: string[], gridWidth: number, gridHeight: number) => {
  const robots = puzzleInput.map((data) => new Robot(data, gridWidth, gridHeight));

  robots.forEach((robot) => robot.movePosition(100));

  const centerX = (gridWidth - 1) / 2;
  const centerY = (gridHeight - 1) / 2;
  const quadrants = [0, 0, 0, 0];

  robots
    .filter(({ position: { x, y } }) => x !== centerX && y !== centerY) // excludes the robots on axes
    .forEach(({ position: { x, y } }) => {
      const quadrant = (x > centerX ? 2 : 0) + (y > centerY ? 1 : 0);
      quadrants[quadrant]++;
    });

  return quadrants.reduce((val, acc) => (acc *= val)).toString();
};

export const partTwo = (puzzleInput: string[], gridWidth: number, gridHeight: number, log = false) => {
  const robots = puzzleInput.map((data) => new Robot(data, gridWidth, gridHeight));
  const grid = createGrid(gridWidth, gridHeight);

  let seconds = 0;
  while (!hasTreeStump(grid, robots)) {
    robots.forEach((robot) => robot.movePosition());
    updateGrid(grid, robots);
    seconds++;
  }

  if (log) printGrid(grid);

  return seconds.toString();
};

if (require.main === module) {
  const inputType = InputFile.INPUT;

  // @ts-expect-error so I can switch input files without needing to redefine width/height
  const { width, height } = inputType === InputFile.EXAMPLE ? { width: 11, height: 7 } : { width: 101, height: 103 };

  const puzzleInput = readPuzzleInput(path.resolve(__dirname, inputType));
  runPuzzle('14', 'restroom_redoubt', partOne, partTwo, puzzleInput, width, height, true);

  // partTwoAnimation(puzzleInput, width, height);
}
