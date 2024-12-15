import path from 'path';
import { InputFile, readPuzzleInput, split2DArray } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Coord, Direction, directionOffsets, Grid } from '../../utils/grid';

import { Tree, TreeNode, defaultTraversalStrategy } from 'ts-tree-lib';

const DIRECTION_MAP = new Map<string, Direction>([
  ['^', Direction.North],
  ['>', Direction.East],
  ['v', Direction.South],
  ['<', Direction.West]
]);

const expandGrid = (grid: string[]) => {
  const newGrid = grid.map((row) =>
    row.split('').flatMap((char) => {
      switch (char) {
        case '#': {
          return ['#', '#'];
        }
        case 'O': {
          return ['[', ']'];
        }
        case '.': {
          return ['.', '.'];
        }
        case '@': {
          return ['@', '.'];
        }
        default: {
          return ['.', '.'];
        }
      }
    })
  );

  return newGrid;
};

export const partOne = (puzzleInput: string[]) => {
  const formattedInput = split2DArray(puzzleInput, '');

  const grid = new Grid(formattedInput[0].map((row) => row.split('')));
  const directions = formattedInput[1].flatMap((line) => line.split('').map((char) => DIRECTION_MAP.get(char)!));

  let robotPosition = grid.find('@')[0];

  for (const direction of directions) {
    const nextCell = grid.getAdjacent(robotPosition[0], robotPosition[1], direction);

    if (nextCell?.value == '.') {
      grid.array[robotPosition[0]][robotPosition[1]] = '.';
      robotPosition = nextCell.position;
      grid.array[robotPosition[0]][robotPosition[1]] = '@';
    } else if (nextCell?.value === 'O') {
      const adjBoxCells = [nextCell.position];

      let currentBoxPosition = nextCell.position;
      while (true) {
        const nextBoxPosition = grid.getAdjacent(currentBoxPosition[0], currentBoxPosition[1], direction);
        if (nextBoxPosition?.value !== 'O') break;
        currentBoxPosition = nextBoxPosition.position;
        adjBoxCells.push(currentBoxPosition);
      }

      const [i, j] = adjBoxCells.at(-1)!;
      const nextNonBoxCell = grid.getAdjacent(i, j, direction);

      if (nextNonBoxCell?.value === '.') {
        grid.array[robotPosition[0]][robotPosition[1]] = '.';
        robotPosition = nextCell.position;
        grid.array[robotPosition[0]][robotPosition[1]] = '@';

        adjBoxCells.shift();

        for (const position of [...adjBoxCells, nextNonBoxCell.position]) {
          grid.array[position[0]][position[1]] = 'O';
        }

        grid.array[nextNonBoxCell.position[0]][nextNonBoxCell.position[1]] = 'O';
      }
    }
  }
  const boxes = grid.find('O');

  return boxes.reduce((acc, box) => (acc += 100 * box[0] + box[1]), 0).toString();
};

const evaluateVerticalBoxes = (i: number, j: number, grid: Grid<string>, direction: Direction) => {
  const firstBox = [[i, j]];

  if (grid.array[i][j] === '[') firstBox.push(grid.getAdjacent(i, j, Direction.East)!.position);
  else firstBox.push(grid.getAdjacent(i, j, Direction.West)!.position);

  firstBox.sort((a, b) => a[1] - b[1]);

  const boxes = [firstBox];
  const boxesToProcess = [firstBox];
  let willMove = true;

  while (boxesToProcess.length > 0) {
    const { dy } = directionOffsets.get(direction)!;
    const box = boxesToProcess.shift()!;

    const behindBox = grid.walk(box[0][0] + dy, box[0][1], Direction.East, 2);

    if (behindBox.values.join('') === '[]') {
      const newBox = behindBox.positions;
      boxesToProcess.push(newBox);
      boxes.push(newBox);
    } else if (behindBox.values.join('') === '][') {
      const newBoxLeft = [
        [box[0][0] + dy, behindBox.positions[0][1]],
        [box[0][0] + dy, behindBox.positions[0][1] + 1]
      ];
      const newBoxRight = [
        [box[0][0] + dy, behindBox.positions[1][1]],
        [box[0][0] + dy, behindBox.positions[1][1] + 1]
      ];

      boxesToProcess.push(newBoxLeft);
      boxesToProcess.push(newBoxRight);
      boxes.push(newBoxLeft);
      boxes.push(newBoxRight);
    } else if (behindBox.values.join('') !== '..') {
      willMove = false;
      break;
    }
  }
  console.log(boxes);
  console.log(willMove);
};

export const partTwo = (puzzleInput: string[]) => {
  const formattedInput = split2DArray(puzzleInput, '');
  const grid = new Grid(expandGrid(formattedInput[0]));

  console.log(grid.toString());

  const directions = formattedInput[1].flatMap((line) => line.split('').map((char) => DIRECTION_MAP.get(char)!));
  const robotPosition = grid.find('@')[0];

  // console.log(directions);
  // console.log(robotPosition)

  grid.array[3] = ['#', '#', '.', '.', '.', '[', ']', '[', ']', '@', '.', '.', '#', '#'];
  grid.array[2][6] = '#';
  console.log(grid.toString());

  evaluateVerticalBoxes(4, 6, grid, Direction.North);

  // for (const direction of directions) {
  //   const nextCell = grid.getAdjacent(robotPosition[0], robotPosition[1], direction);

  //   // clear space
  //   if (nextCell?.value == '.') {
  //     grid.array[robotPosition[0]][robotPosition[1]] = '.';
  //     robotPosition = nextCell.position;
  //     grid.array[robotPosition[0]][robotPosition[1]] = '@';
  //   } // Box found
  //   else if (nextCell?.value === '[' || nextCell?.value === ']') {
  //     const firstBox = [nextCell.position];

  //     // get second half of the box
  //   if (nextCell?.value === '[')
  //     firstBox.push(grid.getAdjacent(nextCell.position[0], nextCell.position[1], Direction.East)!.position);
  // else firstBox.push(grid.getAdjacent(nextCell.position[0], nextCell.position[1], Direction.West)!.position);

  // firstBox.sort((a, b) => a[1] - b[1]);
  // const boxes = [firstBox];
  // const boxesToProcess = [firstBox];

  // while (boxesToProcess) {
  //   const { dy } = directionOffsets.get(direction)!;
  //   const box = boxesToProcess.shift()!;
  //   console.log(box);
  //   const behindBox = grid.walk(box[0][0] + dy, box[0][1], Direction.East, 2);

  //     // check cases
  //     // if [][] add two boxes
  //     // if ? [] ? add single box

  //     console.log(behindBox);
  //   }

  //   console.log(firstBox);

  //   // while ()
  // }
  // }
  // console.log(grid.toString(false));
  // const boxes = grid.find('O');

  // return boxes.reduce((acc, box) => (acc += 100 * box[0] + box[1]), 0).toString();
  return 'Part 2 Answer';
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE_3));
  runPuzzle('15', 'warehouse_woes', partOne, partTwo, puzzleInput);
}
