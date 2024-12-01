import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { functionTimer } from '../../utils/time';

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

const run = () => {
  const mode = InputFile.INPUT; // or InputFile.EXAMPLE

  const puzzle_input = readPuzzleInput(path.resolve(__dirname, mode));

  const { output: p1_output, time: p1_time } = functionTimer(partOne, puzzle_input);
  const { output: p2_output, time: p2_time } = functionTimer(partTwo, puzzle_input);

  console.log('--------------------------------------');
  console.log('Day 01: historian_hysteria');
  console.log('--------------------------------------');
  console.log(`Part One Answer: ${p1_output} - [${p1_time} seconds]`);
  console.log(`Part Two Answer: ${p2_output} - [${p2_time} seconds]`);
  console.log('--------------------------------------');
};

if (require.main === module) {
  run();
}
