import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

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

  movePos() {
    const newX = this.x + this.dx;
    const newY = this.y + this.dy;

    if (newX < 0) this.x = this.gridWidth + newX;
    else if (newX >= this.gridWidth) this.x = newX - this.gridWidth;
    else this.x = newX;

    if (newY < 0) this.y = this.gridHeight + newY;
    else if (newY >= this.gridHeight) this.y = newY - this.gridHeight;
    else this.y = newY;
  }
}

function createGrid(width: number, height: number) {
  return Array(height)
    .fill(0)
    .map(() => Array(width).fill('.'));
}

function printGrid(grid: string[][], width: number, height: number) {
  for (let i = 0; i < height; i++) {
    let row = '';
    for (let j = 0; j < width; j++) {
      row += grid[i][j];
    }
    console.log(row);
  }
}

export const partOne = (puzzleInput: string[], width: number, height: number) => {
  const seconds = 100;
  const robots = puzzleInput.map((robot) => new Robot(robot, width, height));

  for (let s = 0; s < seconds; s++) {
    for (const robot of robots) {
      robot.movePos();
    }
  }

  const midX = (width - 1) / 2;
  const midY = (height - 1) / 2;

  console.log(midX);
  console.log(midY);

  const quadrants = { quad_1: 0, quad_2: 0, quad_3: 0, quad_4: 0 };

  const grid = createGrid(width, height);
  for (const robot of robots) {
    console.log(robot);
    if (robot.x < midX && robot.y < midY) quadrants.quad_1++;
    if (robot.x < midX && robot.y > midY) quadrants.quad_2++;
    if (robot.x > midX && robot.y < midY) quadrants.quad_3++;
    if (robot.x > midX && robot.y > midY) quadrants.quad_4++;

    if (grid[robot.y][robot.x] == 'o') grid[robot.y][robot.x] = 'O';
    else grid[robot.y][robot.x] = 'o';
  }

  printGrid(grid, width, height);

  console.log(quadrants);

  return (quadrants.quad_1 * quadrants.quad_2 * quadrants.quad_3 * quadrants.quad_4).toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return 'Part 2 Answer';
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
