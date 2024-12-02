import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

type SplitLists = { left: number[]; right: number[] };

const separateLists = (puzzle_input: string[]): SplitLists => {
  return puzzle_input.reduce(
    (acc, line) => {
      const [leftValue, rightValue] = line.split('   ').map(Number);
      acc.left.push(leftValue);
      acc.right.push(rightValue);
      return acc;
    },
    { left: [], right: [] } as SplitLists
  );
};

export const partOne = (puzzle_input: string[]) => {
  const { left, right } = separateLists(puzzle_input);

  left.sort((a, b) => a - b);
  right.sort((a, b) => a - b);

  return left.reduce((acc, l, index) => acc + Math.abs(l - right[index]), 0).toString();
};

export const partTwo = (puzzle_input: string[]) => {
  const { left, right } = separateLists(puzzle_input);

  return left.reduce((acc, l) => acc + l * right.filter((r) => r === l).length, 0).toString();
};

if (require.main === module) {
  const puzzle_input = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  runPuzzle('01', 'historian_hysteria', partOne, partTwo, puzzle_input);
}
