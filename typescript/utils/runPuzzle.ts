import { functionTimer } from './time';

export const runPuzzle = (
  dayNum: string,
  dayName: string,
  partOne: (input: string[]) => string,
  partTwo: (input: string[]) => string,
  puzzle_input: string[]
): void => {
  const { output: p1_output, time: p1_time } = functionTimer(partOne, puzzle_input);
  const { output: p2_output, time: p2_time } = functionTimer(partTwo, puzzle_input);

  console.log('--------------------------------------');
  console.log(`Day ${dayNum}: ${dayName}`);
  console.log('--------------------------------------');
  console.log(`Part One Answer: ${p1_output} - [${p1_time} seconds]`);
  console.log(`Part Two Answer: ${p2_output} - [${p2_time} seconds]`);
  console.log('--------------------------------------');
};
