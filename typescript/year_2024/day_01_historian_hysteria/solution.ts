import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { functionTimer } from '../../utils/time';

const separateLists = (puzzle_input: string[]): { left: number[]; right: number[] } => {
  const left: number[] = [];
  const right: number[] = [];

  puzzle_input.forEach((line) => {
    const [leftValue, rightValue] = line.split('   ').map(Number);
    left.push(leftValue);
    right.push(rightValue);
  });

  return { left, right };
};

export const partOne = (puzzle_input: string[]) => {
  const { left, right } = separateLists(puzzle_input);

  left.sort((a, b) => a - b);
  right.sort((a, b) => a - b);

  const distances = left.reduce((acc, l, index) => acc + Math.abs(l - right[index]), 0);

  return distances.toString();
};

export const partTwo = (puzzle_input: string[]) => {
  const { left, right } = separateLists(puzzle_input);

  const similarityScore = left.reduce((acc, l) => acc + l * right.filter((r) => r === l).length, 0);

  return similarityScore.toString();
};

const run = () => {
  const filePath = path.resolve(__dirname, InputFile.INPUT);
  const puzzle_input = readPuzzleInput(filePath);

  const { output: p1_output, time: p1_time } = functionTimer(partOne, puzzle_input);
  const { output: p2_output, time: p2_time } = functionTimer(partTwo, puzzle_input);

  console.log('--------------------------------------');
  console.log('Day 01: historian_hysteria');
  console.log('--------------------------------------');
  console.log(`Part One Answer: ${p1_output} - [${p1_time}ms]`);
  console.log(`Part Two Answer: ${p2_output} - [${p2_time}ms]`);
  console.log('--------------------------------------');
};

if (require.main === module) {
  run();
}
