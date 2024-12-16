import path from 'path';
import { Coord, Direction, directionOffsets, Grid } from '../../utils/grid';
import { InputFile, readPuzzleInput, split2DArray } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

const DIRECTION_MAP = new Map<string, Direction>([
  ['^', Direction.North],
  ['>', Direction.East],
  ['v', Direction.South],
  ['<', Direction.West]
]);

const expandGrid = (grid: string[]): string[][] => {
  return grid.map((row) =>
    row.split('').flatMap((cell) => {
      switch (cell) {
        case '#':
          return ['#', '#'];
        case 'O':
          return ['[', ']'];
        case '.':
          return ['.', '.'];
        case '@':
          return ['@', '.'];
        default:
          return ['.', '.'];
      }
    })
  );
};

const moveRobot = (grid: Grid<string>, currentPos: [number, number], nextPos: [number, number]) => {
  grid.array[currentPos[0]][currentPos[1]] = '.';
  grid.array[nextPos[0]][nextPos[1]] = '@';
  return nextPos;
};

export const partOne = (puzzleInput: string[]) => {
  const formattedInput = split2DArray(puzzleInput, '');

  const grid = new Grid(formattedInput[0].map((row) => row.split('')));
  const directions = formattedInput[1].flatMap((line) => line.split('').map((char) => DIRECTION_MAP.get(char)!));

  let robotPosition = grid.find('@')[0];

  for (const direction of directions) {
    const nextCell = grid.getAdjacent(robotPosition[0], robotPosition[1], direction)!;

    if (nextCell?.value == '.') {
      robotPosition = moveRobot(grid, robotPosition, nextCell.position);
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
        robotPosition = moveRobot(grid, robotPosition, nextCell.position);

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
  const { dy } = directionOffsets.get(direction)!;

  const firstBox =
    grid.array[i][j] === '['
      ? [[i, j], grid.getAdjacent(i, j, Direction.East)!.position]
      : [grid.getAdjacent(i, j, Direction.West)!.position, [i, j]];

  const boxes = [firstBox];
  const boxesToProcess = [firstBox];
  let willMove = true;

  const addBox = (positions: Coord[]) => {
    boxesToProcess.push(positions);
    boxes.push(positions);
  };

  while (boxesToProcess.length > 0) {
    const currentBox = boxesToProcess.shift()!;
    const behindBox = grid.walk(currentBox[0][0] + dy, currentBox[0][1], Direction.East, 2);
    const cellsBehindBox = behindBox.values.join('');

    if (cellsBehindBox.includes('#')) {
      willMove = false;
      break; // Movement is blocked, terminate processing
    }

    if (cellsBehindBox === '[]') {
      addBox(behindBox.positions as Coord[]); // Directly behind
    } else {
      if (cellsBehindBox.includes('[')) {
        const newBoxRight: Coord[] = [
          [currentBox[0][0] + dy, behindBox.positions[1][1]],
          [currentBox[0][0] + dy, behindBox.positions[1][1] + 1] // Behind and to the right
        ];
        addBox(newBoxRight);
      }
      if (cellsBehindBox.includes(']')) {
        const newBoxLeft: Coord[] = [
          [currentBox[0][0] + dy, behindBox.positions[0][1] - 1],
          [currentBox[0][0] + dy, behindBox.positions[0][1]] // Behind and to the left
        ];
        addBox(newBoxLeft);
      }
    }
  }
  return { boxes, willMove };
};

export const partTwo = (puzzleInput: string[]) => {
  const formattedInput = split2DArray(puzzleInput, '');
  const grid = new Grid(expandGrid(formattedInput[0]));

  const directions = formattedInput[1].flatMap((line) => line.split('').map((char) => DIRECTION_MAP.get(char)!));
  let robotPosition = grid.find('@')[0];

  for (const direction of directions) {
    const nextCell = grid.getAdjacent(robotPosition[0], robotPosition[1], direction);
    const { dy } = directionOffsets.get(direction)!;

    if (nextCell?.value == '.') {
      grid.array[robotPosition[0]][robotPosition[1]] = '.';
      robotPosition = nextCell.position;
      grid.array[robotPosition[0]][robotPosition[1]] = '@';
    } else if (nextCell?.value == '[' || nextCell?.value == ']') {
      if (direction === Direction.North || direction === Direction.South) {
        const { boxes, willMove } = evaluateVerticalBoxes(nextCell.position[0], nextCell.position[1], grid, direction);

        if (direction === Direction.North) {
          boxes.sort((a, b) => a[0][0] - b[0][0]);
        } else {
          boxes.sort((a, b) => b[0][0] - a[0][0]);
        }

        if (willMove) {
          for (const box of boxes) {
            const [left, right] = box;
            // reset
            grid.array[left[0]][left[1]] = '.';
            grid.array[right[0]][right[1]] = '.';

            // set box
            grid.array[left[0] + dy][left[1]] = '[';
            grid.array[right[0] + dy][right[1]] = ']';
          }
          grid.array[robotPosition[0]][robotPosition[1]] = '.';
          robotPosition = nextCell.position;
          grid.array[robotPosition[0]][robotPosition[1]] = '@';
        }
      } else {
        const [i, j] = nextCell.position;
        const boxParts = [nextCell.position];

        if (grid.array[i][j] === '[') boxParts.push(grid.getAdjacent(i, j, Direction.East)!.position);
        else boxParts.push(grid.getAdjacent(i, j, Direction.West)!.position);

        let currentBoxPosition = boxParts.at(-1)!;
        let willMove = true;
        while (true) {
          const nextBoxPosition = grid.getAdjacent(currentBoxPosition[0], currentBoxPosition[1], direction)!;
          if (nextBoxPosition?.value === '.') break;
          if (nextBoxPosition?.value === '#') {
            willMove = false;
            break;
          }
          currentBoxPosition = nextBoxPosition.position;
          boxParts.push(currentBoxPosition);
        }

        if (direction === Direction.West) {
          boxParts.sort((a, b) => a[1] - b[1]);
        } else {
          boxParts.sort((a, b) => b[1] - a[1]);
        }

        const { dx } = directionOffsets.get(direction)!;

        let start = direction === Direction.West ? true : false;
        if (willMove) {
          for (const side of boxParts) {
            // reset
            grid.array[side[0]][side[1]] = '.';

            // set box
            grid.array[side[0]][side[1] + dx] = start ? '[' : ']';
            start = !start;
          }
          grid.array[robotPosition[0]][robotPosition[1]] = '.';
          robotPosition = nextCell.position;
          grid.array[robotPosition[0]][robotPosition[1]] = '@';
        }
      }
    }
    // clear();
    // console.log(grid.toString(true));
    // console.log(direction);
    // await delay(250);
  }
  const boxes = grid.find('[');
  return boxes.reduce((acc, box) => (acc += 100 * box[0] + box[1]), 0).toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('15', 'warehouse_woes', partOne, partTwo, puzzleInput);
}
