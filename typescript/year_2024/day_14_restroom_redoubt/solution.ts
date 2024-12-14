import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const WIDTH = 101;
const HEIGHT = 103;

class Robot {
  x: number;
  y: number;
  dx: number;
  dy: number;

  constructor(robotData: string) {
    const [x, y, dx, dy] = robotData.match(/-?\d+/g)!.map(Number);
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
  }

  movePos() {
    const newX = this.x + this.dx;
    const newY = this.y + this.dy;

    if (newX < 0) this.x = WIDTH + newX;
    else if (newX >= WIDTH) this.x = newX - WIDTH;
    else this.x = newX;

    if (newY < 0) this.y = HEIGHT + newY;
    else if (newY >= HEIGHT) this.y = newY - HEIGHT;
    else this.y = newY;
  }
}

function createGrid() {
  return Array(HEIGHT)
    .fill(0)
    .map(() => Array(WIDTH).fill('.'));
}

function printGrid(grid: string[][]) {
  for (let i = 0; i < HEIGHT; i++) {
    let row = '';
    for (let j = 0; j < WIDTH; j++) {
      row += grid[i][j];
    }
    console.log(row);
  }
}

export const partOne = (puzzleInput: string[]) => {
  const seconds = 100;
  const robots = puzzleInput.map((robot) => new Robot(robot));

  for (let s = 0; s < seconds; s++) {
    for (const robot of robots) {
      robot.movePos();
    }
  }

  const midX = (WIDTH - 1) / 2;
  const midY = (HEIGHT - 1) / 2;

  const quadrants = { quad_1: 0, quad_2: 0, quad_3: 0, quad_4: 0 };

  const grid = createGrid();
  for (const robot of robots) {
    if (robot.x < midX && robot.y < midY) quadrants.quad_1++;
    if (robot.x < midX && robot.y > midY) quadrants.quad_2++;
    if (robot.x > midX && robot.y < midY) quadrants.quad_3++;
    if (robot.x > midX && robot.y > midY) quadrants.quad_4++;

    if (grid[robot.y][robot.x] == 'o') grid[robot.y][robot.x] = 'O';
    else grid[robot.y][robot.x] = 'o';
  }

  printGrid(grid);
  console.log(quadrants);

  return (quadrants.quad_1 * quadrants.quad_2 * quadrants.quad_3 * quadrants.quad_4).toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return 'Part 2 Answer';
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('14', 'restroom_redoubt', partOne, partTwo, puzzleInput);
}
