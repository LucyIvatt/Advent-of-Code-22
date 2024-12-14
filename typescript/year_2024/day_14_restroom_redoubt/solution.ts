import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const ROBOT_SYMBOL = '#';

class Robot {
  x: number;
  y: number;
  dx: number;
  dy: number;
  gridWidth: number;
  gridHeight: number;

  constructor(robotData: string, gridWidth: number, gridHeight: number) {
    const [x, y, dx, dy] = robotData.match(/-?\d+/g)!.map(Number);
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.gridWidth = gridWidth;
    this.gridHeight = gridHeight;
  }

  movePosition() {
    const newX = (this.x + this.dx) % this.gridWidth;
    const newY = (this.y + this.dy) % this.gridHeight;

    this.x = newX < 0 ? this.gridWidth + newX : newX;
    this.y = newY < 0 ? this.gridHeight + newY : newY;
  }
}

function createGrid(width: number, height: number) {
  return Array(height)
    .fill(0)
    .map(() => Array(width).fill('.'));
}

function printGrid(grid: string[][], width: number, height: number) {
  for (let i = 0; i < height; i++) {
    let row = '.';
    for (let j = 0; j < width; j++) {
      row += grid[i][j];
    }
    console.log(row);
  }
}

function hasTreeStump(grid: string[][], width: number, height: number): boolean {
  for (let r = 0; r <= height - 3; r++) {
    for (let c = 0; c <= width - 3; c++) {
      let isMatch = true;
      for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
          if (grid[r + i][c + j] !== ROBOT_SYMBOL) {
            isMatch = false;
            break;
          }
        }
        if (!isMatch) break;
      }
      if (isMatch) return true;
    }
  }

  return false;
}

export const partOne = (puzzleInput: string[], gridWidth: number, gridHeight: number) => {
  const totalSeconds = 100;
  const robots = puzzleInput.map((data) => new Robot(data, gridWidth, gridHeight));

  for (let second = 0; second < totalSeconds; second++) {
    robots.forEach((robot) => robot.movePosition());
  }

  const centerX = (gridWidth - 1) / 2;
  const centerY = (gridHeight - 1) / 2;

  const quadrantCounts = { first: 0, second: 0, third: 0, fourth: 0 };

  const grid = createGrid(gridWidth, gridHeight);
  robots.forEach((robot) => {
    if (robot.x < centerX && robot.y < centerY) quadrantCounts.first++;
    else if (robot.x < centerX && robot.y > centerY) quadrantCounts.second++;
    else if (robot.x > centerX && robot.y < centerY) quadrantCounts.third++;
    else if (robot.x > centerX && robot.y > centerY) quadrantCounts.fourth++;
  });

  return (quadrantCounts.first * quadrantCounts.second * quadrantCounts.third * quadrantCounts.fourth).toString();
};

export const partTwo = (puzzleInput: string[], gridWidth: number, gridHeight: number) => {
  const robots = puzzleInput.map((data) => new Robot(data, gridWidth, gridHeight));
  let grid = createGrid(gridWidth, gridHeight);
  let seconds = 0;

  while (!hasTreeStump(grid, gridWidth, gridHeight)) {
    grid = createGrid(gridWidth, gridHeight);
    robots.forEach((robot) => {
      robot.movePosition();
      grid[robot.y][robot.x] = ROBOT_SYMBOL;
    });
    seconds += 1;
  }

  printGrid(grid, gridWidth, gridHeight);
  return seconds.toString();
};

if (require.main === module) {
  let width;
  let height;

  const inputType = InputFile.INPUT;

  // @ts-expect-error so I can switch input files without needing to redefine width/height
  if (inputType === InputFile.EXAMPLE) {
    width = 11;
    height = 7;
  } else {
    width = 101;
    height = 103;
  }

  const puzzleInput = readPuzzleInput(path.resolve(__dirname, inputType));
  runPuzzle('14', 'restroom_redoubt', partOne, partTwo, puzzleInput, width, height);
}
